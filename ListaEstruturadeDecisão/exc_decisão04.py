'''Faça um Programa que verifique se uma letra digitada é vogal ou consoante.'''

def verificar_tipo_de_letra(letra):
    if letra in ('A', 'E', 'I', 'O', 'U'):
        print(f'{letra} é uma vogal')
    else:
        print(f'{letra} é uma consoante')

if __name__ == '__main__':
    letra = input('Digite uma letra:\n')
    verificar_tipo_de_letra(letra.upper())
