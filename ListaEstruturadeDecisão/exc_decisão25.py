''' Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".'''

def detector_de_criminoso():
    contagem = 0
    
    print('Analise de Criminoso: Responder sim ou não para as perguntas abaixo.\n')
    
    resposta1 = str(input('Telefonou para a vítima ?\n'))
    if resposta1 == 'sim':
        contagem = contagem + 1
    
    resposta2 = str(input('Esteve no local do crime ?\n'))
    if resposta2 == 'sim':
        contagem = contagem + 1

    resposta3 = str(input('Mora perto da vítima ?\n'))
    if resposta3 == 'sim':
        contagem = contagem + 1
    
    resposta4 = str(input('Devia para a vítima ?\n'))
    if resposta4 == 'sim':
        contagem = contagem + 1
    
    resposta5 = str(input('Já trabalhou com a vítima ?\n'))
    if resposta5 == 'sim':
        contagem = contagem + 1
    
    grau_criminalidade = {
        "0":'Inocente',
        "1":'Inocente',
        "2":'Suspeita',
        "3":'Cúmplice',
        "4":'Cúmplice',
        "5":'Assassino'
    }

    resultado = grau_criminalidade.get(str(contagem))
    
    return f'\nVocê é {resultado}'

if __name__ == '__main__':
    print(detector_de_criminoso())
