class date(object):
    def show_date(self):
        return '01/11/1984'


class time(object):
    def show_time(self):
        return '11:00'


class date_time(date, time):
    def show_date_time(self):
        print(self.show_date(), self.show_time())


calendar = date_time()
calendar.show_date_time()
print(calendar.show_date())
print(calendar.show_time())
