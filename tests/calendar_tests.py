import unittest
from test_helpers import use_base_date

from season.calendar import calendar

@use_base_date("2025-05-10")
class CalendarTestCase(unittest.TestCase):
    def test_calendar_class_next_season(self):
        next_season = calendar().next_season()
        self.assertEqual(next_season, 22)

    def test_calendar_class_next_year(self):
        next_year = calendar().next_year()
        self.assertEqual(next_year, 236)

    def test_calendar_class_next_month(self):
        next_month = calendar().next_month()
        self.assertEqual(next_month, 22)

if __name__ == '__main__':
    unittest.main()