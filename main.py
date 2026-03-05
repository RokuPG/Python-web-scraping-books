import scraper
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensaje": "¡Mi primera API funcionando!"}

@app.get("/libros")
def obtener_libros():
    datos_reales = scraper.traer_datos()
    return datos_reales