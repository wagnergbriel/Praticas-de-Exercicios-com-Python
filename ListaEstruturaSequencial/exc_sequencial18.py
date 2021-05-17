'''
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''
def tempo_do_download(tamanhoarquivo, velocidadelink):
    #Calculando o tempo do download
    tempo  = tamanhoarquivo/velocidadelink #tempo em segundo
    tempoemminuto = tempo/60 #tempo em minuto 
    print(f'O download vai durar {tempoemminuto:0.2f} minutos.')

if __name__ == "__main__":
    tamanhoarquivo = float(input('Digite o tamanho do arquivo em MB:\n'))
    velocidadelink = float(input('Digite a velocidade da internet em Mbps:\n'))
    tempo_do_download(tamanhoarquivo, velocidadelink)