# Librerias para el proyecto ---------------------------------------------------------------------------------------------

from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

# URL´s que voy a usar ---------------------------------------------------------------------------------------------------

url_usd = "https://www.dolarhoy.com/"
page_usd = requests.get(url_usd)
soup_usd = BeautifulSoup(page_usd.content, "html.parser")

url_eu = "https://dolarhoy.com/cotizacion-euro"
page_eu = requests.get(url_eu)
soup_eu = BeautifulSoup(page_eu.content, "html.parser")

url_re = "https://dolarhoy.com/cotizacion-real-brasileno"
page_re = requests.get(url_re)
soup_re = BeautifulSoup(page_re.content, "html.parser")

# Listas para guardar los valores y armar el DataFrame -------------------------------------------------------------------

valores = list()
divisas = list()

# Para los dolares -------------------------------------------------------------------------------------------------------

divisa_usd = soup_usd.find_all("a", class_="title")

count = 0 
for tag_usd in divisa_usd:
    if count < 3:
        divisas.append(tag_usd.text)
    else:
        break
    count += 1

del divisas[0]

val_usd = soup_usd.find_all("div", class_="val")

count = 0
for number_usd in val_usd:
    if count < 5:
        valores.append(number_usd.text)
    else:
        break
    count += 1

del valores[0]
del valores[0]
del valores[1]

dolarhoy = float(valores[0].replace("$", ""))

# Para el Euro -----------------------------------------------------------------------------------------------------------

divisa_eu = soup_eu.find_all("div", class_="tile is-child title")

count = 0 
for tag_eu in divisa_eu:
    if count < 3:
        divisas.append(tag_eu.text)
    else:
        break
    count += 1

val_eu = soup_eu.find_all("div", class_="value")

count = 0
for number_eu in val_eu:
    if count < 5:
        valores.append(number_eu.text)
    else:
        break
    count += 1

del valores[3]

# Para el Real -----------------------------------------------------------------------------------------------------------

divisa_re = soup_re.find_all("div", class_="tile is-child title")

count = 0
for tag_re in divisa_re:
    if count < 5:
        divisas.append(tag_re.text)
    else:
        break
    count += 1

val_re = soup_re.find_all("div", class_="value")

count = 0
for number_re in val_re:
    if count < 5:
        valores.append(number_re.text)
    else:
        break
    count += 1

del valores[4]

# Creo el frame de pandas para divisas existentes ------------------------------------------------------------------------

pd_df = pd.DataFrame({"Divisa" : divisas, "Valor" : valores})

# A partir de aca empieza el programa ------------------------------------------------------------------------------------
print()
print()
print("Hola! soy un conversor de divisas y estas son las divisas que puedo convertir:")
print()
print()
time.sleep(1.5)
print(pd_df)
print()
print()
time.sleep(1.5)
print("¿Qué operacion te gustaria hacer? \n \n 1) Convertir a Pesos \n 2) Convertir a moneda extranjera")
print()
choice = int(input())

if choice == 1:

    print()
    print("¿Qué divisa desea usar? \n \n 1) Dolar Blue \n 2) Dolar Oficial Promedio \n 3) Euro \n 4) Real")
    print()

    choice_div = int(input())

    if choice_div == 1:
        print()
        print("¿Cuantos dolares tenés?")
        print()
        have = int(input())
        print()
        conv_have = have * float(valores[0].replace("$", ""))
        print(f"Entonces tenes ${conv_have} pesos")
    elif choice_div == 2:
        print()
        print("¿Cuantos dolares tenés?")
        print()
        have = int(input())
        print()
        conv_have = have * float(valores[1].replace("$", ""))
        print(f"Entonces tenes ${conv_have} pesos")
    elif choice_div == 3:
        print()
        print("¿Cuantos euros tenés?")
        print()
        have = int(input())
        print()
        conv_have = have * float(valores[2].replace("$", ""))
        print(f"Entonces tenes ${conv_have} pesos")
    elif choice_div == 4:
        print()
        print("¿Cuantos reales tenés?")
        print()
        have = int(input())
        print()
        conv_have = have * float(valores[3].replace("$", ""))
        print(f"Entonces tenes ${conv_have} pesos")
    else:
        exit()

elif choice == 2:

    print()
    print("¿Qué divisa desea usar? \n \n 1) Dolar Blue \n 2) Dolar Oficial Promedio \n 3) Euro \n 4) Real")
    print()

    choice_div = int(input())

    if choice_div == 1:
        print()
        print("¿Cuantos pesos tenés?")
        print()
        have = int(input())
        print()
        conv_have = have / float(valores[0].replace("$", ""))
        print()
        print(f"Tenes $" + "{0:.2f}".format(conv_have) + " dolares")
    elif choice_div == 2:
        print()
        print("¿Cuantos pesos tenés?")
        print()
        have = int(input())
        print()
        conv_have = have / float(valores[1].replace("$", ""))
        print()
        print(f"Tenes $" + "{0:.2f}".format(conv_have) + " dolares")
    elif choice_div == 3:
        print()
        print("¿Cuantos pesos tenés?")
        print()
        have = int(input())
        print()
        conv_have = have / float(valores[2].replace("$", ""))
        print()
        print(f"Tenes $" + "{0:.2f}".format(conv_have) + " euros")
    elif choice_div == 4:
        print()
        print("¿Cuantos pesos tenés?")
        print()
        have = int(input())
        print()
        conv_have = have / float(valores[3].replace("$", ""))
        print()
        print(f"Tenes $" + "{0:.2f}".format(conv_have) + " reales")
    else:
        exit()        