import os

os.system('cls')
hall_dados = []
resp= ""
Contador_Mes=0
while(resp != "N"):
    try:
        valor_mes = float(input("Valor da ação: "))
        hall_dados.append(valor_mes)
        resp_p = input("Deseja adcionar mais um mês?(S/N): ").upper()
        resp =resp_p[0]
        Contador_Mes+=1
    except ValueError:
        print("\33[31m INSIRA UM NÚMERO \033[m")
contadorMedia=0
y=0
os.system('cls')

for x in hall_dados:
    y =x+y
    contadorMedia +=1
    media= y/contadorMedia 

print(f'O valor de Media obtido foi de: {media}')

contadorMedia=0
y=0
# DESVIO MEDIO de cada valor presente na lista = VALOR - MEDIA     
for x in hall_dados:
    print(f"O devio do mês {contadorMedia+1} é: {abs(hall_dados[(contadorMedia)]-media)}")
    y =abs(hall_dados[(contadorMedia)]-media)+y
    contadorMedia+=1
print(f"O desvio absoluto foi de: {y/Contador_Mes}")
