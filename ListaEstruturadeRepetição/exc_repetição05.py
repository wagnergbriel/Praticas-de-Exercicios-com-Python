'''
Altere o programa anterior permitindo ao usuário informar as populações e
as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
'''
ANOS = 0
while True:
    populacao_a = float(input('Informe a quantidade de habitantes:\n'))
    populacao_b = float(input('Informe outra quantidade de habitantes:\n'))
    taxa_a = float(input('Informe a taxa de habitantes por ano:\n'))
    taxa_b = float(input('Informe outra taxa de habitantes por ano:\n'))
    taxa_a = taxa_a / 100
    taxa_b = taxa_b / 100
    populacao_a  = populacao_a + (populacao_a * taxa_a)
    populacao_b = populacao_b + (populacao_b * taxa_b)
    ANOS += 1
    print(f'Para a polucação A ultrapasse a polulaçaõ B, vai durar {ANOS} anos\n')
    print(f'Polulação A: {populacao_a:0.0f}')
    print(f'Polulação B: {populacao_b:0.0f}')
