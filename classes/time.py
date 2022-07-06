from datetime import datetime, timedelta


class Time:

    def __init__(self):
        self._now = datetime.now()
        self._year = self._now.year
        self._last_year = self._year - 1
        self._month = self._now.month
        self._months = [*range(1, self._month + 1, 1)]

    def get_years(self):
        return [self._year, self._last_year]

    def get_months(self, year: int = 0):
        # if not year:
        #     year = self._year
        # if year != self._year:
        self._months = [*range(1, 13, 1)]

        months_list = []
        for month in self._months:
            months_list.append([month, datetime.strptime(str(month), "%m").strftime("%B")])
        return months_list

    @staticmethod
    def month_range(month: int, year: int):
        form_date = datetime.strptime(str(year) + "-" + str(month) + "-01", "%Y-%m-%d").strftime("%Y-%m-%d")
        if month == 12:
            to_date = datetime.strptime(str(year) + "-" + str(month) + "-31", "%Y-%m-%d").strftime("%Y-%m-%d")
        else:
            to_date = (datetime.strptime(str(year) + "-" + str(month + 1) + "-01", "%Y-%m-%d") - timedelta(days=1)) \
                .strftime("%Y-%m-%d")
        return [form_date, to_date]
