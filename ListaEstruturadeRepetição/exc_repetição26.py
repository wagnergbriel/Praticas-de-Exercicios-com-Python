"""Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato. """
quantidade_de_eleitores = int(
    input("Digite a quantidade de eleitores para a eleição:\n")
)
soma_de_votos_candidato1 = 0
soma_de_votos_candidato2 = 0
soma_de_votos_candidato3 = 0

for eleitor in range(1, quantidade_de_eleitores + 1):
    voto = int(
        input(
            "Em quem deseja votar?\nCandidatos:\n1 - Dória\n2 - Bolsonaro\n3 - Ciro\n"
        )
    )
    if voto == 1:
        soma_de_votos_candidato1 += 1
    elif voto == 2:
        soma_de_votos_candidato2 += 1
    elif voto == 3:
        soma_de_votos_candidato3 += 1
    else:
        print("Não existe essa opção de voto")

print(
    f"Apuração dos votos:\nDória: {soma_de_votos_candidato1} votos\nBolsonaro: {soma_de_votos_candidato2} votos\nCiro: {soma_de_votos_candidato3} votos"
)
