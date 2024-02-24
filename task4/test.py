import unittest
import main


class TestChange(unittest.TestCase):

    def test1(self):
        self.assertEqual(main.convert(0), 'Ноль')

    def test2(self):
        self.assertEqual(main.convert(10), 'Десять')

    def test3(self):
        self.assertEqual(main.convert(100), 'Сто')

    def test4(self):
        self.assertEqual(main.convert(1000), 'Одна тысячa')

    def test5(self):
        self.assertEqual(main.convert(1_000_000), 'Один миллион')

    def test6(self):
        self.assertEqual(main.convert(12), 'Двенадцать')

    def test7(self):
        self.assertEqual(main.convert(143), 'Сто сорок три')

    def test8(self):
        self.assertEqual(main.convert(3245), 'Три тысячи двести сорок пять')

    def test9(self):
        self.assertEqual(main.convert(145_290), 'Сто сорок пять тысяч двести девяносто')

    def test10(self):
        self.assertEqual(main.convert(1_111_111), 'Один миллион сто одиннадцать тысяч сто одиннадцать')

    def test11(self):
        self.assertEqual(main.convert(999999), 'Девятьсот девяносто девять тысяч девятьсот девяносто девять')

