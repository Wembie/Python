#usando pydantic recibiendo 2 numeros por post y hacer operaciones basicas (usar codigos de respuesta diferentes 200,201,202,204), controlar los errores usando try

from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

class Numbers( BaseModel ):
    number1 : int
    number2 : int

class Response( BaseModel ):
    message : str
    status_code : int

@app.post( "/add" )
def add( number : Numbers ):
    try:
        return JSONResponse( content = f"La suma entre { number.number1 } y { number.number2 } es: { number.number1 + number.number2 }", status_code = status.HTTP_201_CREATED ) 
        
    except Exception as e:
        raise HTTPException( status_code = status.HTTP_400_BAD_REQUEST, detail = str( e ) )
    
@app.post( "/subtract", status_code = status.HTTP_202_ACCEPTED )
def subtract( number : Numbers ):
    try:
        return Response( message = f"La resta entre { number.number1 } y { number.number2 } es: { number.number1 - number.number2 }", status_code = status.HTTP_202_ACCEPTED )
    except Exception as e:
        raise HTTPException( status_code = status.HTTP_400_BAD_REQUEST, detail = str( e ) )
    
@app.post( "/multiply" )
def multiply( number : Numbers ):
    try:
        return {
            f"La multiplicación entre { number.number1 } y { number.number2 } es:" : number.number1 * number.number2, "status_code" : status.HTTP_202_ACCEPTED
        }
    except Exception as e:
        raise HTTPException( status_code = status.HTTP_400_BAD_REQUEST, detail = str( e ) )
    
@app.post( "/divide" )
def divide( number : Numbers ):
    try:
        try:
            return {
                f"La división entre { number.number1 } y { number.number2 } es:" : number.number1 / number.number2, "status_code" : status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
            }
        except ZeroDivisionError:
            raise HTTPException( status_code = status.HTTP_204_NO_CONTENT, detail = "Error: División por cero" )
    except Exception as e:
        raise HTTPException( status_code = status.HTTP_400_BAD_REQUEST, detail = str( e ) )