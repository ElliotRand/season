import unittest
from test_helpers import use_base_date

from season.calendar import calendar, get_current_season_months

@use_base_date("2025-05-10")
class CalendarTestCase(unittest.TestCase):
    def test_calendar_class_next_season(self):
        next_season = calendar().days_until_next_season()
        self.assertEqual(next_season, 22)

    def test_calendar_class_next_year(self):
        next_year = calendar().days_until_next_year()
        self.assertEqual(next_year, 236)

    def test_calendar_class_next_month(self):
        next_month = calendar().days_until_next_month()
        self.assertEqual(next_month, 22)

    def test_calendar_class_remaining_seasons_this_year(self):
        remaining_seasons = calendar().remaining_seasons()
        self.assertEqual(remaining_seasons, 3)

    def test_calendar_class_remaining_months_this_season(self):
        remaining_months = calendar().remaining_months(False, True)
        self.assertEqual(remaining_months, 0)

    def test_calendar_class_remaining_months_this_year(self):
        remaining_months = calendar().remaining_months()
        self.assertEqual(remaining_months, 7)

    def test_calendar_class_remaining_days_this_season(self):
        remaining_days = calendar().remaining_days(False, False, True)
        self.assertEqual(remaining_days, 22)

    def test_calendar_class_remaining_days_this_year(self):
        remaining_days = calendar().remaining_days(False, True)
        self.assertEqual(remaining_days, 236)

    def test_calendar_class_remaining_days_this_month(self):
        remaining_days = calendar().remaining_days()
        self.assertEqual(remaining_days, 22)

    def test_get_current_season_months(self):
        months = get_current_season_months()
        self.assertListEqual(months, ['March', 'April', 'May'])

    def test_get_current_season_months_as_numbers(self):
        months = get_current_season_months(as_numbers=True)
        self.assertListEqual(months, [3, 4, 5])

if __name__ == '__main__':
    unittest.main()