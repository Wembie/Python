from pydantic import BaseModel

class Battle( BaseModel ):
    pokemon_name_1 : str
    pokemon_name_2 : str

class Battle_Result( BaseModel ):
    registro_existente : bool
    ganador_nombre : str
    perdedor_nombre : str
    iniciador_nombre : str