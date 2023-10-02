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

while True:
    opcion = int(input("""Buenas, elija la opción que desee consultar
    1) Unidimensional
    2) Bidimensional
    3) Arreglos de más de dos dimensiones
    4) Matrices poco densas
    5) Matriz Tridiagonal
    6) Salir
    
    """))

    if opcion == 1:
        print("Elige el arreglo unidimensional que deseas ver:")
        print("1) Nombres de Clientes")
        print("2) Números de ID")
        print("3) Estado de Activación")
        print("4) Números de Tarjeta")
        print("5) Fechas de Vencimiento")
        print("6) Códigos de Seguridad")
        print("7) Saldos")
        
        sub_opcion = int(input("Ingresa el número de la opción que deseas: "))

        if sub_opcion == 1:
            print("Nombres de Clientes:", recoleccion_datos[0])
        elif sub_opcion == 2:
            print("Números de ID:", recoleccion_datos[1])
        elif sub_opcion == 3:
            print("Estado de Activación:", recoleccion_datos[2])
        elif sub_opcion == 4:
            print("Números de Tarjeta:", recoleccion_datos[3])
        elif sub_opcion == 5:
            print("Fechas de Vencimiento:", recoleccion_datos[4])
        elif sub_opcion == 6:
            print("Códigos de Seguridad:", recoleccion_datos[5])
        elif sub_opcion == 7:
            print("Saldos:", recoleccion_datos[6])
        else:
            print("Opción no válida.")
    
    elif opcion == 2:
        print("Tarjeta Encontrada:")
        for fila in recoleccion_datos:
            print(fila)
    
    elif opcion == 3:
        credit_card_data = [
            ["5655-5269-7876-9996", '02/27', 1500.00],
            ["4512-8999-6333-7858", '05/26', 500.00],
            ["4555-7886-3621-2222", '11/24', 2000.00]
        ]
        print("Tarjetas encontradas:")
        for tarjeta in credit_card_data:
            print(f"{tarjeta[0]} | {tarjeta[1]} | {tarjeta[2]}")
    
    elif opcion == 4:
        Matriz_transacciones = [
            ["$0", "$100.00", "$0"],
            ["$50.00", "$0", "$75.00"],
            ["$0", "$25.00", "$0"]
        ]
        print("Matriz de Transacciones:")
        for fila in Matriz_transacciones:
            print(f"{fila[0]:<10} | {fila[1]:<10} | {fila[2]:<10}")
    
    elif opcion == 5:
        Matriz_pagos = [
            [200.00, 0, 0],
            [0, 150.00, 0],
            [0, 0, 180.00]
        ]
        print("Historial de Pagos de Tarjeta 2:")
        for i, row in enumerate(Matriz_pagos):
            for j, amount in enumerate(row):
                if amount > 0:
                    print(f"Mes {i + 1}, Mes {j + 1}: ${amount} pagado")

        # Imprimir la matriz con barras verticales
        for fila in Matriz_pagos:
            for elemento in fila:
                print(f"| {elemento:.2f} ", end="")
            print("|")  # Agrega una barra vertical al final de cada fila
    
    elif opcion == 6:
        print("Saliendo...")
        break
    
    else:
        print("Opción no válida. Introduzca un número del 1 al 6.")