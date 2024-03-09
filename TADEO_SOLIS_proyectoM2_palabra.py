# pedir datos al usuario
while True:
    palabra = input('Por favor ingrese una palabra de entre 4 y 8 letras\n')
    #condiciones de evaluacion de los datos ingresados por el usuario.
    #Si el numero resulta mayor de lo estipulado.
    if len(palabra) > 8:
        num = len(palabra)
        print(f'La palabra contiene demasiadas letras. Son {num} letras en total.\n')
    #si el dato resulta menor de lo estipulado.
    elif len (palabra) < 4:
        num = len(palabra)
        print(f'La palabra no contiene suficientes letras, solo tiene {num} letras.\n')
    #cuando el dato cumple con las especificaciones.
    else:
        #Corroborar que solo se hayan escrito letras en la palabra.
        for i in (palabra):
            if palabra.isdigit():
                print('La palabra solo debe contener letras.\n')
                break
            else:
                continue
        #Caso exitoso = fin del programa.
        print('La palabra es correcta.\n')
        break
    exit
