#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

def saudacao(turno: str):
    if turno == 'M':
        print('\nBom Dia !!')
    elif turno == 'V':
        print('\nBoa Tarde !!')
    elif turno == 'N':
        print('\nBoa Noite !!')
    else:
        print('Valor Invalido.')

if __name__ == "__main__":
    print('Digitar M-matutino ou V-Vespertino ou N- Noturno para dizer qual é o turno\n')
    turno = str(input('Qual é o seu turno ?\n'))
    saudacao(turno.upper())
