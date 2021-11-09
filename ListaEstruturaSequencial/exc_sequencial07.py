'''
    Faça um Programa que calcule a área de um quadrado, 
    em seguida mostre o dobro desta área para o usuário.
'''

lado = int(input('Digite o tamanho do lado do quadrado: \n'))
areadoquadrado = pow(lado, 2)
print(f'A área do quadrado é {areadoquadrado}')
print('Dobro da área é',areadoquadrado*areadoquadrado)
