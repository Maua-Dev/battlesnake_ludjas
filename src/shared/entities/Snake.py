from typing import List
from src.shared.entities.Coord import Coord

class Snake:
    __id: str
    __name: str
    __health: int
    __body: List[Coord]
    __head: Coord
    __length: int
    __shout: str
    __squad: str
    __latency: str

    def __init__(self, json: dict):
        if type(json) is not dict:
            raise TypeError("json must be a dict")

        self.__id = json["id"]
        self.__name = json["name"]
        self.__health = json["health"]
        self.__body = []
        self.__head = Coord(json["head"]["x"], json["head"]["y"])
        self.__length = json["length"]
        self.__shout = json["shout"]
        self.__squad = json["squad"]
        self.__latency = json["latency"]

        for coord in json["body"]:
            self.__body.append(Coord(coord["x"], coord["y"]))
            
    def get_id(self) -> str:
        return self.__id
    
    def get_name(self) -> str:
        return self.__name
    
    def get_health(self) -> int:
        return self.__health
    
    def get_body(self) -> List[Coord]:
        return self.__body
    
    def get_head(self) -> Coord:
        return self.__head
    
    def get_length(self) -> int:
        return self.__length
    
    def get_shout(self) -> str:
        return self.__shout
    
    def get_squad(self) -> str:
        return self.__squad
    
    def get_latency(self) -> str:
        return self.__latency