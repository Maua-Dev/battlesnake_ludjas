import pytest
from src.shared.entities.Coord import Coord


class Test_Coord:
    def test_coord(self):
        x = 1
        y = 2
        coord = Coord(x, y)
        assert coord.get_x() == x
        assert coord.get_y() == y
    
    def test_coord_wrong_type_x(self):
        with pytest.raises(TypeError):
            coord = Coord("1", 2)
            
    def test_coord_wrong_type_y(self):
        with pytest.raises(TypeError):
            coord = Coord(1, "2")
            
    def test_coord_wrong_type_equal(self):
        coord = Coord(1, 2)
        with pytest.raises(TypeError):
            coord == "1,2"