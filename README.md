# 🚢 Hub Logístico Panamá-Colombia: Machine Learning & Dynamic Pricing para Comercio Exterior

Este proyecto implementa una solución de **Data Science prescriptiva** orientada a la optimización de decisiones comerciales en la **Zona Libre de Colón (Panamá)** para reexportaciones hacia **Colombia**.

A través de modelos predictivos y consumo de APIs financieras en tiempo real, el sistema recomienda el **Incoterm óptimo (FOB vs. DDP)** y calcula el precio ajustado por **riesgo aduanero (DIAN)** y **volatilidad cambiaria (USD/COP)**.

---

## 📌 1. Problema de Negocio

Las empresas comercializadoras que operan en la Zona Libre de Colón enfrentan dos riesgos principales al exportar a mercados latinoamericanos como Colombia:

1. **Retenciones e Inspecciones Aduaneras (Canal Rojo):** Tiempos de almacenamiento no planificados (*demurrage*) que erosionan el margen operativo.
2. **Riesgo Cambiario (USD/COP):** Volatilidad en la TRM del Peso Colombiano cuando se vende bajo esquemas servicializados (*DDP*).

---

## 🏗️ 2. Arquitectura de la Solución

```text
   [ API Pública Colombia ] ---> Ingesta TRM (USD/COP) en Vivo
                │
   [ Cloud Dataset (CSV/S3) ] -> Ingesta de Transacciones (HS Code, Puerto, FOB)
                │
                ▼
   [ Pipeline Python / Scikit-Learn ] -> Preprocesamiento & Feature Engineering
                │
                ▼
   [ Modelo Random Forest ] -> Predicción de Probabilidad de Canal Rojo
                │
                ▼
   [ Motor de Decisiones Incoterms ] -> Selección Automática FOB Colón vs. DDP Bogotá
