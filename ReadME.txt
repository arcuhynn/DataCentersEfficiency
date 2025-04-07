# 🌱 Calculadora de Eficiencia Energética para Data Centers

Esta aplicación desarrollada con Streamlit permite analizar el consumo energético de cuartos de comunicaciones o data centers en empresas. Genera recomendaciones automáticas para mejorar la eficiencia, reducir emisiones de carbono y optimizar costos.

---

## 🚀 Características
- Subida de archivos CSV con datos operativos.
- Cálculo automático de variables derivadas clave.
- Motor de reglas que genera recomendaciones personalizadas.
- Visualización de recomendaciones más frecuentes.
- Dashboard interactivo con filtros y KPIs (energía, emisiones, costo).
- Exportación de resultados con recomendaciones.

---

## 📁 Estructura del proyecto
```
├── app.py                 # Aplicación principal de Streamlit
├── requirements.txt       # Dependencias para correr la app
└── README.md              # Este archivo
```

---

## 📥 Instrucciones de uso local
1. Clona este repositorio:
```bash
git clone https://github.com/tu_usuario/streamlit-efficiency-app.git
cd streamlit-efficiency-app
```

2. Crea un entorno virtual y actívalo:
```bash
python -m venv venv
source venv/bin/activate    # En Windows: venv\Scripts\activate
```

3. Instala dependencias:
```bash
pip install -r requirements.txt
```

4. Corre la app:
```bash
streamlit run app.py
```

---

## ☁️ Despliegue en Streamlit Cloud
Puedes publicar esta app en [Streamlit Cloud](https://streamlit.io/cloud) conectando este repositorio con tu cuenta de GitHub.

---

## 📊 Ejemplo de datos esperados (CSV)
El archivo debe tener las siguientes columnas:
- CPU_Usage_%
- RAM_Usage_%
- Disk_IO_MBps
- Network_IO_MBps
- Ambient_Temp_C
- Power_Usage_Effectiveness
- Server_Age_Years
- Power_kWh
- CO2_Emissions_kg
- Electric_Cost_USD

---

## ✨ Autor
**Mercedes Perea**  
Líder en tecnología, sostenibilidad y ciencia de datos.

---

## 📄 Licencia
MIT
