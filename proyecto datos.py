# TARJETAS DE CRÉDITO
# DATOS DE LA TARJETA (Unidimensionales)

recoleccion_datos = []

clients = ["Charlie Gregorio", "Juan Gonzalo", "Idalberto Chiavenato", "Amanda Perez"]
recoleccion_datos.append(clients)

num_id = ["402-565852-4", "402-875263-8", "001-562369-7", "001-754683-2"]
recoleccion_datos.append(num_id)

activa = [True, False, True, False]
recoleccion_datos.append(activa)

num_tarjeta = ["5655-5269-7876-9996", "4512-8999-6333-7858", "4555-7886-3621-2222", "4564-8896-0457-4777"]
recoleccion_datos.append(num_tarjeta)

fecha_vencimiento = ["02/27", "05/26", "11/24", "12/23"]
recoleccion_datos.append(fecha_vencimiento)

codigo_seguridad = ["669", "455", "420", "107"]
recoleccion_datos.append(codigo_seguridad)

saldos = [1500.00, 500.00, 2000.00, 7500.00]
recoleccion_datos.append(saldos)

while True:
    opcion = int(input("""Buenas, elija la opción que desee consultar
    1) Unidimensional
    2) Bidimensional
    3) Arreglos de más de dos dimensiones
    4) Matrices poco densas
    5) Matriz Tridiagonal
    6) Matriz Simétrica
    7) Matriz Antisimétrica
    8) Matriz Binaria 
    9) Salir
    
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
        print("Leyenda \nFila: # Tarjeta \nColumna: Mes ")
        for fila in Matriz_transacciones:
            print(f"{fila[0]:<10} | {fila[1]:<10} | {fila[2]:<10}")
    
    elif opcion == 5:
        Matriz_pagos = [
            [200.00, 50.00, 100.00, 0, 0],
            [140.00, 150.00, 25.00, 0],
            [0, 170.00, 180.00, 150.00],
            [0, 0, 180.00, 300.00]
        ]
        print("Historial de Pagos de las Tarjetas:")
        for i, row in enumerate(Matriz_pagos):
            for j, amount in enumerate(row):
                if amount > 0:
                    print(f"Mes {i + 1}, Mes {j + 1}: ${amount} pagado")

        # Imprimir la matriz con barras verticales
        print()
        print("Historial de Pagos de las Tarjetas en forma de matriz:")
        print("Leyenda \nFila: # Tarjeta \nColumna: Mes")
        for fila in Matriz_pagos:
            for elemento in fila:
                print(f"| {elemento:.2f} ", end="")
            print("|")  
    
    
    elif opcion == 6:
        transacciones = [
            [100.0, 200.0, 50.0],
            [50.0, 150.0, 75.0],
            [75.0, 180.0, 90.0]
        ]

        def crear_matriz_simetrica(transacciones):
            n = len(transacciones)
            matriz_simetrica = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(i, n):
                    promedio = (transacciones[i][j] + transacciones[j][i]) / 2
                    matriz_simetrica[i][j] = promedio
                    matriz_simetrica[j][i] = promedio

            return matriz_simetrica
        matriz_simetrica = crear_matriz_simetrica(transacciones)
        
        print("Matriz Simétrica:")
        print("Matriz de Transacciones Agosto-Sep-Oct:")
        for fila in matriz_simetrica:
                print(fila)
        print("Leyenda \nFila: # Tarjeta \nColumna: Mes ")
        print()

    elif opcion == 7:
        transacciones = [
            [100.0, 200.0, 50.0],
            [50.0, 150.0, 75.0],
            [75.0, 180.0, 90.0]
        ]
        def crear_matriz_antisimetrica(transacciones):
            n = len(transacciones)
            matriz_antisimetrica = [[0] * n for _ in range(n)]
            
            for i in range(n):
                for j in range(i, n):
                    diferencia = (transacciones[i][j] - transacciones[j][i]) / 2
                    matriz_antisimetrica[i][j] = -diferencia
                    matriz_antisimetrica[j][i] = diferencia
        
            return matriz_antisimetrica
        matriz_antisimetrica = crear_matriz_antisimetrica(transacciones)
        
        print("Matriz Antisimétrica:")
        print("Matriz de Saldo Disponible Agosto-Sep-Oct:")
        for fila in matriz_antisimetrica:
         print(fila)
        print("Leyenda \nFila: # Tarjeta \nColumna: Mes ")
        print()

    elif opcion == 8:
        matriz_binaria = [[int(activa) for activa in recoleccion_datos[2]]] * 3  # Replicamos la fila 3 veces
        print("Matriz Binaria de Activación de Tarjetas:")
        for fila in matriz_binaria:
         print(fila)
        print()

    elif opcion == 9:
        print("Saliendo...")
        break

    else:
        print("Opción no válida. Introduzca una opción válida.")