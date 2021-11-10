"""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes;
"""
ladoa = float(input("Digite o lado A do trinângulo:\n"))
ladob = float(input("Digite o lado B do trinângulo:\n"))
ladoc = float(input("Digite o lado C do trinângulo:\n"))

if ladoa == ladob and ladoa == ladoc:
    print(
        f"Os lados A:{ladoa}, B:{ladob}, C:{ladoc} são iguais. É um Triângulo Esquilátero."
    )

elif ladoa == ladob or ladoa == ladoc or ladob == ladoc:
    print(
        f"Os lados A:{ladoa}, B:{ladob}, C:{ladoc} apenas dois são iguais. É um Triângulo Isósceles."
    )

elif ladoa != ladob and ladoa != ladoc or ladob != ladoc and ladoc != ladoa and ladob:
    print(
        f"Os lados A:{ladoa}, B:{ladob}, C:{ladoc} todos os lados são diferentes. É um Triângulo Escaleno."
    )
