while True:
    palabra = input('Por favor ingrese una palabra de entre 4 y 8 letras\n')
    if len(palabra) > 8:
        print('La palabra contiene demasiadas letras.\n')
    elif len (palabra) < 4:
        print('La palabra no contiene suficientes letras.\n')
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
   
