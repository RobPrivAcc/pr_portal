class Calculations:
    def __init__(self, lst: list):
        self.list_of_objects = lst

    def display_categories(self):
        categories = []
        for obj in self.list_of_objects:
            tmp_cat = vars(obj)['_category'].get_category()
            if tmp_cat not in categories:
                categories.append(tmp_cat)
        return categories

    # getting list of main type Names
    def get_types(self):
        types = []
        for typ, sub in self.display_categories():
            if typ not in types:
                types.append(typ)
        return types

    # getting list of main type Names
    def get_sub_types(self, main_type):
        sub_types = []
        for typ, sub in self.display_categories():
            if typ == main_type:
                if sub not in sub_types:
                    sub_types.append(sub)
        return sub_types

    def summarise_type(self):
        type_value = []

        for category in self.get_types():
            summary_past = 0
            summary_current = 0
            for product in self.list_of_objects:
                if category == product.get_type():
                    summary_past += product.get_year()[0]['value']
                    summary_current += product.get_year()[1]['value']
                    # return
            type_value.append(
                [category,
                 round(summary_past, 2),
                 round(summary_current, 2),
                 self._calculate_growth(summary_past, summary_current)])
        return type_value

    def summarise_sub_type(self, main_type):
        sub_type_value = []

        for sub_category in self.get_sub_types(main_type):
            summary_past = 0
            summary_current = 0
            for product in self.list_of_objects:
                if main_type == product.get_type() and sub_category == product.get_sub_type():
                    summary_past += product.get_year()[0]['value']
                    summary_current += product.get_year()[1]['value']
            sub_type_value.append(
                [sub_category,
                 round(summary_past, 2),
                 round(summary_current, 2),
                 self._calculate_growth(summary_past, summary_current)])
        return sub_type_value

    def summarise_products(self, main_type, sub_type):
        product_value = []

        summary_past = 0
        summary_current = 0

        for product in self.list_of_objects:
            if main_type == product.get_type() and sub_type == product.get_sub_type():
                summary_past = round(product.get_year()[0]['value'], 2)
                summary_current = round(product.get_year()[1]['value'], 2)
                product_value.append(
                    [product.get_name(),
                     summary_past,
                     summary_current,
                     self._calculate_growth(summary_past, summary_current)])
        return product_value


    def _calculate_growth(self, summary_past, summary_current):
        if summary_past != 0:
            return round(((summary_current - summary_past) / summary_past) * 100, 2)
        elif summary_current == summary_past:
            return 0
        elif (summary_current > summary_past) and summary_past == 0:
            return 100
        else:
            return -100
