from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

#http://127.0.0.1:8000 

class Pokemon( BaseModel ):
    nombre : str
    hp : int
    speed: int
    attack : int
    defense : int
    ultimate : Optional[ str ]

@app.get( "/" )
def index():
    return { "message" : "Hola Wembie" }

@app.get( "/pokemons/{id}" )
def mostrarPokemon( id : int ):
    return { "data" : id }

@app.post( "/pokemons" )
def insertarPokemon( pokemon : Pokemon ):
    return { "message" : f"El pokemon { pokemon.nombre } ha sido insertado" }
