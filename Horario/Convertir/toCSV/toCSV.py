import os
import pandas as pd

# Directorio de entrada de los archivos .xlsx
carpeta_entrada = 'D:/Algo/Win/VSC/pocotu/tod/Proy/Horario/Convertir/toCSV/XLSXs'

# Directorio de salida de los archivos .csv
carpeta_salida = 'D:/Algo/Win/VSC/pocotu/tod/Proy/Horario/Convertir/toCSV/CSVs'

# Obtener la lista de archivos .xlsx en el directorio de entrada
archivos_xlsx = [f for f in os.listdir(carpeta_entrada) if f.endswith('.xlsx')]

# Recorrer cada archivo .xlsx y convertirlo a .csv
for archivo_xlsx in archivos_xlsx:
    # Crear el nombre completo de archivo de entrada y salida
    input_file_path = os.path.join(carpeta_entrada, archivo_xlsx)
    output_file_path = os.path.join(carpeta_salida, os.path.splitext(archivo_xlsx)[0] + '.csv')
    
    # Leer el archivo .xlsx y guardarlo como .csv en el directorio de salida
    df = pd.read_excel(input_file_path)
    df.to_csv(output_file_path, index=None, header=True)

    print(f"Convertido '{input_file_path}' a '{output_file_path}'")

print("Proceso completado")