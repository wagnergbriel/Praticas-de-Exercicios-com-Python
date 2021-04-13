#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
from Exc_Decisão17 import ano_bissexto

def validar_data(data:str):
    # O dia, mês e ano serão separados por barra.
    dia, mes, ano = data.split('/')
    mes_com_31_dias = ['01', '03', '05', '07', '08', '10', '12']
    mes_com_30_dias = ['04', '06', '09', '11']
    data_valida = False

    if mes in mes_com_31_dias:
        if dia <= '31':
            data_valida = True
    
    elif mes in mes_com_30_dias:
        if dia <= '30':
            data_valida = True

    elif mes == '02'\
            and dia <= '28':
                data_valida = True
        
        if ano_bissexto(int(ano))\
            and dia <= '29':
                data_valida = True

    if data_valida:
        print(f'Esta data é valida: {data}')
    else:
        print(f'Esta data não é valida: {data}')

if __name__ == "__main__":
    validar_data('28/02/2021')