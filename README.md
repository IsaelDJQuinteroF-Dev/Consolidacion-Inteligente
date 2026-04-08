# 📊 Consolidación Inteligente de Ventas (CSV & Excel)

### 🚀 El Problema
En entornos administrativos y comerciales, la información suele estar dispersa en múltiples archivos de diferentes formatos. Consolidar manualmente reportes mensuales de ventas puede tomar horas y es propenso a errores humanos (duplicados, formatos de moneda incorrectos, datos faltantes).

### 💡 La Solución
Este script de Python actúa como un **procesador automático** que:
1. **Detecta y lee** automáticamente archivos tanto en formato `.csv` como `.xlsx` dentro de una carpeta.
2. **Limpia los datos** eliminando registros duplicados y gestionando valores nulos.
3. **Estandariza formatos**, asegurando que las columnas de 'Precio' y 'Cantidad' sean tratadas como números para cálculos financieros precisos.
4. **Genera un reporte ejecutivo** en Excel con el resumen total de ventas por producto.

### 🛠️ Tecnologías Utilizadas
* **Python 3.x**
* **Pandas**: Para la manipulación y análisis de datos.
* **Openpyxl**: Para la compatibilidad con archivos Excel modernos.
* **OS**: Para la gestión automatizada de rutas y carpetas.

### 📈 Valor Agregado para el Negocio
* **Reducción de Tiempo**: Pasa de horas de trabajo manual a segundos de procesamiento.
* **Integridad de Datos**: Garantiza que los totales financieros sean exactos al aplicar filtros de limpieza profesional.
* **Escalabilidad**: El código funciona igual de bien con 10 o con 100 archivos mensuales.

---
**Autor:** Isael D. Quintero F.
*Administrador especializado en la optimización de procesos mediante Python.*
