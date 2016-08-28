# -*- coding: utf-8 -*-

from pendulum import Pendulum
from pendulum.formatting.alternative_formatter import AlternativeFormatter
from .. import AbstractTestCase


class ClassicFormatterTest(AbstractTestCase):

    def test_year_tokens(self):
        d = Pendulum(2009, 1, 14, 15, 25, 50, 123456)
        f = AlternativeFormatter()
        self.assertEqual('2009', f.format(d, 'YYYY'))
        self.assertEqual('09', f.format(d, 'YY'))
        self.assertEqual('2009', f.format(d, 'Y'))

    def test_quarter_tokens(self):
        f = AlternativeFormatter()
        d = Pendulum(1985, 1, 4)
        self.assertEqual('1', f.format(d, 'Q'))
        d = Pendulum(2029, 8, 1)
        self.assertEqual('3', f.format(d, 'Q'))
        d = Pendulum(1985, 1, 4)
        self.assertEqual('1st', f.format(d, 'Qo'))
        d = Pendulum(2029, 8, 1)
        self.assertEqual('3rd', f.format(d, 'Qo'))
        d = Pendulum(1985, 1, 4)
        self.assertEqual('1er', f.format(d, 'Qo', locale='fr'))
        d = Pendulum(2029, 8, 1)
        self.assertEqual('3e', f.format(d, 'Qo', locale='fr'))

    def test_month_tokens(self):
        f = AlternativeFormatter()
        d = Pendulum(2016, 3, 24)
        self.assertEqual('03', f.format(d, 'MM'))
        self.assertEqual('3', f.format(d, 'M'))

        self.assertEqual('Mar', f.format(d, 'MMM'))
        self.assertEqual('March', f.format(d, 'MMMM'))
        self.assertEqual('3rd', f.format(d, 'Mo'))

        self.assertEqual('mars', f.format(d, 'MMM', locale='fr'))
        self.assertEqual('mars', f.format(d, 'MMMM', locale='fr'))
        self.assertEqual('3e', f.format(d, 'Mo', locale='fr'))

    def test_day_tokens(self):
        f = AlternativeFormatter()
        d = Pendulum(2016, 3, 7)
        self.assertEqual('07', f.format(d, 'DD'))
        self.assertEqual('7', f.format(d, 'D'))

        self.assertEqual('7th', f.format(d, 'Do'))
        self.assertEqual('1st', f.format(d.first_of('month'), 'Do'))

        self.assertEqual('7e', f.format(d, 'Do', locale='fr'))
        self.assertEqual('1er', f.format(d.first_of('month'), 'Do', locale='fr'))

    def test_day_of_year(self):
        f = AlternativeFormatter()
        d = Pendulum(2016, 8, 28)
        self.assertEqual('241', f.format(d, 'DDDD'))
        self.assertEqual('241', f.format(d, 'DDD'))
        self.assertEqual('001', f.format(d.start_of('year'), 'DDDD'))
        self.assertEqual('1', f.format(d.start_of('year'), 'DDD'))

        self.assertEqual('241st', f.format(d, 'DDDo'))
        self.assertEqual('244th', f.format(d.add(days=3), 'DDDo'))

        self.assertEqual('241e', f.format(d, 'DDDo', locale='fr'))
        self.assertEqual('244e', f.format(d.add(days=3), 'DDDo', locale='fr'))

    def test_day_of_week(self):
        f = AlternativeFormatter()
        d = Pendulum(2016, 8, 28)
        self.assertEqual('0', f.format(d, 'd'))

        self.assertEqual('Sun', f.format(d, 'dd'))
        self.assertEqual('Sun', f.format(d, 'ddd'))
        self.assertEqual('Sunday', f.format(d, 'dddd'))

        self.assertEqual('dim', f.format(d, 'dd', locale='fr'))
        self.assertEqual('dim', f.format(d, 'ddd', locale='fr'))
        self.assertEqual('dimanche', f.format(d, 'dddd', locale='fr'))

    def test_am_pm(self):
        f = AlternativeFormatter()
        d = Pendulum(2016, 8, 28, 23)
        self.assertEqual('PM', f.format(d, 'A'))
        self.assertEqual('AM', f.format(d.hour_(11), 'A'))

    def test_hour(self):
        f = AlternativeFormatter()
        d = Pendulum(2016, 8, 28, 7)
        self.assertEqual('7', f.format(d, 'H'))
        self.assertEqual('07', f.format(d, 'HH'))

        d = Pendulum(2016, 8, 28, 0)
        self.assertEqual('12', f.format(d, 'h'))
        self.assertEqual('12', f.format(d, 'hh'))

    def test_minute(self):
        f = AlternativeFormatter()
        d = Pendulum(2016, 8, 28, 7, 3)
        self.assertEqual('3', f.format(d, 'm'))
        self.assertEqual('03', f.format(d, 'mm'))

    def test_second(self):
        f = AlternativeFormatter()
        d = Pendulum(2016, 8, 28, 7, 3, 6)
        self.assertEqual('6', f.format(d, 's'))
        self.assertEqual('06', f.format(d, 'ss'))

    def test_fractional_second(self):
        f = AlternativeFormatter()
        d = Pendulum(2016, 8, 28, 7, 3, 6, 123456)
        self.assertEqual('1', f.format(d, 'S'))
        self.assertEqual('12', f.format(d, 'SS'))
        self.assertEqual('123', f.format(d, 'SSS'))
        self.assertEqual('1234', f.format(d, 'SSSS'))
        self.assertEqual('12345', f.format(d, 'SSSSS'))
        self.assertEqual('123456', f.format(d, 'SSSSSS'))

    def test_timezone(self):
        f = AlternativeFormatter()
        d = Pendulum(2016, 8, 28, 7, 3, 6, 123456, 'Europe/Paris')
        self.assertEqual('CEST', f.format(d, 'z'))
        self.assertEqual('Europe/Paris', f.format(d, 'zz'))

        d = Pendulum(2016, 1, 28, 7, 3, 6, 123456, 'Europe/Paris')
        self.assertEqual('CET', f.format(d, 'z'))
        self.assertEqual('Europe/Paris', f.format(d, 'zz'))

    def test_timezone_offset(self):
        f = AlternativeFormatter()
        d = Pendulum(2016, 8, 28, 7, 3, 6, 123456, 'Europe/Paris')
        self.assertEqual('+0200', f.format(d, 'Z'))
        self.assertEqual('+02:00', f.format(d, 'ZZ'))

        d = Pendulum(2016, 1, 28, 7, 3, 6, 123456, 'Europe/Paris')
        self.assertEqual('+0100', f.format(d, 'Z'))
        self.assertEqual('+01:00', f.format(d, 'ZZ'))

    def test_timestamp(self):
        f = AlternativeFormatter()
        d = Pendulum(1970, 1, 1)
        self.assertEqual('0', f.format(d, 'X'))
        self.assertEqual('86400', f.format(d.add(days=1), 'X'))

    def test_escape(self):
        f = AlternativeFormatter()
        d = Pendulum(2016, 8, 28)
        self.assertEqual('YYYY 2016 [2016]', f.format(d, '[YYYY] YYYY \[YYYY\]'))
        self.assertEqual('D 28 \\28', f.format(d, '\D D \\\D'))
