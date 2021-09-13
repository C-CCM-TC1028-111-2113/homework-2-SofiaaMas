def main():
    #escribe tu código abajo de esta línea
    peso=float(input('Inserte el peso en kg'))
altura=float(input('Inserte altura en m'))

if(peso<=0) or (altura<=0):
    print('Revise sus datos, alguno es erróneo')
else:
    indice=peso/(altura**2)
    if altura<=0:
        print('Revise sus datos, alguno es erróneo')
    elif indice<20:
        print('Tiene peso bajo')
    elif 20<=indice<25:
        print('Tiene peso Normal')
    elif 25<=indice<30:
        print('Tiene sobrepeso')
    elif 30<=indice<40:
        print('Tiene obesidad')
    elif indice>=40:
        print('Tiene obesidad mórbida')
    pass
if __name__=='__main__':
    main()
