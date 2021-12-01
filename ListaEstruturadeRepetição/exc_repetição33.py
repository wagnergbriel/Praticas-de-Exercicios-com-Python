""" O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas,
e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas."""
lista_de_temperatura = []
soma_de_temperatura = 0

while True:
    temperatura = float(
        input("Digite a temeperatura:(Digite zero para informar o resultado)\n")
    )
    if temperatura > 0:
        lista_de_temperatura.append(temperatura)
        soma_de_temperatura += temperatura
    else:
        break
maior_temperatura = max(lista_de_temperatura)
menor_temperatura = min(lista_de_temperatura)
media_da_temeperatura = soma_de_temperatura / len(lista_de_temperatura)
print(
    f"Média das temperaturas: {media_da_temeperatura} C°\nMaior Temperatura: {maior_temperatura} C°\nMenor temeperatura: {menor_temperatura} C°"
)
