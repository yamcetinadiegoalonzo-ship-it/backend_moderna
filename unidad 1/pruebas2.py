import requests 
#recibe lo que el servidor le responda
respuesta = requests.get("http://127.0.0.1:8000")

print(respuesta) 
print(respuesta.raw)#nos devuelve en que direccion de memeria esta 
print(respuesta.text) #es la cadena String pero en texto plano
print(respuesta.json()) #devuelve el diccionario 

diccionario=respuesta.json()
print(diccionario["Hola"])

def peticion_path_id():
    respuesta =requests.get("http://127.0.0.1:8000/path/1")
    print(respuesta.json())

peticion_path_id()
def peticionMultiple(y, x,a):
    respuesta=requests.get("http://127.0.0.1:8000/multiples/path/99/diego/21")
    print(respuesta.json())

peticionMultiple(9,"diego",21)

