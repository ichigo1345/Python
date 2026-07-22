from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"menssage: hola zeidler"}
@app.get("/celulares")
async def obtenerCelulares():
    return [
        {"id": 1, "marca": "Apple", "Modelo": "Iphone 17 pro max"},
        {"id": 2, "marca": "Samsung", "Modelo": "Samsung Galaxy S25 Ultra"},
        {"id": 3, "marca": "Motorola", "Modelo": "Motorola Edge 50"},
    ]
@app.get("/servants")
async def obtenerservants():
    return [
        {"id": 1, "Clase": "Saber", "Nombre verdadero": "Ricardo Corazon de leon"},
        {"id": 2, "Clase": "Archer", "Nombre verdadero": "Alcides"},
        {"id": 3, "Clase": "Lancer", "Nombre verdadero": "Enkidu"},
        {"id": 4, "Clase": "Rider", "Nombre verdadero": "Pale Rider"},
        {"id": 5, "Clase": "Assasin", "Nombre verdadero": "Shiki Ryougi"},
        {"id": 6, "Clase": "Berserker", "Nombre verdadero": "Lancelot"},
        {"id": 7, "Clase": "Caster", "Nombre verdadero": "Medea"},
        {"id": 8, "Clase": "Ruler", "Nombre verdadero": "Jeanne D'Arc"},

    ]