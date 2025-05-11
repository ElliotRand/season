from datetime import date
from datetime import datetime
from calendar import Calendar

__all__ = ["calendar"]

season_months = {
    'spring': ['March', 'April', 'May'],
    'summer': ['June', 'July', 'August'],
    'autumn': ['September', 'October', 'November'],
    'winter': ['December', 'January', 'February'],
}

season_order = ['spring', 'summer', 'autumn', 'winter']

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

def get_current_season_months(as_numbers=False):
    today = date.today()
    month = today.strftime("%B")
    for season, months in season_months.items():
        if month in months:
            if as_numbers:
                return [month_numbers[m] for m in months]
            return months
    return []

class Calendar_(Calendar):
    def days_until_next_season(self):
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
    
    def days_until_next_year(self):
        today = date.today()
        next_year_date = date(today.year + 1, 1, 1)
        return (next_year_date - today).days
    
    def days_until_next_month(self):
        today = date.today()
        if today.month == 12:
            next_month_date = date(today.year + 1, 1, 1)
        else:
            next_month_date = date(today.year, today.month + 1, 1)
        return (next_month_date - today).days
    
    def remaining_seasons(self, this_year=True):
        today = date.today()
        month = today.strftime("%B")
        for season, months in season_months.items():
            if month in months:
                season = season
                break
        index = season_order.index(season)
        seasons = season_order[index + 1:] if this_year else []
        return len(seasons)
    
    def remaining_months(self, this_year=True, this_season=False):
        today = date.today()
        month = today.strftime("%B")
        if this_season:
            for season, months in season_months.items():
                if month in months:
                    season_months_ = months
                    break
            index = season_months_.index(month)
            return len(season_months_[index + 1:])
        if this_year:
            months = [
                'January',
                'February',
                'March',
                'April',
                'May',
                'June',
                'July',
                'August',
                'September',
                'October',
                'November',
                'December',
            ]
            index = months.index(month)
            return len(months[index + 1:])
        return []

    def remaining_days(self, this_month=True, this_year=False, this_season=False):
        today = date.today()
        if this_month:
            if today.month == 12:
                next_month = date(today.year + 1, 1, 1)
            else:
                next_month = date(today.year, today.month + 1, 1)
            return (next_month - today).days
        if this_year:
            next_year = date(today.year + 1, 1, 1)
            return (next_year - today).days
        if this_season:
            current_month = today.strftime("%B")
            for season, months in season_months.items():
                if current_month in months:
                    current_season = season
                    current_season_months = months
                    break
            season_end_month = current_season_months[-1]
            season_end_month_num = datetime.strptime(season_end_month, "%B").month
            if season_end_month_num < today.month:
                season_end_date = date(today.year + 1, season_end_month_num + 1, 1)
            else:
                season_end_date = date(today.year, season_end_month_num + 1, 1)
            return (season_end_date - today).days
        return 0
    
def calendar():
    return Calendar_()