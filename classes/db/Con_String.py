import json
import os


class ConString:

    def __init__(self, config_path=str()):
        self.config_path = os.path.join(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'config.json'))

        if config_path:
            self.config_path = config_path

        with open(self.config_path) as f:
            json_string = json.load(f)
            self._cred = json_string[0]
            self._con_string = []
            for i in json_string[1]:
                self._con_string.append({**self._cred, **i})
        self.shop_number = len(self._con_string)

    def get_string(self, number: int = None):
        number = int(number)
        if number:
            number = number - 1
            if number < self.shop_number:
                return self._con_string[int(number)]
            else:
                print(f"The number must be lower than {self.shop_number}")
        else:
            return self._con_string

    def skip_shop(self, number):
        if number:
            self._con_string.pop(number)
            return self._con_string

    def get_shop_name(self, shop_no : int = None):
        if not shop_no:
            shops_list = []

            for shop in self._con_string:
                shops_list.append([shop['postcode'], shop['shopName']])
            return shops_list
        else:
            return [[self._con_string[shop_no - 1]['postcode'],
                    self._con_string[shop_no - 1]['shopName']]]