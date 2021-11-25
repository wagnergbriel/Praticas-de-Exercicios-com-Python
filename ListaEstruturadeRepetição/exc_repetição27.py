""" Faça um programa que calcule o número médio de alunos por turma. 
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
As turmas não podem ter mais de 40 alunos."""
quantidade_de_turmas = int(input("Informe a quantidade de turmas:\n"))
soma_de_alunos_por_turma = 0
for turma in range(1, quantidade_de_turmas + 1):
    quantidade_alunos_por_turma = int(
        input(f"Informe a quantidade de alunos no {turma}° turma\n")
    )
    if quantidade_alunos_por_turma <= 40:
        soma_de_alunos_por_turma += quantidade_alunos_por_turma
    else:
        print("O número de alunos passou de 40\n")
        quantidade_alunos_por_turma = int(
            input(f"Informe a quantidade de alunos no {turma}° turma\n")
        )

media_de_alunos_por_turma = soma_de_alunos_por_turma / quantidade_de_turmas
print(f"A média de alunos por turma é {media_de_alunos_por_turma}")
