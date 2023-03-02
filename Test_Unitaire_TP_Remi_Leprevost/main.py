from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


donnees = {
    'lieux': [
        'Paris',
        'Lyon',
        'Marseille',
        'Montpellier',
        'Toulon',
        'Lilles',
        'Nantes']
}

@app.get("/lieux")
async def get_lieux():
    return {'donnees': donnees}


@app.post("/lieux")
async def post_lieu(lieu: str):
    if lieu in donnees['lieux']:
        return {'donnees': donnees, 'message': "l'emplacement existe déjà"}
    
    else:
        donnees['lieux'].append(lieu)
        return {'donnees': donnees, 'message': "l'emplacement a été ajouté"}

    
@app.delete("/lieux")
async def delete_lieu(lieu: str):
    if lieu in donnees['lieux']:
        donnees['lieux'].remove(lieu)
        return {'data': donnees, 'message':'le lieu est supprimé'}
    
    else:
        return {'data': donnees, 'message': "le lieu n'existe pas"}