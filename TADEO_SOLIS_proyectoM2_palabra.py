while True:
    palabra = input('Por favor ingrese una palabra de entre 4 y 8 letras\n')
    if len(palabra) > 8:
        num = len(palabra)
        print(f'La palabra contiene demasiadas letras. Son {num} letras en total.\n')
    elif len (palabra) < 4:
        num = len(palabra)
        print(f'La palabra no contiene suficientes letras, solo tiene {num} letras.\n')
    else:
        for i in (palabra):
            if palabra.isdigit():
                print('La palabra solo debe contener letras.\n')
                break
            else:
                continue
        print('La palabra es correcta.\n')
        break
    exit
   
