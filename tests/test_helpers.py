from freezegun import freeze_time

def use_base_date(date: str):
    return freeze_time(date)