""" Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar 
se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é 
jovem, adulta ou idosa, conforme a média calculada."""
quantidade_de_alunos = int(input("Informe a quantidade de alunos na turma:\n"))
soma_da_idade = 0

for i in range(1, quantidade_de_alunos + 1):
    idade_do_aluno = int(input(f"\nInforme a idade do {i}° aluno:\n"))
    soma_da_idade += idade_do_aluno

media_das_idades = soma_da_idade / quantidade_de_alunos

if media_das_idades > 0 and media_das_idades <= 25:
    print(f"\nA média das idades jovem. Média: {media_das_idades:0.1f}")
elif media_das_idades > 25 and media_das_idades <= 60:
    print(f"\nA média das idades adulta. Média: {media_das_idades:0.1f}")
elif media_das_idades > 60:
    print(f"\nA média das idades idosa. Média: {media_das_idades:0.1f}")
