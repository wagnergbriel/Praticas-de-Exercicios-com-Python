'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro
entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada.
'''
multiplicando = int(input('Informe o número para exibir a tabuada que deseja:\n'))
MULTIPLICADOR = 0
print(f'----------Tabuada de {multiplicando}----------')
while MULTIPLICADOR < 10:
    MULTIPLICADOR += 1
    resultado = multiplicando * MULTIPLICADOR
    print(f'{multiplicando} X {MULTIPLICADOR} = {resultado}')
print('--------------------------------')
