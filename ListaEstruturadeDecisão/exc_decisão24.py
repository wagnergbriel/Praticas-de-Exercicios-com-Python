'''Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
    O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal.'''

from Exc_Decisão02 import verificar_do_numero
from Exc_Decisão22 import verificar_paridade
from Exc_Decisão23 import verificar_conjunto_numerico

def operacoes_numericas(primeironumero, segundonumero):
    opção = int(input('Digite a opção para escolher a operação desejada:\n\
                    1 - par ou impar\n\
                    2 - positivo ou negativo\n\
                    3 - inteiro ou decimal.\n'))
    if opção == 1:
        print(verificar_paridade(primeironumero))
        print(verificar_paridade(segundonumero))
       
    if opção == 2:
        verificar_do_numero(primeironumero)
        verificar_do_numero(segundonumero)
    
    if opção == 3:
        print(verificar_conjunto_numerico(primeironumero))
        print(verificar_conjunto_numerico(segundonumero))




operacoes_numericas(18.6, 8)