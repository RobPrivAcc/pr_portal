from classes.ProductType import ProductType


class Product:
    def __init__(self):
        self._name = None
        self._retail = 0.0
        self._cost = 0.0
        self._category = ProductType

    def set_name(self, name: str):
        self._name = name

    def set_categories(self, main, sub=""):
        self._category = ProductType(main, sub)

    def get_categories(self):
        return {'main': self._category.get_category()[0],
                'sub': self._category.get_category()[1]}

    def get_type(self):
        return self._category.get_category()[0]

    def get_sub_type(self):
        return self._category.get_category()[1]

    def get_product(self, asDictionary=False):
        return [self.get_categories()['main'],
                self.get_categories()['sub'],
                self._name]

    def get_name(self):
        return self._name
