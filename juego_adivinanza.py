

import random


def juego():

    numeroAleatorio = random.randint(1, 100)
    intentos = 0
    adivinanza = True

    print('Bienvenid@ al juego adivinanza')
    print('Debes adivinar un numero entre el 1 al 100')
    print('intentalo')

    while adivinanza:
        numeroUsuario = input('Introduzca un numero entre el 1 al 100: ')

        if numeroUsuario.isdigit():
            numeroUsuario = int(numeroUsuario)
            intentos += 1

            if numeroUsuario < numeroAleatorio:
                print(f'El numero secreto es mayor {numeroUsuario}')
            elif numeroUsuario > numeroAleatorio:
                print(f'El numero secreto es menor al {numeroUsuario}')
            else:
                print(f'Felicitaciones lo lograste es numero secreto es: {numeroAleatorio} y lo hiciste en {intentos} intentos ')        
        else:
            print('Desbes ingresar un numero valido')    


juego()            