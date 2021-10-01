'''
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,...
Faça um programa capaz de gerar a série até o n−ésimo termo
'''
proximo = 0
anterior = 0
while(proximo < 60):
    print(proximo)
    proximo += anterior
    anterior = proximo - anterior

    if(proximo == 0):
        proximo += 1