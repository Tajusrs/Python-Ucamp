import math
Mens_err= ('Por favor ingrese un valor valido')
Form_err= ('Formato invalido, intente nuevamente.\n')
#pedir nombre al usuario.
ap= str(input('Por favor digite su apellido paterno.\n'))
am= str(input('Por favor digite su apellido materno.\n'))
nom= str(input('Por favor ingrese su(s) nombre(s). \n'))

#pedir edad al usuario
ed_con= False
while ed_con == False:
    try:
        edad= int(input('Por favor ingrese su edad en años.\n'))
        if edad>0:
            ed_con = True
        else:
            print(Mens_err)
    except ValueError:
        print(Form_err)

#pedir peso al usuario
pes_con= False
while pes_con==False:
    try:
        peso= float(input('Por favor digite su peso en Kg.\n'))
        if peso>3.2:
            pes_con = True
        else:
            print (Mens_err)
    except ValueError:
        print(Form_err)

#Pedir estatura al usuario
ets_cond= False
while ets_cond == False:
    try:
        estatura= float(input('Por favor ingrese su estatura en metros.\n'))
        if estatura> 0.65 and estatura<2.75:
            ets_cond = True
        else:
            print(Mens_err)
    except ValueError:
        print(Form_err)

#calcular imc
imc= (peso / (estatura**2))
print(f'Hola, {nom}, {ap}, {am}, su imc es de {math.trunc(imc)}')
