from app.tools.functionTools import *
from app.sprites.item.item import Item


class ItemFactory:
    def __init__(self):
        pass

    def create(self, item):
        iType = seekAtt(item, "type")
        if iType == "item" and hasattr(item, 'name'):
            return Item(item.x, item.y, item.name)

