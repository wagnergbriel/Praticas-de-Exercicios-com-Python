""" Faça um programa que calcule o número médio de alunos por turma. 
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
As turmas não podem ter mais de 40 alunos."""
quantidadeturmas = int(input("Informe a quantidade de turmas:\n"))
somadealunosporturma = 0
for turma in range(1, quantidadeturmas + 1):
    quantidadealunosporturma = int(
        input(f"Informe a quantidade de alunos no {turma}° turma\n")
    )
    if quantidadealunosporturma <= 40:
        somadealunosporturma += quantidadealunosporturma
    else:
        print("O número de alunos passou de 40\n")
        quantidadealunosporturma = int(
            input(f"Informe a quantidade de alunos no {turma}° turma\n")
        )

mediadealunosporturma = somadealunosporturma / quantidadeturmas
print(f"A média de alunos por turma é {mediadealunosporturma}")
