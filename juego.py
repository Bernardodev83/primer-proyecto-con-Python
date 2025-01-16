import random


def juego():
    numeroAleatorio = random.randint(1, 100)
    intentos = 0
    adivino = True

    print("Bienvendid@ al juego de adivinanza de numero")
    print("Debes adivinar un numero entre 1 al 100")
    print("Intenta adivinarlo")

    while adivino:
        numeroUsuario = input("Introduzca un numero entre el 1 al 100 : ")

        if numeroUsuario.isdigit():
            numeroUsuario = int(numeroUsuario)
            intentos += 1
            if numeroUsuario < numeroAleatorio:
                print(f"El numero secreto es mayor a {numeroUsuario}")
            elif numeroUsuario > numeroAleatorio:
                print(f"El numero secreto es menor al {numeroUsuario}")
            else:
                print(
                    f"Felicitaciones adivinaste el numero secreto {numeroUsuario}, y lo lograste en {intentos} intentos"
                )
        else:
            print("Debes ingresar un numero valido")


juego()
