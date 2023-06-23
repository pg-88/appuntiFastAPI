from fastapi import FastAPI, Depends
import uvicorn
from pydantic import BaseModel

#####################DATI#################################################


class Computer(BaseModel):
    cpu: str
    freq: int


asus = {
    "cpu" : 'ryzen7',
    "freq": 2500000
}

my_pc = Computer(**asus)

class Numbers(BaseModel):
    num1: int =6
    num2: int =6

##########################################################################

app = FastAPI()

@app.get("/")
def hello():
    return "http://localhost:8000/docs"

@app.get("/pc")
def computer(pc: Computer= asus):
    return{pc.cpu: pc.freq}

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
        return {'error': 'something went wrong'}
# @app.get("/inventory")
# def inventory():
#     return inventory



if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)