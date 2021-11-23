""" Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar 
se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é 
jovem, adulta ou idosa, conforme a média calculada."""
quantidadealunos = int(input("Informe a quantidade de alunos na turma:\n"))
somadaidade = 0

for i in range(1, quantidadealunos + 1):
    idadedoaluno = int(input(f"\nInforme a idade do {i}° aluno:\n"))
    somadaidade += idadedoaluno

mediadasidades = somadaidade / quantidadealunos

if mediadasidades > 0 and mediadasidades <= 25:
    print(f"\nA média das idades jovem. Média: {mediadasidades:0.1f}")
elif mediadasidades > 25 and mediadasidades <= 60:
    print(f"\nA média das idades adulta. Média: {mediadasidades:0.1f}")
elif mediadasidades > 60:
    print(f"\nA média das idades idosa. Média: {mediadasidades:0.1f}")
