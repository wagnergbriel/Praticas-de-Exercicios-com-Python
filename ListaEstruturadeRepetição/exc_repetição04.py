'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de
crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva o número de anos necessários para que a população do país
A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
'''
ANOS = 0
POPULACAO_A = 80000
POPULACAO_B = 200000
while POPULACAO_A < POPULACAO_B:
    POPULACAO_A  = POPULACAO_A + (POPULACAO_A * 0.03)
    POPULACAO_B = POPULACAO_B + (POPULACAO_B * 0.015)
    ANOS += 1
print(f'Para a polucação A ultrapasse a polulaçaõ B, vai durar {ANOS} anos\n')
print(f'Polulação A: {POPULACAO_A:0.0f}')
print(f'Polulação B: {POPULACAO_B:0.0f}')
