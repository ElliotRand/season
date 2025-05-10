from datetime import date
from calendar import Calendar

__all__ = ["calendar"]

season_months = {
    'spring': ['March', 'April', 'May'],
    'summer': ['June', 'July', 'August'],
    'autumn': ['September', 'October', 'November'],
    'winter': ['December', 'January', 'February'],
}

season_order = ['spring', 'summer', 'autumn', 'winter']

class Calendar_(Calendar):
    def next_season(self):
        today = date.today()
        month = today.strftime("%B")
        for season, months in season_months.items():
            if month in months:
                season = season
                break
        next_season = season_order[(season_order.index(season) + 1) % 4]
        first_month = season_months[next_season][0]
        next_season_date = date(today.year, today.month, 1)
        while next_season_date.strftime("%B") != first_month:
            next_season_date = next_season_date.replace(month=next_season_date.month % 12 + 1)
        return (next_season_date - today).days
    
    def next_year(self):
        today = date.today()
        next_year_date = date(today.year + 1, 1, 1)
        return (next_year_date - today).days
    
    def next_month(self):
        today = date.today()
        if today.month == 12:
            next_month_date = date(today.year + 1, 1, 1)
        else:
            next_month_date = date(today.year, today.month + 1, 1)
        return (next_month_date - today).days
    
def calendar():
    return Calendar_()