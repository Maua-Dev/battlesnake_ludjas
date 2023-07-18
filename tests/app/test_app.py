from src.app.main import create_item, read_item, info


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

    def test_get_item(self):

        resp = read_item(1)

        assert resp == {"item_id": 1}

    def test_post_item(self):
        request = {"item_id": 1,
                   "name": "test"}

        resp = create_item(request)

        assert resp == {"item_id": 1,
                        "name": "test"}
