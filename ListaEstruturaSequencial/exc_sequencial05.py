#Faça um Programa que converta metros para centímetros.

def converter_metro_para_centimetro(metro):
    centimetro = metro/0.010000
    print(f'{metro} m é {centimetro} cm')

if __name__ == "__main__":
    print('\n------- Converção de Metro para Centimetro ------\n')
    m = int(input('Quantos metro(s) deseja converter ?\n'))
    converter_metro_para_centimetro(m)