"""
Faça um Programa para leitura de três notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:

A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""
primeiranota = float(input("Digite a primeira nota:\n"))
segundanota = float(input("Digite a segunda nota:\n"))
terceiranota = float(input("Digite a terceira nota:\n"))
media = (primeiranota + segundanota + terceiranota) / 3

if media == 10:
    print(f"Aprovado com distinção. Media:{media:0.1f}")

elif media >= 7:
    print(f"Aprovado. Media:{media:0.2f}")

elif media < 7:
    print(f"Reprovado. Media:{media:0.2f}")
