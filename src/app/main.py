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

@app.post("/start") 
def start():
    return "ok"

@app.post("/move")
def move():
    return {
        "move": "up",
        "shout": "I'm moving up!"
    }

@app.post("/end")
def end():
    return "ok"


handler = Mangum(app, lifespan="off")
