# TARJETAS DE CREDITO
# DATOS DE LA TAJETA (Unidimensionales)

recoleccion_datos = []

clients = ["Charlie Gregorio", "Juan Gonzalo", "Idalberto Chiavenato"] 
recoleccion_datos.append(clients)

num_id = ["402-565852-4", "602-875263-8", "451-562369-7"]
recoleccion_datos.append(num_id)

activa = [True, False, True]
recoleccion_datos.append(activa)

num_tarjeta = ["5655-5269-7876-9996", "4512-8999-6333-7858", "4555-7886-3621-2222"]
recoleccion_datos.append(num_tarjeta)

fecha_vencimiento = ["02/27", "05/26", "11/24"]
recoleccion_datos.append(fecha_vencimiento)

codigo_seguridad = ["669", "455", "420"]
recoleccion_datos.append(codigo_seguridad)

saldos = [1500.00, 500.00, 2000.00]
recoleccion_datos.append(saldos)

## Para consultar ##

while True:
    opcion = int(input("""Buenas, elija la opción que desee consultar
    1) Unidimensional
    2) Bidimensional
    3) Arreglos de más de dos dimensiones
    4) Matrices poco densas
    5) Matriz Diagonal
    6) Salir
    
    """))

    if opcion == 1:
        print("Nombre del Cliente:", recoleccion_datos[0])
    elif opcion == 2:
        print("Tarjeta Encontrada:", recoleccion_datos)
        
    elif opcion == 3:
        
# Creamos una matriz de mas de dos arreglos para representar la info de las tarjetas
# Cada fila representa una tarjeta, cada columna un atributo
     credit_card_data = [
     ["5655-5269-7876-9996", '02/27', 1500.00],
     ["4512-8999-6333-7858", '05/26', 500.00],
     ["4555-7886-3621-2222", '11/24', 2000.00]
     ]
# Imprime la información de una tarjeta de credito específica
     print("Número de Tarjeta:", credit_card_data[0][0])
     print("Fecha de Vencimiento:", credit_card_data[0][1])
     print("Saldo Disponible:", credit_card_data[0][2])
     
#####################################################################

    elif opcion == 4:

# Creamos una matriz poco densa para representar transacciones
# Cada fila representa una tarjeta, cada columna un mes 
     Matriz_transacciones = [
     [0, 100.00, 0],
     [50.00, 0, 75.00],
     [0, 25.00, 0]
     ]

# Imprimimos las transacciones de una tarjeta
     print("Transacciones de Tarjeta 1:")
     for month, amount in enumerate(Matriz_transacciones[0]):
       if amount > 0:
        print(f"Enero: ${amount} en transacciones")
########################################################################

    elif opcion == 5:
# Creamos una matriz tridiagonal para representar el historial de pagos
# Cada fila representa una tarjeta, cada columna un mes
     Matriz_pagos = [
     [200.00, 0, 0],
     [0, 150.00, 0],
     [0, 0, 180.00]
     ]
# Imprimimos el historial de pagos de una tarjeta
     print("Historial de Pagos de Tarjeta 2:")
     for i, row in enumerate(Matriz_pagos):
      for j, amount in enumerate(row):
        if amount > 0:
            print(f"Mes {i + 1}, Mes {j + 1}: ${amount} pagado")
############################################################################### 
        
    elif opcion == 6:
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Introduzca un número del 1 al 6.")