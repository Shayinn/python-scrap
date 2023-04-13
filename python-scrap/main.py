import re
from colorama import Fore
import requests

# Se deben ver los patrones de la gestion de carpetas de la web previamente

web_to_scrap = "https://vulnhub.com/"
result = requests.get(web_to_scrap)  # Para recoger el resultado de la pagina
content = result.text # Convierte el resultado a texto

#Colores a usar:
green = Fore.GREEN
red = Fore.RED

# Mediante expresiones regulares se comienza a scrapear, filtrando por titulos
# con la libreria r, encotramos los patrones para asi eliminar lo que no nos interesa

pattern = r"/entry/[\w-]*" #Todo lo que vaya despues de /entry/
repeated = re.findall(pattern, str(content)) # Aqui se observa que todo esta repetido por lo que debemos eliminarlo
no_dupplicated = list(set(repeated))

list_f = []

for i in no_dupplicated:
    name_f = i.replace("/entry/", "")
    list_f.append(name_f)
    print(name_f)

# Para ver si hay cambios en la pag web, creo un condicional

new_title = "noooob-1" #El texto a buscar
exist = False

for k in list_f:
    if k == new_title:
        exist = True
        break

if exist == True:
    print("\n" + green + "There is nothing new")
 
else:
    print("\n" + red + "New Update!")

