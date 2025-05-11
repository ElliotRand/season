import unittest
from test_helpers import use_base_date

from season import Season, get_current_season, is_spring, is_summer, is_autumn, is_winter

@use_base_date("2025-05-10 14:34:02")
class SeasonTestCase(unittest.TestCase):
    def test_season_class_strftime(self):
        season = Season().strftime("%S")
        self.assertEqual(season, 'spring')

    def test_season_class_today_strftime(self):
        season = Season().today().strftime("%S")
        self.assertEqual(season, 'spring')

    def test_season_class_intftime(self):
        season = Season().intftime("%s")
        self.assertEqual(season, 1)

    def test_season_class_today_intftime(self):
        season = Season().today().intftime("%s")
        self.assertEqual(season, 1)

    def test_season_class_intftime_year(self):
        year = Season().intftime("%y")
        self.assertEqual(year, 2025)

    def test_season_class_intftime_month(self):
        month = Season().intftime("%m")
        self.assertEqual(month, 5)

    def test_season_class_intftime_day(self):
        day = Season().intftime("%d")
        self.assertEqual(day, 6)

    def test_season_class_variable(self):
        season = Season().season
        self.assertEqual(season, 'spring')

    def test_season_class_today_variable(self):
        season = Season().today().season
        self.assertEqual(season, 'spring')

    def test_season_class_as_number(self):
        season = Season().as_number()
        self.assertEqual(season, 1)

    def test_season_class_today_as_number(self):
        season = Season().today().as_number()
        self.assertEqual(season, 1)

    def test_season_class_str(self):
        season = str(Season())
        self.assertEqual(season, 'spring')

    def test_season_class_today_str(self):
        season = str(Season().today())
        self.assertEqual(season, 'spring')

    def test_season_class_month(self):
        month = Season().month
        self.assertEqual(month, 'May')

    def test_season_class_today_month(self):
        month = Season().today().month
        self.assertEqual(month, 'May')

    def test_season_class_day(self):
        day = Season().day
        self.assertEqual(day, 'Saturday')

    def test_season_class_today_month(self):
        day = Season().today().day
        self.assertEqual(day, 'Saturday')

    def test_season_class_strftime_month(self):
        month = Season().strftime("%M")
        self.assertEqual(month, 'May')

    def test_season_class_strftime_day(self):
        day = Season().strftime("%D")
        self.assertEqual(day, 'Saturday')

    def test_season_class_intftime_hour(self):
        hour = Season().intftime("%H")
        self.assertEqual(hour, 14)

    def test_season_class_intftime_minute(self):
        minute = Season().intftime("%M")
        self.assertEqual(minute, 34)

    def test_season_class_intftime_second(self):
        second = Season().intftime("%S")
        self.assertEqual(second, 2)

    def test_get_current_season(self):
        season = get_current_season()
        self.assertEqual(season, 'spring')

    def test_get_current_season_as_number(self):
        season = get_current_season(as_number=True)
        self.assertEqual(season, 1)

    def test_get_current_season_by_month(self):
        season = get_current_season(month='March')
        self.assertEqual(season, 'spring')

    def test_get_current_season_by_month_as_number(self):
        season = get_current_season(month='March', as_number=True)
        self.assertEqual(season, 1)

    def test_is_spring(self):
        self.assertTrue(is_spring())

    def test_is_summer(self):
        self.assertFalse(is_summer())

    def test_is_autumn(self):
        self.assertFalse(is_autumn())

    def test_is_winter(self):
        self.assertFalse(is_winter())

if __name__ == '__main__':
    unittest.main()