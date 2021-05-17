#Faça um Programa que peça um número correspondente a um determinado ano e 
# em seguida informe se este ano é ou não bissexto.

def ano_bissexto(ano: int):
    if ano % 4 == 0 and ano % 100 !=0:
        print(f'O ano de {ano} é bissexto.')
    
    else:
        print(f'O ano de {ano} não é bissexto.')


if __name__ == "__main__":
    ano = int(input('Digite o ano:\n'))
    ano_bissexto(ano)