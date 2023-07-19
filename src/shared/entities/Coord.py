class Coord:
    __x: int
    __y: int
    
    def __init__(self, x: int, y: int):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        
        self.__x = x
        self.__y = y
        
    def get_x(self) -> int:
        return self.__x

    def get_y(self) -> int:
        return self.__y
        
    def __eq__(self, other):
        if not isinstance(other, Coord):
            raise TypeError("Cannot compare Coord with " + str(type(other)))
        return self.__x == other.__x and self.__y == other.__y
    
    def __str__(self):
        return "(" + str(self.__x) + "," + str(self.__y) + ")"