import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class CoordIn(BaseModel):
    password : str
    lat : float
    lon : float
    zoom : Optional[int] = None
    description : Optional[int] = None

class CoordOut(BaseModel):
    lat : float
    lon : float
    zoom : Optional[int] = None
    description : Optional[int] = None

#get
@app.get('/')
async def hello_world():
    return {"hello":"world"}

#single parameter
@app.get('/component/{component_id}')
async def get_component(component_id: int):
    return {"component" : component_id}

#multiple parameter
@app.get('/component/')
async def get_param(param1: int, param2: Optional[str]):
    #http://127.0.0.1:8000/component/?param1=21&param2=abc
    return {"param1" : param1, "param2" :param2}

#post simple BaseModel obeject
@app.get('/position/{priority}', response_model=CoordIn, response_model_include={'description'})#response_model_exclude={'description'})
async def make_position(priority: int, coord: Coord):
    #return {"priority" : priority, "new_coord" : coord.dict()}
    return coord

    
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    print('there')
