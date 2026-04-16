#EJERCICO 1
"""
cont = 0
precio = 0

nombre = input('Ingrese su nombre: ')

while not nombre.isalpha():
    print("ERROR. Ingrese un nombre valido")
    nombre = input('Ingrese un nombre valido: ')
    
productos = input("Ingrese la cantidad de productos a comprar: ")

while not productos.isdigit() or productos == "0":
    print("Error. Ingrese un numero valido y diferente de 0")   
    productos = input('Ingrese la cantidad de productos a comprar: ')   

cont += int(productos)

total_sin_desc = 0
total_con_desc = 0

print(f"\nCliente: {nombre}")
print(f"Cantidad de productos: {cont}")

while precio < cont:
    total = input(f'Producto {precio + 1} - Precio: ')
    
    while not total.isdigit():
        print("ERROR. Ingrese un precio válido")
        total = input(f'Producto {precio + 1} - Precio: ')
    
    total = int(total)
    
    descuentos = input("Descuento (S/N): ").lower()

    while descuentos != "s" and descuentos != "n":
        print("ERROR. Ingrese S/N")
        descuentos = input("Descuento (S/N): ").lower()
    
    print(f"Producto {precio + 1} - Precio: {total} Descuento (S/N): {descuentos}")
    
    if descuentos == "s":
        total_con_desc += total * 0.9
    else:
        total_con_desc += total

    total_sin_desc += total

    precio += 1

ahorro = total_sin_desc - total_con_desc
promedio = total_con_desc / cont

print(f"Total sin descuentos: ${total_sin_desc}")
print(f"Total con descuentos: ${total_con_desc:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

"""
#EJERCICIO 2
"""
usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

while intentos < 3:
    print(f"\nIntento {intentos + 1}/3")
    
    usuario = input("Usuario: ")
    clave = input("Clave: ")
    
    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        acceso = True
        break
    else:
        print("Error: credenciales inválidas.")
        intentos += 1

if not acceso:
    print("Cuenta bloqueada.")

while acceso:
    print("\n1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
    
    opcion = input("Opción: ")
    
    if not opcion.isdigit():
        print("Error: ingrese un numero válido.")
        continue
    
    opcion = int(opcion)
     
    if opcion < 1 or opcion > 4:
        print("Error: opción fuera de rango.")
        continue
    
    if opcion == 1:
        print("Inscripto")
    
    elif opcion == 2:
        nueva = input("Nueva clave: ")
        
        if len(nueva) < 6:
            print("Error: minimo 6 caracteres.")
            continue
        
        confirmar = input("Confirmar clave: ")
        
        if nueva != confirmar:
            print("Error: no coinciden.")
        else:
            clave_correcta = nueva
            print("Clave cambiada correctamente.")
    
    elif opcion == 3:
        print("Seguí practicando, vas muy bien 🔥")
    
    elif opcion == 4:
        print("Saliendo...")
        break

"""

#EJERCICIO 3
"""
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

operador = input("Ingrese su nombre: ")

while not operador.isalpha():
    print("ERROR. Nombre inválido")
    operador = input("Ingrese su nombre: ")

while True:
    print("\n1) Reservar turno")
    print("2) Cancelar turno")
    print("3) Ver agenda del día")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")

    opcion = input("Opción: ")

    if not opcion.isdigit():
        print("Error: ingrese un número válido.")
        continue

    opcion = int(opcion)

    if opcion < 1 or opcion > 5:
        print("Error: opción fuera de rango.")
        continue

    if opcion == 1:
        dia = input("Día (1=Lunes, 2=Martes): ")

        while dia != "1" and dia != "2":
            print("ERROR")
            dia = input("Día (1=Lunes, 2=Martes): ")

        nombre = input("Nombre del paciente: ")

        while not nombre.isalpha():
            print("ERROR")
            nombre = input("Nombre del paciente: ")

        if dia == "1":
            if nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre == lunes4:
                print("Paciente ya tiene turno en Lunes")
            else:
                if lunes1 == "":
                    lunes1 = nombre
                elif lunes2 == "":
                    lunes2 = nombre
                elif lunes3 == "":
                    lunes3 = nombre
                elif lunes4 == "":
                    lunes4 = nombre
                else:
                    print("No hay cupos en Lunes")

        else:
            if nombre == martes1 or nombre == martes2 or nombre == martes3:
                print("Paciente ya tiene turno en Martes")
            else:
                if martes1 == "":
                    martes1 = nombre
                elif martes2 == "":
                    martes2 = nombre
                elif martes3 == "":
                    martes3 = nombre
                else:
                    print("No hay cupos en Martes")

    elif opcion == 2:
        dia = input("Día (1=Lunes, 2=Martes): ")

        while dia != "1" and dia != "2":
            print("ERROR")
            dia = input("Día (1=Lunes, 2=Martes): ")

        nombre = input("Nombre del paciente: ")

        while not nombre.isalpha():
            print("ERROR")
            nombre = input("Nombre del paciente: ")

        if dia == "1":
            if lunes1 == nombre:
                lunes1 = ""
            elif lunes2 == nombre:
                lunes2 = ""
            elif lunes3 == nombre:
                lunes3 = ""
            elif lunes4 == nombre:
                lunes4 = ""
            else:
                print("No encontrado")

        else:
            if martes1 == nombre:
                martes1 = ""
            elif martes2 == nombre:
                martes2 = ""
            elif martes3 == nombre:
                martes3 = ""
            else:
                print("No encontrado")

    elif opcion == 3:
        dia = input("Día (1=Lunes, 2=Martes): ")

        while dia != "1" and dia != "2":
            print("ERROR")
            dia = input("Día (1=Lunes, 2=Martes): ")

        if dia == "1":
            print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")
            print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
            print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
            print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")
        else:
            print("Turno 1:", martes1 if martes1 != "" else "(libre)")
            print("Turno 2:", martes2 if martes2 != "" else "(libre)")
            print("Turno 3:", martes3 if martes3 != "" else "(libre)")

    elif opcion == 4:
        ocupados_lunes = 0
        ocupados_martes = 0

        if lunes1 != "": ocupados_lunes += 1
        if lunes2 != "": ocupados_lunes += 1
        if lunes3 != "": ocupados_lunes += 1
        if lunes4 != "": ocupados_lunes += 1

        if martes1 != "": ocupados_martes += 1
        if martes2 != "": ocupados_martes += 1
        if martes3 != "": ocupados_martes += 1

        print("Lunes -> Ocupados:", ocupados_lunes, "Disponibles:", 4 - ocupados_lunes)
        print("Martes -> Ocupados:", ocupados_martes, "Disponibles:", 3 - ocupados_martes)

        if ocupados_lunes > ocupados_martes:
            print("Día con más turnos: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("Día con más turnos: Martes")
        else:
            print("Empate")

    elif opcion == 5:
        print("Sistema cerrado")
        break

"""

