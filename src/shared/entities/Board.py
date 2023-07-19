from typing import List
from src.shared.entities.Coord import Coord
from src.shared.entities.Snake import Snake

class Board:
    __height: int
    __width: int
    __food: List[Coord]
    __hazards: List[Coord]
    __snakes: List[Snake]
    
    def __init__(self, json: dict):
        if type(json) is not dict:
            raise TypeError("json must be a dict")
        
        self.__height = json["height"]
        self.__width = json["width"]
        self.__food = []
        self.__hazards = []
        self.__snakes = []
        
        for food in json["food"]:
            self.__food.append(Coord(food["x"], food["y"]))
        
        for hazard in json["hazards"]:
            self.__hazards.append(Coord(hazard["x"], hazard["y"]))
        
        for snake in json["snakes"]:
            self.__snakes.append(Snake(snake))
            
    def get_height(self) -> int:
        return self.__height
    
    def get_width(self) -> int:
        return self.__width
    
    def get_food(self) -> List[Coord]:
        return self.__food
    
    def get_hazards(self) -> List[Coord]:
        return self.__hazards
    
    def get_snakes(self) -> List[Snake]:
        return self.__snakes