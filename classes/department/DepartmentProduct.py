from classes.product import Product


class DepartmentProduct(Product):
    def __init__(self):
        self.year = []

    def add_year(self, year, value=0.0):
        self.year.append({'year': year,
                          'value': float(value)}
                         )

    def get_year(self):
        return self.year

    def get_product(self):
        p = Product.get_product(self)
        if len(self.get_year()) > 0:
            for year in self.get_year():
                p.append(year['value'])
        return p