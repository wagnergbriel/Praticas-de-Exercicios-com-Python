#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

def nota_bimestral(nota1, nota2, nota3, nota4):
    media = (nota1 + nota2 + nota3 + nota4)/4
    print(f'A média do aluno é {media}')

if __name__ == "__main__":
    nota1 = int(input('Digite a primeira nota: \n'))
    nota2 = int(input('Digite a segunda nota: \n'))
    nota3 = int(input('Digite a terceira nota: \n'))
    nota4 = int(input('Digite a quarta nota: \n'))
    nota_bimestral(nota1,nota2,nota3,nota4)