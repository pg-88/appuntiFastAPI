from fastapi import FastAPI, Depends, Request
import uvicorn
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

#####################DATI#################################################

class Numbers(BaseModel):
    num1: float =6
    num2: float =6

##########################################################################

app = FastAPI(description="API di prova per studiare approfondire Jinja", title="Test Jinja")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def hello():
    return "<-----------      http://localhost:8000/docs     ---------->"

@app.get("/sum")
def sum_numbers(numbers: Numbers= Depends()):
    sum = int(numbers.num1 + numbers.num2)
    return sum

@app.post("/sum")
async def sum_numbers(numbers: Numbers):
    try:
        res = numbers.num1 + numbers.num2
        return res
    except:
        return {'result': 'errore' }





if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)