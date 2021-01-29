#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

def verificar_letra(letra):
    if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
            print(f'{letra} é uma vogal')
    else:
        print(f'{letra} é uma consoante')

if __name__ == '__main__':
    letra = input('Digite uma letra:\n')
    verificar_letra(letra.upper())