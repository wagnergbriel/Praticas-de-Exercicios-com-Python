'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''
letra = input('Digite uma letra:\n').upper()
if letra in ('A', 'E', 'I', 'O', 'U'):
    print(f'{letra} é uma vogal')
else:
    print(f'{letra} é uma consoante')
