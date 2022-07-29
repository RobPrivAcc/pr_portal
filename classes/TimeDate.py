from datetime import datetime, date
import calendar

"""
%a	Weekday, short version	                Wed
%A	Weekday, full version	                Wednesday
%w	Weekday as a number 0-6, 0 is Sunday	3
%d	Day of month 01-31	                    31
%b	Month name, short version	            Dec
%B	Month name, full version	            December
%m	Month as a number 01-12	                12
%y	Year, short version, without century	18
%Y	Year, full version	                    2018
%H	Hour 00-23	                            17
%I	Hour 00-12	                            05
%p	AM/PM	                                PM
%M	Minute 00-59	                        41
%S	Second 00-59	                        08
%f	Microsecond 000000-999999	            548513
%z	UTC offset	                            +0100
%Z	Timezone	                            CST
%j	Day number of year 001-366	            365
%U	Week number of year, Sunday as the first day of week, 00-53	52
%W	Week number of year, Monday as the first day of week, 00-53	52
%c	Local version of date and time	Mon Dec 31 17:41:00 2018
%x	Local version of date	12/31/18
%X	Local version of time	17:41:00
%%	A % character	%
"""

#todo add dates range
class TimeDate:
    def __init__(self):

        curr_date = date.today()

        date_list = list(map(lambda d: int(d), str(curr_date).split("-")))
        self.date_obj = datetime(date_list[0], date_list[1], date_list[2])

        self.current_year = self.date_obj.strftime("%Y")
        self.current_month = self.date_obj.strftime("%m")
        self.current_day = date_list[2]
        self.current_month_last_day = calendar.monthrange(self.date_obj.year, self.date_obj.month)[1]

    def get_current_date(self):
        return str(self.date_obj.strftime("%Y")) + "-" + str(self.date_obj.strftime("%m")) + "-" + str(
            self.date_obj.strftime("%d"))

    def get_month(self, month_name=False):
        if month_name:
            return str(self.date_obj.strftime("%B"))
        return str(self.date_obj.strftime("%m"))

    def get_months(self):
        months = []
        for i in range(1, 13):
            date_object = datetime.strptime(str(i), "%m")
            months.append(date_object.strftime("%B"))
        return months

    def get_years(self):
        return [self.current_year, int(self.current_year) - 1]

    def get_month_range(self):
        return [str(self.current_year) + "-" + str(self.current_month) + "-01",
                str(self.current_year) + "-" + str(self.current_month) + "-" + str(self.current_month_last_day)]

    """ get list of date ranges from 01 Jan till today 
    vs same date range last year"""

    def get_last_and_current_year(self, date_range: list = None):
        return [
            [str(int(self.current_year) - 1) + "-01-01",
             str(int(self.current_year) - 1) + "-" +
             str(self.current_month) + "-" +
             str(self.current_day)],
            [str(self.current_year) + "-01-01",
             str(self.current_year) + "-" +
             str(self.current_month) + "-" +
             str(self.current_day)]
        ]
