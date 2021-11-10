"""
Faça um Programa para um caixa eletrônico. 
O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor 
 serão fornecidas. 
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O
 valor mínimo é de 10 reais e o máximo de 600 reais. 
O programa não deve se preocupar com a quantidade de notas existentes na máquina.

Exemplo 1: 
Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, 
uma nota de 50, uma nota de 5 e uma nota de 1;

Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, 
uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""
saque = 500
saque = dinheiro

if dinheiro >= 10 and dinheiro <= 600:
    # Calculando a quantidade de notas
    notasde100 = int(dinheiro / 100)
    dinheiro = dinheiro % 100

    notasde50 = int(dinheiro / 50)
    dinheiro = dinheiro % 50

    notasde10 = int(dinheiro / 10)
    dinheiro = dinheiro % 10

    notasde5 = int(dinheiro / 5)
    dinheiro = notasde5 % 5

    notasde1 = dinheiro

    print(
        f"Saque de {saque}, você receberá notas:\n\
                                    {notasde100} de 100,\n\
                                    {notasde50} de 50,\n\
                                    {notasde10} de 10,\n\
                                    {notasde5} de 5,\n\
                                    {notasde1} de 1."
    )

else:
    print("O valor do saque deve está entre 10 e 600 reais.")
