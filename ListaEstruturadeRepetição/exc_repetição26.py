"""Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato. """
quantidadeeleitores = int(input("Digite a quantidade de eleitores para a eleição:\n"))
somadevotoscandidato1 = 0
somadevotoscandidato2 = 0
somadevotoscandidato3 = 0

for eleitor in range(1, quantidadeeleitores + 1):
    voto = int(
        input(
            "Em quem deseja votar?\nCandidatos:\n1 - Dória\n2 - Bolsonaro\n3 - Ciro\n"
        )
    )
    if voto == 1:
        somadevotoscandidato1 += 1
    elif voto == 2:
        somadevotoscandidato2 += 1
    elif voto == 3:
        somadevotoscandidato3 += 1
    else:
        print("Não existe essa opção de voto")

print(
    f"Apuração dos votos:\nDória: {somadevotoscandidato1} votos\nBolsonaro: {somadevotoscandidato2} votos\nCiro: {somadevotoscandidato3} votos"
)
