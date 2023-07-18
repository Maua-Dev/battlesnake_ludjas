from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

# GET / - info about the snake (https://docs.battlesnake.com/api/requests/info)
# POST /start - start the game (https://docs.battlesnake.com/api/requests/start)
# POST /move - move the snake (https://docs.battlesnake.com/api/requests/move)
# POST /end - end the game (https://docs.battlesnake.com/api/requests/end)


@app.get("/")
def info():
    return {
        "apiversion": "1",
        "author": "LuigiTrevisan",
        "color": "#8B0000",
        "head": "tiger-king",
        "tail": "hook",
        "version": "1.0.0"
    }


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


@app.post("/create_item")
def create_item(request: dict):
    item_id = request.get("item_id")
    name = request.get("name")

    return {"item_id": item_id,
            "name": name}


handler = Mangum(app, lifespan="off")
