'''
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe o valor
válido.
'''
bool = True
while(bool):
    nota = int(input('Digite uma nota entre 0 e 10.\n'))
    
    if nota == 10:
        print('Você acertou o valor da nota')
        bool = False