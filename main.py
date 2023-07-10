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
    num1: float =6
    num2: float =6

##########################################################################

app = FastAPI(description="API di prova per studiare FastAPI", title="Imparare API")

@app.get("/")
def hello():
    return {"<-----------      http://localhost:8000/docs     ---------->"}

##Test


if __name__ == '__main__':
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)