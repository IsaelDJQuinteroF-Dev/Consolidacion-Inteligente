'''
Reporte Consolidado de Ventas - es un script que toma los reportes mensuales de ventas, 
los consolida, limpia los datos y genera un resumen anual por producto. 
El resultado se guarda en un archivo Excel llamado 'Resumen_Consolidado_Ventas.xlsx'.
Elaborado por: Isael D'Jesús Quintero Fuentes.
'''

import pandas as pd
import os

# 1. Definimos la ubicación de los archivos
carpeta_ventas = './reportes_2026/' # esta es una ubicación genérica.

# Si no existe, la creamos indicandole al usuario que ubique los archivos ahí.
if not os.path.exists(carpeta_ventas):
    os.makedirs(carpeta_ventas)
    print(f"Aviso: Se ha creado la carpeta '{carpeta_ventas}'. Por favor, coloca tus archivos ahí.")

# 2. Seleccionamso los archivos seún su tipo.
archivos = [f for f in os.listdir(carpeta_ventas) if f.endswith(('.csv', '.xlsx'))]

# 3. Creamos la lista donde almacenaremos la información con la que trabajaremos.
todos_los_datos = []

# 4. verificamos si se encontraron archivos para procesar.
if not archivos:
    print("No se encontraron archivos .csv o .xlsx para procesar.")
else:
    print(f"Detectados {len(archivos)} archivos. Iniciando procesamiento...")

# 5. Ejecución del proceso.
    for archivo in archivos:
        ruta = os.path.join(carpeta_ventas, archivo)
        try:
            # Opción Interna: Detectar formato y leer correctamente
            if archivo.endswith('.csv'):
                df_mes = pd.read_csv(ruta)
            elif archivo.endswith('.xlsx'):
                df_mes = pd.read_excel(ruta)
            
            todos_los_datos.append(df_mes)
            print(f"  [OK] Procesado: {archivo}")
        except Exception as e:
            print(f"  [ERROR] No se pudo leer {archivo}: {e}")

# 6. Consolidamos, limpiamos y damos formato.
    if todos_los_datos:

        reporte_anual = pd.concat(todos_los_datos, ignore_index=True)
        
        reporte_anual = reporte_anual.drop_duplicates()
        reporte_anual = reporte_anual.dropna(subset=['Producto', 'Precio'])
        
        reporte_anual['Precio'] = pd.to_numeric(reporte_anual['Precio'], errors='coerce')
        reporte_anual['Cantidad'] = pd.to_numeric(reporte_anual['Cantidad'], errors='coerce')
        
        reporte_anual = reporte_anual.dropna(subset=['Precio', 'Cantidad'])

# 7. Generamos el reporte.
        reporte_anual['Subtotal'] = reporte_anual['Cantidad'] * reporte_anual['Precio']
        resumen = reporte_anual.groupby('Producto')['Subtotal'].sum().reset_index()

# 8. Lo guardamos en excel
        nombre_salida = 'Resumen_Consolidado_Ventas.xlsx'
        resumen.to_excel(nombre_salida, index=False)
        
        print("\n" + "="*40)
        print(f"PROCESO FINALIZADO CON ÉXITO")
        print(f"Archivo generado: {nombre_salida}")
        print("="*40)