#EJERCICIO 4
"""
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

racha_forzar = 0

agente = input("Ingrese su nombre de agente: ")

while not agente.isalpha():
    print("ERROR")
    agente = input("Ingrese su nombre de agente: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    if alarma and tiempo <= 3:
        print("Sistema bloqueado por alarma")
        break

    print(f"\nAgente: {agente}")
    print(f"Energía: {energia} | Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"Código parcial: {codigo_parcial}")
    print(f"Alarma: {'ON' if alarma else 'OFF'}")

    print("\n1) Forzar cerradura")
    print("2) Hackear panel")
    print("3) Descansar")

    opcion = input("Opción: ")

    while not opcion.isdigit():
        print("ERROR")
        opcion = input("Opción: ")

    opcion = int(opcion)

    if opcion < 1 or opcion > 3:
        print("Opción inválida")
        continue

    if opcion == 1:
        racha_forzar += 1

        energia -= 20
        tiempo -= 2

        if racha_forzar == 3:
            alarma = True
            print("Se trabó la cerradura por forzar demasiado")
            continue

        if energia < 40:
            riesgo = input("Riesgo alto. Elegí número (1-3): ")

            while not riesgo.isdigit() or int(riesgo) < 1 or int(riesgo) > 3:
                print("ERROR")
                riesgo = input("Riesgo alto. Elegí número (1-3): ")

            if riesgo == "3":
                alarma = True
                print("Alarma activada")
                continue

        if not alarma:
            cerraduras_abiertas += 1
            print("Cerradura abierta")

    elif opcion == 2:
        racha_forzar = 0

        energia -= 10
        tiempo -= 3

        for i in range(4):
            codigo_parcial += "A"
            print(f"Hackeando... paso {i+1}/4")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Cerradura abierta por hackeo")

    elif opcion == 3:
        racha_forzar = 0

        energia += 15
        if energia > 100:
            energia = 100

        tiempo -= 1

        if alarma:
            energia -= 10

        print("Descansando")

print("\n--- RESULTADO ---")

if cerraduras_abiertas == 3:
    print("Victoria: abriste la bóveda")
elif energia <= 0:
    print("Derrota: sin energía")
elif tiempo <= 0:
    print("Derrota: sin tiempo")
elif alarma and tiempo <= 3:
    print("Derrota: sistema bloqueado por alarma")
else:
    print("Misión fallida")

"""

#EJERCICIO 5
"""
print("--- BIENVENIDO A LA ARENA ---")

nombre = input("Nombre del Gladiador: ")

while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

vida_gladiador = 100
vida_enemigo = 100
pociones = 3

ataque_pesado = 15
ataque_enemigo = 12

turno_gladiador = True

print("\n=== INICIO DEL COMBATE ===")

while vida_gladiador > 0 and vida_enemigo > 0:

    print(f"\n=== NUEVO TURNO ===")
    print(f"{nombre} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")

    if turno_gladiador:

        print("\nElige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        opcion = input("Opción: ")

        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
            print("Error: Ingrese un número válido.")
            opcion = input("Opción: ")

        opcion = int(opcion)

        if opcion == 1:
            daño = ataque_pesado

            if vida_enemigo < 20:
                daño = daño * 1.5

            vida_enemigo -= int(daño)
            print(f">> ¡Atacaste al enemigo por {daño} puntos de daño!")

        elif opcion == 2:
            print(">> ¡Inicias una ráfaga de golpes!")
            for i in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")

        elif opcion == 3:
            if pociones > 0:
                vida_gladiador += 30
                pociones -= 1
                print(">> Recuperaste 30 puntos de vida")
            else:
                print("¡No quedan pociones!")

        turno_gladiador = False

    else:
        vida_gladiador -= ataque_enemigo
        print(f">> ¡El enemigo contraataca por {ataque_enemigo} puntos!")

        turno_gladiador = True

print("\n=== FIN DEL COMBATE ===")

if vida_gladiador > 0:
    print(f"VICTORIA. {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")

"""