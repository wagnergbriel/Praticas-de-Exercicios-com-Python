"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, 
dezenas e unidades do mesmo.

Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 
326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""
numero = 4555

if numero > 0 and numero <= 9:
    print(f"{numero} = {numero} Unidade(s).")

elif numero >= 10 and numero <= 99:
    parse_numero = list(str(numero))
    dezena = parse_numero[0]
    unidade = parse_numero[1]
    print(f"{numero} = {dezena} Dezena(s) e {unidade} Unidade(s).")

elif numero >= 100 and numero <= 999:
    parse_numero = list(str(numero))
    centena = parse_numero[0]
    dezena = parse_numero[1]
    unidade = parse_numero[2]
    print(
        f"{numero} = {centena} Centena(s), {dezena} Dezena(s) e {unidade} Unidade(s)."
    )
else:
    print("O número tem mais de 3 algarismos.")
