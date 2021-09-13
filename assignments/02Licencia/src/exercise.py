
def main():
    #Escribe tu código debajo de esta línea
    edad=int(input('Coloca tu edad'))
id_oficial=str(input('Cuentas con identificación oficial? (si/no):'))

if edad<0:
    print('Respuesta incorrecta')
elif edad>=18 and id_oficial == 'si':
    print('Trámite de licencia concedido')
elif edad<=18 and id_oficial == 'si':
    print('No cumple con los requisitos')
    elif edad>=18 and id_oficial == 'no':
    print('No cumple con los requisitos')
elif edad<=18 and id_oficial == 'no':
    print('No cumple con los requisitos')
elif id_oficial != 'si' or 'no':
    print('Respuesta incorrecta')
    pass


if __name__ == '__main__':
    main()
