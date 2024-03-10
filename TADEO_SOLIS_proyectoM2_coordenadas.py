#Pedirle datos al usuario
while True:
    X = int (input('Por favor, ingrese la coordenada del eje X\n'))
    Y = int(input('por favor, ingree la coordenada del eje Y\n'))
    #Si la coordenanda resulta estar en el origen
    if X == 0 & Y == 0:
        print('la coordenada se encuentra en el origen.\n')
        break
    #si la coordenada resulta estar en el eje Y
    elif X == 0:
        print(f'La coordenada se encuentra en el punto {Y} del eje Y.\n') 
        break
    #si la coordenada resulta estar en el eje X
    elif Y == 0:
        print(f'La coordenada se encuentra en el punto {X} del eje X.\n')   
        break
    #Si la coordenada es mayor a 0 en sus dos datos, se encuentra en el cuadrante II
    elif X > 0 and Y > 0:
        print('La coordenada se encuentra en el cuadrante II.\n')
        break
    #si la coordenada resulta menor a 0 en X y mayor en Y se encuentra en el cuadrante I
    elif X < 0 and Y > 0:
        print('La coordenada se encuentra en el cuadrante I.\n')
        break
    #Si la coordenada resulta ser mayor a 0 en X y menor en Y se encuentra en el cuadrante VI
    elif X > 0 and Y < 0:
        print('La coordenada se encunetra en el cuadrante VI.\n')
        break
    #Si la coordenada resulta menor a 0 en sus dos datos se encuentra en cuadrante III
    elif X < 0 and Y < 0:
        print('La coordenada se encunetra en el cuadrante III.\n')
        break
    #cualquier otro resultado indica que s eingreso un apartado invalido
    else:
        print(' Por favor ingresar numeros validos.\n')
        break
exit    
    