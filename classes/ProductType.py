class ProductType:
    def __init__(self,
                 main_category: str,
                 sub_category: str):
        self.main_category = main_category
        self.sub_category = sub_category

    def get_category(self):
        return [self.main_category, self.sub_category]
