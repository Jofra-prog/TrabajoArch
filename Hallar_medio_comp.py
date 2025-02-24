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

# Función para filtrar las compras realizadas por metodo de pago dado
def filtrar_por_metodo_pago(datos, pago):
    compras_pago = [fila for fila in datos if fila['Payment_Type'] == pago]
    return compras_pago

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
    pago = input("Ingrese el metodo de pago que desea buscar las compras \n")
    metodopago = filtrar_por_metodo_pago(datos, pago)
    if metodopago:
        total_compras = len(metodopago)
        print(f"Total de compras realizadas en {pago}: {total_compras}")
        break
    else:
        print(f"El metodo de pago '{pago}' no está en la lista. Inténtelo de nuevo.")

