'''
Faca um programa que solicite dois numeros ao usuario e informe ao
usuario qual deles  ́e maior.
'''
n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')
if (n1 > n2):
    print(n1 + ' é o maior número')
else:
    if (n2 > n1):
        print(n2 + ' é o maior número')
    else:
        print('ambos os números são o mesmo: ' + n1)