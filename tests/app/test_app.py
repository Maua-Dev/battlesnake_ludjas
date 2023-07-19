from src.app.main import info, start, move, end

class Test_App:
    def test_info(self):
        resp = info()

        assert resp == {
            "apiversion": "1",
            "author": "LuigiTrevisan",
            "color": "#8B0000",
            "head": "tiger-king",
            "tail": "hook",
            "version": "1.0.0"
        }