class Order:

    def __init__(self, order_details: list):
        self.order_number = order_details[9]
        self.ordered_date = order_details[1]
        self.book_in_date = order_details[0]
        self.invoice_ref = order_details[5]
        self.created_by = order_details[6]
        self.supplier = order_details[4]
        self.total_checked_value = round(order_details[7], 2)
        self.expenses = round(order_details[8], 2)

    def get_order_date(self):
        return self.ordered_date.strftime("%Y-%m-%d")

    def get_book_in_date(self):
        return self.book_in_date.strftime("%Y-%m-%d %H:%M:%S")

    def display(self):
        return [str(self.order_number),
                self.get_order_date(),
                self.get_book_in_date(),
                str(self.invoice_ref),
                str(self.created_by),
                str(self.supplier),
                str(self.total_checked_value),
                str(self.expenses)]
