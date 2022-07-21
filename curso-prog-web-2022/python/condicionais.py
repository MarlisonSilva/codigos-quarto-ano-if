boolean = True
print('COMEÇO!')
if (boolean):
    print('Entrou na 1ª condição')
    boolean = False
    if (boolean):
        print('Entrou na 2ª condição')
    else:
        print('Não entrou na 2ª condição')
else:
    print('Não entrou na 1ª condição')
print('FIM!')