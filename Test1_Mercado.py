
hall_dados = []
resp= ""
while(resp != "N"):
    try:
        valor_mes = int(input("Valor da ação:"))
        hall_dados.append(valor_mes)
        resp_p = input("Deseja adcionar mais um mês?(S/N): ").upper()
        resp =resp_p[0]
    except ValueError:
        print("\33[31m INSIRA UM NÚMERO \033[m")

