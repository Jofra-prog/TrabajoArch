# Función para leer el archivo CSV y convertirlo en una lista de diccionarios
def leer_csv(x):
    with open(x, 'r', encoding='utf-8') as archivo:
        lineasar = archivo.readlines()
    
    # Obtener los encabezados de las columnas
    encabezados = lineasar[0].strip().split(',')
    
    # Crear una lista de diccionarios para almacenar los datos
    datos = []
    for linea in lineasar[1:]:
        valores = linea.strip().split(',')
        fila = dict(zip(encabezados, valores))
        datos.append(fila)
        
    return datos

# Función para filtrar las compras realizadas en un país dado
def filtrar_por_pais(datos, pais):
    compras_pais = [fila for fila in datos if fila['Country'] == pais]
    return compras_pais

# Leer los datos del archivo CSV
while True:
    try:
        name =input("Ingrese la ruta que desea buscar \n")
        datos = leer_csv(name)
        break
    except FileNotFoundError:
        print("El archivo no fue encontrado o esta mal escrito, reescribalo correctamente")
        

# Filtrar las compras realizadas en un país dado
while True:
    pais = input("Ingrese el pais que desea buscar las compras \n")
    compras_pais = filtrar_por_pais(datos, pais)
    if compras_pais:
        total_compras = len(compras_pais)
        print(f"Total de compras realizadas en {pais}: {total_compras}")
        break
    else:
        print(f"El país '{pais}' no está en la lista. Inténtelo de nuevo.")
