peso = float(input('Peso en Kg: '))
altura = float(input('Altura en Metros: '))
imc= peso/(altura**2)
print('Tu índice de masa corporal es: ' + str(round(imc,2)))