## IMPORT 27/06

import time
import random

## PERSONAJES

Elon = {
    "Puño": 1,
    "Patada": 1.5,
    "Vida": 100,
    "Velocidad": 1,
    "Fuerza": 1,

    "Energia":100,
    "Nombre": "Elon",

}   

Mark = {
    "Puño": 10,
    "Patada": 15,
    "Vida": 100,
    "Velocidad": 1,
    "Fuerza": 1.2,
    "Energia":100,
    "Nombre": "Mark",

}  

msg  = ''' 
    Elon se encuentra sentado en su silla trabajando tranquilamente en su computadora, 
    hasta que recuerda que un dia el tenia que pelear contra Mark, y entonces se puso las pilas.
    
    Dijo que iba a pelear, pero tendria que preparse antes, pero depende de ti que pelee contra un mini peleador, en este caso Nicolas Maduro, para seguir adelante y llegar a Mark Zuckemberg
    Tu elijes:

        1. "Preparse"
        2. "Pelear"

    Tu elijes: '''

inicio = input(msg)

if inicio == "Prepararse":

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
    
    else:
    
        def mensajes1(personaje):
            if personaje["Vida"]>70:
                msg = '''
            se siente fuerte y se rie de su oponente 
            '''
                
            if personaje["Vida"]<70:
                msg = '''
            Elon mira desde lejos una luz blanca 
                '''
            else:
                msg = '''
            NOT 
                '''
            print(msg)
            
        def mensajes2(personaje):
            if personaje["Vida"]>70:
                msg = '''
            Mark no baja su mirada
            '''
                
            if personaje["Vida"]<70:
                msg = '''
            Mark parece estar cansado
            '''
            else:
                msg = '''
            NOT 
                '''
            print(msg)
                    
        def lucha(personaje1,personaje2,DesicionElon='no'):
            if DesicionElon is["Patada","Puño"]:
                personaje1["Vida"] -= personaje2[DesicionElon] * personaje2["Velocidad"]

                print(f"{personaje2['Nombre']} golpea con {DesicionElon}") 
            else:
                DesicionMark = random.choice(["Patada","Puño"])
                print(DesicionMark)
                personaje1["Vida"] -= personaje2[DesicionMark] * personaje2["Velocidad"]
                print(f" {personaje2} golpea con {DesicionMark}")
            
            print(Mark)
            print(Elon)
            
            while Elon["Vida"] > 0 and Mark["Vida"] > 0: 

                msg = '''
                    Elon se siente abrumado por el ensordecedor ruido de la hinchada del publico,
                    pero no puede distraerse, debe de empezar a pelear contra su contrincante, Mark
                    
                    Es hora de Elonear, dijo Elon antes de hacer su primer ataque
                        
                        1. "Patada"
                        2. "Puño"
                        
                    Tu elijes: '''

                DesicionElon = input(msg).capitalize()


                print("        Aqui viene mark!")

                lucha(Elon,Mark)
                mensajes1(Elon)
                lucha(Mark,Elon,DesicionElon)
                mensajes2(Mark)

            print("Game Over")

            if Elon["Vida"] > Mark["Vida"] :
                print("Gano Elon")
            else:
                print("Gano Mark")

