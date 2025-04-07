import streamlit as st
import pandas as pd
import numpy as np
from collections import Counter

# Título y descripción
st.title("Calculadora de Eficiencia Energética para Data Centers")
st.markdown("""
Esta herramienta analiza el consumo energético de tus cuartos de comunicaciones y genera recomendaciones personalizadas para mejorar la eficiencia.
""")

# Subida de archivo
uploaded_file = st.file_uploader("Sube tu archivo con datos (CSV)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Derivar variables clave
    df['Cost_per_kWh'] = df['Electric_Cost_USD'] / df['Power_kWh']
    df['CO2_per_kWh'] = df['CO2_Emissions_kg'] / df['Power_kWh']
    df['Power_per_Age'] = df['Power_kWh'] / (df['Server_Age_Years'] + 1)
    df['Temp_efficiency_ratio'] = df['Ambient_Temp_C'] / df['Power_Usage_Effectiveness']
    df['CPU_CO2_ratio'] = df['CPU_Usage_%'] / df['CO2_Emissions_kg']
    df['RAM_CO2_ratio'] = df['RAM_Usage_%'] / df['CO2_Emissions_kg']

    # Generar recomendaciones
    def generar_recomendaciones(row):
        recomendaciones = []
        if row['CO2_per_kWh'] > 1.0:
            recomendaciones.append("Reducir emisiones de carbono por unidad de energía.")
        if row['Power_per_Age'] > 300:
            recomendaciones.append("Evaluar renovación tecnológica de servidores antiguos.")
        if row['Temp_efficiency_ratio'] > 20:
            recomendaciones.append("Revisar HVAC o aislamiento térmico.")
        if row['Cost_per_kWh'] > 0.2:
            recomendaciones.append("Optimizar costo energético renegociando tarifas.")
        if row['CPU_CO2_ratio'] < 0.05:
            recomendaciones.append("Revisar eficiencia de uso de CPU.")
        if row['RAM_CO2_ratio'] < 0.05:
            recomendaciones.append("Optimizar uso de memoria.")
        return recomendaciones if recomendaciones else ["Consumo energético aceptable."]

    df['Recomendaciones'] = df.apply(generar_recomendaciones, axis=1)

    # Generar semáforo de eficiencia
    def clasificar_eficiencia(row):
        n_recs = len(row['Recomendaciones'])
        if "Consumo energético aceptable." in row['Recomendaciones']:
            return "🟢 Eficiente"
        elif n_recs <= 2:
            return "🟡 Medio"
        else:
            return "🔴 Crítico"

    df['Semaforo'] = df.apply(clasificar_eficiencia, axis=1)

    # Mostrar resultados
    st.subheader("Resultados y Recomendaciones")
    st.dataframe(df[['Power_kWh', 'CO2_per_kWh', 'Power_per_Age', 'Temp_efficiency_ratio',
                     'Cost_per_kWh', 'CPU_CO2_ratio', 'RAM_CO2_ratio', 'Recomendaciones', 'Semaforo']])

    # Visualizar recomendaciones
    st.subheader("Visualización de Recomendaciones Generadas")
    all_recs = sum(df['Recomendaciones'], [])
    rec_counts = pd.DataFrame.from_dict(Counter(all_recs), orient='index', columns=['Frecuencia'])
    rec_counts = rec_counts.sort_values(by='Frecuencia', ascending=False)
    st.bar_chart(rec_counts)

    # Dashboard adicional
    st.subheader("Dashboard de Impacto y Filtros")
    rec_filter = st.multiselect("Filtrar por tipo de recomendación", rec_counts.index.tolist())

    if rec_filter:
        df_filtered = df[df['Recomendaciones'].apply(lambda recs: any(r in recs for r in rec_filter))]
        st.write(f"Mostrando {len(df_filtered)} registros que aplican a las recomendaciones seleccionadas.")
        st.dataframe(df_filtered[['Power_kWh', 'CO2_per_kWh', 'Cost_per_kWh', 'Recomendaciones', 'Semaforo']])
        st.metric("Promedio de consumo energético (kWh)", round(df_filtered['Power_kWh'].mean(), 2))
        st.metric("Promedio de emisiones CO2 (kg)", round(df_filtered['CO2_per_kWh'].mean(), 2))
        st.metric("Costo promedio por kWh", round(df_filtered['Cost_per_kWh'].mean(), 4))
        st.markdown(f"**Distribución de eficiencia:**\n\n{df_filtered['Semaforo'].value_counts().to_frame().to_markdown()}")
    else:
        st.info("Selecciona uno o más tipos de recomendaciones para ver su impacto.")

    # Descargar resultados
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Descargar resultados", csv, "resultados_eficiencia.csv", "text/csv")
else:
    st.info("Por favor sube un archivo CSV para iniciar el análisis.")


