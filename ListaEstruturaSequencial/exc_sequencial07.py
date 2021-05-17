#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

def calcular_area_quadrado(lado):
    areadoquadrado = pow(lado, 2)
    print(f'A área do quadrado é {areadoquadrado}')

    def dobro_area(a):
        print('Dobro da área é',areadoquadrado*areadoquadrado)
    dobro_area(areadoquadrado)


if __name__ == "__main__":
    lado = int(input('Digite o tamanho do lado do quadrado: \n'))
    calcular_area_quadrado(lado)