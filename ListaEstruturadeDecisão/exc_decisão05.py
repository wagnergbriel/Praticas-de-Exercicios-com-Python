'''
Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
 * A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
 * A mensagem "Reprovado", se a média for menor do que sete;
 * A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''
def calcular_media_aluno(primeiranota:float, segundanota:float):
    media = (primeiranota + segundanota)/2
    if media == 10:
        print(f'Aprovado com distinção. Media:{media:0.1f}')
    elif media >= 7:
        print(f'Aprovado. Media:{media:0.2f}')
    elif media < 7:
        print(f'Reprovado. Media:{media:0.2f}')

if __name__=='__main__':
    primeiranota = float(input('Digite a primeira nota:\n'))
    segundanota = float(input('Digite a segunda nota:\n'))
    calcular_media_aluno(primeiranota, segundanota)
