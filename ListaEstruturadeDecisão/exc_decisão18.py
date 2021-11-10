"""Faça um Programa que peça uma data no formato dd/mm/aaaa
    e determine se a mesma é uma data válida."""
data = "28/02/2021"
dia, mes, ano = data.split("/")  # O dia, mês e ano serão separados por barra.

# Listas dos meses referentes a quantidade de dias
mes_com_31_dias = ["01", "03", "05", "07", "08", "10", "12"]
mes_com_30_dias = ["04", "06", "09", "11"]
data_valida = False

if mes in mes_com_31_dias:
    if dia <= "31":
        data_valida = True

elif mes in mes_com_30_dias:
    if dia <= "30":
        data_valida = True
    # No caso do mes de fevereiro, tem que verificar se o ano é bissexto ou não
    elif mes == "02" and dia <= "28":
        data_valida = True

    if (ano % 4 == 0 and ano % 100 != 0) and dia <= "29":
        data_valida = True

if data_valida:
    print(f"Esta data é valida: {data}")
else:
    print(f"Esta data não é valida: {data}")
