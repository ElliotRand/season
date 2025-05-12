from datetime import date
from datetime import datetime
from . import calendar

__all__ = ["Season", "is_spring", "is_summer", "is_autumn", "is_winter", "get_current_season", "calendar"]

season_months = {
    'spring': ['March', 'April', 'May'],
    'summer': ['June', 'July', 'August'],
    'autumn': ['September', 'October', 'November'],
    'winter': ['December', 'January', 'February'],
}

season_numbers = {
    'spring': 1,
    'summer': 2,
    'autumn': 3,
    'winter': 4,
}

month_numbers = {
    'January': 1,
    'February': 2,
    'March': 3,
    'April': 4,
    'May': 5,
    'June': 6,
    'July': 7,
    'August': 8,
    'September': 9,
    'October': 10,
    'November': 11,
    'December': 12,
}

day_numbers = {
    'Monday': 1,
    'Tuesday': 2,
    'Wednesday': 3,
    'Thursday': 4,
    'Friday': 5,
    'Saturday': 6,
    'Sunday': 7,
}

def get_current_season(month=date.today().strftime("%B"), as_number=False):
    for season, months in season_months.items():
        if month in months:
            return season_numbers[season] if as_number else season
        
def get_current_month(as_number=False):
    month = date.today().strftime("%B")
    return month_numbers[month] if as_number else month

def get_current_day(as_number=False):
    day = date.today().strftime("%A")
    return day_numbers[day] if as_number else day

def is_spring():
    return get_current_season() == 'spring'

def is_summer():
    return get_current_season() == 'summer'

def is_autumn():
    return get_current_season() == 'autumn'

def is_winter():
    return get_current_season() == 'winter'
        
class Season_(date):
    def __new__(cls, year, month, day):
        return super().__new__(cls, year, month, day)
    
    def __str__(self):
        return self.strftime("%S")
    
    @property
    def season(self):
        return get_current_season()
    
    @property
    def month(self):
        return get_current_month()
    
    @property
    def day(self):
        return get_current_day()
    
    def strftime(self, format):
        format = format.replace("%S", self.season)
        format = format.replace("%M", super().strftime("%B"))
        format = format.replace("%D", super().strftime("%A"))
        return super().strftime(format)
    
    def intftime(self, format: str):
        if len(format.split()) == 1:
            if format == "%s":
                return self.as_number()
            elif format == "%y":
                return self.year
            elif format == "%m":
                return get_current_month(as_number=True)
            elif format == "%d":
                return get_current_day(as_number=True)
            elif format == "%H":
                return datetime.now().hour
            elif format == "%M":
                return datetime.now().minute
            elif format == "%S":
                return datetime.now().second
            else:
                return 0
        else:
            format = format.replace("%s", str(self.as_number()))
            format = format.replace("%y", str(self.year))
            format = format.replace("%m", str(get_current_month(as_number=True)))
            format = format.replace("%d", str(get_current_day(as_number=True)))
            format = format.replace("%H", str(datetime.now().hour))
            format = format.replace("%M", str(datetime.now().minute))
            format = format.replace("%S", str(datetime.now().second))
            return format
    
    def as_number(self):
        return get_current_season(as_number=True)
        
def Season():
    today = date.today()
    return Season_(today.year, today.month, today.day)