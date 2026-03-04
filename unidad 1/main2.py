from fastapi import FastAPI

app = FastAPI()  
#genera el primer endpoint con un get
#@funcion decoradora, recibe otra funcion
@app.get("/")    

def prueba():
    return {"Hola":"dani"}  

#parametros de ruta 
@app.get("/path/{id}")

def path_wraper(id:int):
    return{"usuario": id}

@app.get("/multiples/path/{id}/{nombre}/{edad}")

def multiples_path_wraper(id:int, nombre: str, edad:int):
    return {"usuario":id,"nombre":nombre,"edad":edad}