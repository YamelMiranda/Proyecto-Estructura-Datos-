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
    9) Colas
    10) Pilas
    11) Salir
    
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
        matriz_binaria = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 1] ]
 
        print("Matriz Binaria de Pago de Tarjetas por mes:")
        print ("Mes de Septiembre\n")
        for fila in matriz_binaria:
            print(' '.join(map(str, fila)))
        print()

    elif opcion == 9:
        cola_tarjetas = []

        def add(cliente, num_id, num_tarjeta):
            nueva_tarjeta = {
                "cliente": cliente,
                "num_id": num_id,
                "num_tarjeta": num_tarjeta
            }
            cola_tarjetas.append(nueva_tarjeta)
            print(f"Se ha agregado la tarjeta de crédito de {cliente} a la cola.")

        def remove():
            if not cola_tarjetas:
                print("La cola de tarjetas de crédito está vacía.")
            else:
                tarjeta = cola_tarjetas.pop(0)
                print(f"Se ha retirado la tarjeta de crédito de {tarjeta['cliente']} de la cola.")
                return tarjeta

        def buscar_por_id(num_id):
            for tarjeta in cola_tarjetas:
                if tarjeta["num_id"] == num_id:
                    print(f"Tarjeta encontrada - Cliente: {tarjeta['cliente']}, Número de Identificación: {tarjeta['num_id']}")
                    return tarjeta
            print(f"No se encontró ninguna tarjeta con el número de identificación {num_id}.")
            return None

        def mostrar_menu():
            print("\nMenú de opciones:")
            print("1) Agregar tarjeta de crédito (Add)")
            print("2) Eliminar tarjeta de crédito(Remove)")
            print("3) Buscar tarjeta de crédito por número de identificación(peek)")
            print("4) Salir")

        while True:
            mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                cliente = input("Ingrese el nombre del cliente: ")
                num_id = input("Ingrese el número de identificación: ")
                num_tarjeta = input("Ingrese el número de tarjeta de crédito: ")
                add(cliente, num_id, num_tarjeta)
            elif opcion == "2":
                removed_card = remove()
            elif opcion == "3":
                num_id = input("Ingrese el número de identificación que desea buscar: ")
                buscar_por_id(num_id)
            elif opcion == "4":
                print("Saliendo del programa. ¡Hasta luego!")
                break

    elif opcion == 10:
        pila_clientes = []
        pila_num_id = []
        pila_num_tarjeta = []

        def push_cliente(cliente):
            pila_clientes.append(cliente)
            print(f"Se ha agregado a la pila de clientes a {cliente}.")

        def push_num_id(num_id):
            pila_num_id.append(num_id)
            print(f"Se ha agregado a la pila de números de identificación el valor {num_id}.")

        def push_num_tarjeta(num_tarjeta):
            pila_num_tarjeta.append(num_tarjeta)
            print(f"Se ha agregado a la pila de números de tarjeta de crédito el valor {num_tarjeta}.")

        def pop_cliente():
            if not pila_clientes:
                print("La pila de clientes está vacía.")
            else:
                cliente = pila_clientes.pop()
                print(f"Se ha obtenido y eliminado de la pila de clientes a {cliente}.")
                return cliente

        def pop_num_id():
            if not pila_num_id:
                print("La pila de números de identificación está vacía.")
            else:
                num_id = pila_num_id.pop()
                print(f"Se ha obtenido y eliminado de la pila de números de identificación el valor {num_id}.")
                return num_id

        def pop_num_tarjeta():
            if not pila_num_tarjeta:
                print("La pila de números de tarjeta de crédito está vacía.")
            else:
                num_tarjeta = pila_num_tarjeta.pop()
                print(f"Se ha obtenido y eliminado de la pila de números de tarjeta de crédito el valor {num_tarjeta}.")

        def peek_num_id():
            if not pila_num_id:
                print("La pila de números de identificación está vacía.")
            else:
                num_id = pila_num_id[-1]
                print(f"El siguiente valor de salida de la pila de números de identificación es {num_id}.")

        def mostrar_menu():
            print("\nMenú de opciones:")
            print("1. Agregar tarjeta de crédito")
            print("2. Eliminar tarjeta de crédito")
            print("3. Buscar tarjeta de crédito")
            print("4. Salir")

        while True:
            mostrar_menu()
            opcion = input("Seleccione una opción (1/2/3/4): ")

            if opcion == "1":
                cliente = input("Ingrese el nombre del cliente: ")
                num_id = input("Ingrese el número de identificación: ")
                num_tarjeta = input("Ingrese el número de tarjeta de crédito: ")
                push_cliente(cliente)
                push_num_id(num_id)
                push_num_tarjeta(num_tarjeta)
            elif opcion == "2":
                pop_cliente()
                pop_num_id()
                pop_num_tarjeta()
            elif opcion == "3":
                opcion_busqueda = input("Buscar número de Identificación: ")
                if opcion_busqueda == "1":
                    num_id = input("Ingrese el número de identificación que desea buscar: ")
                    if num_id in pila_num_id:
                        print(f"Tarjeta encontrada - Número de Identificación: {num_id}")
                    else:
                        print(f"No se encontró ninguna tarjeta con el número de identificación {num_id}.")
            elif opcion == "4":
             print("Saliendo del programa. ¡Hasta luego!")
            

    elif opcion == 11:
        print("Saliendo...")
        break