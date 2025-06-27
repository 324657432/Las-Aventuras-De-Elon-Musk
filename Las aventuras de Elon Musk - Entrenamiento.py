import time
import random

# PERSONAJES
Elon = {
    "Puno": 1,
    "Patada": 1.5,
    "Vida": 100,
    "Velocidad": 0,
    "Fuerza": 1,
    "Energia": 100,
}

Mark = {
    "Puno": 10,
    "Patada": 15,
    "Vida": 100,
    "Velocidad": 5,
    "Fuerza": 1.2,
}

def mostrar_estadisticas():
    print("\n--- ESTADÍSTICAS DE ELON ---")
    for clave, valor in Elon.items():
        print(f"{clave}: {valor}")
    print("-----------------------------\n")

def ejercicio_realizado():
    mostrar_estadisticas()
    continuar = input("¿Querés seguir entrenando o ya pelear?\n1. Seguir entrenando\n2. Pelear\nTu elección: ")
    return continuar == "1"

def entrenar():
    entrenando = True
    while entrenando:
        eleccion_entrenamiento = input("Elegí qué querés entrenar:\n1. Patada\n2. Puño\n3. Velocidad\nTu elección: ")

        if eleccion_entrenamiento == "1":
            opcion = input("Elegí el ejercicio:\n1. Patada alta (-15 energía)\n2. Patada media (-10 energía)\n3. Patada baja (-5 energía)\nTu elección: ")
            if opcion == "1":
                print("Buena elección. Ganaste +3 fuerza y +3 patada.")
                Elon["Fuerza"] += 3
                Elon["Patada"] += 3
                Elon["Energia"] -= 15
            elif opcion == "2":
                print("Buena elección. Ganaste +2 fuerza y +2 patada.")
                Elon["Fuerza"] += 2
                Elon["Patada"] += 2
                Elon["Energia"] -= 10
            elif opcion == "3":
                print("Buena elección. Ganaste +1 fuerza y +1 patada.")
                Elon["Fuerza"] += 1
                Elon["Patada"] += 1
                Elon["Energia"] -= 5

        elif eleccion_entrenamiento == "2":
            opcion = input("Elegí el ejercicio:\n1. Puño alto (-15 energía)\n2. Puño medio (-10 energía)\n3. Puño bajo (-5 energía)\nTu elección: ")
            if opcion == "1":
                print("Buena elección. Ganaste +3 fuerza y +3 puño.")
                Elon["Fuerza"] += 3
                Elon["Puno"] += 3
                Elon["Energia"] -= 15
            elif opcion == "2":
                print("Buena elección. Ganaste +2 fuerza y +2 puño.")
                Elon["Fuerza"] += 2
                Elon["Puno"] += 2
                Elon["Energia"] -= 10
            elif opcion == "3":
                print("Buena elección. Ganaste +1 fuerza y +1 puño.")
                Elon["Fuerza"] += 1
                Elon["Puno"] += 1
                Elon["Energia"] -= 5

        elif eleccion_entrenamiento == "3":
            opcion = input("Elegí el ejercicio:\n1. Skipping rapidísimo (-15 energía)\n2. Skipping normal (-10 energía)\n3. Trotecito (-5 energía)\nTu elección: ")
            if opcion == "1":
                print("Buena elección. Ganaste +3 fuerza y +3 velocidad.")
                Elon["Fuerza"] += 3
                Elon["Velocidad"] += 3
                Elon["Energia"] -= 15
            elif opcion == "2":
                print("Buena elección. Ganaste +2 fuerza y +2 velocidad.")
                Elon["Fuerza"] += 2
                Elon["Velocidad"] += 2
                Elon["Energia"] -= 10
            elif opcion == "3":
                print("Buena elección. Ganaste +1 fuerza y +1 velocidad.")
                Elon["Fuerza"] += 1
                Elon["Velocidad"] += 1
                Elon["Energia"] -= 5

        entrenando = ejercicio_realizado()

# INICIO DEL JUEGO
msg = ''' 
Elon Musk está en su compu cuando se acuerda que tiene que pelear contra Mark Zuckerberg.
Pero primero tiene que prepararse.

¿Qué querés hacer?
1. Prepararse
2. Pelear directamente

Tu elección: '''

inicio = input(msg)

if inicio == "1":
    print("Preparate para entrenar. Tenés distintos ejercicios para hacer.")
    entrenar()
elif inicio == "2":
    print("¡A pelear directamente!")