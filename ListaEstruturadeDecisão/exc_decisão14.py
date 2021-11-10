"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
    Entre 9.0 e 10.0        A
    Entre 7.5 e 9.0         B
    Entre 6.0 e 7.5         C
    Entre 4.0 e 6.0         D
    Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C 
    ou “REPROVADO” se o conceito for D ou E.
"""
primeiranota = float(input("Digite a primeira nota:\n"))
segundanota = float(input("Digite a segunda nota:\n"))
media = (primeiranota + segundanota) / 2

if media >= 0 and media < 4:
    print(f"Sua nota é {media:0.1f}, conceito E. Está Reprovado.")

elif media >= 4 and media < 6:
    print(f"Sua nota é {media:0.1f}, conceito D. Está Reprovado.")

elif media >= 6 and media < 7.5:
    print(f"Sua nota é {media:0.1f}, conceito C. Está Aprovado.")

elif media >= 7.5 and media < 9:
    print(f"Sua nota é {media:0.1f}, conceito B. Está Aprovado.")

elif media >= 9 and media <= 10:
    print(f"Sua nota é {media:0.1f}, conceito A. Está Aprovado.")
