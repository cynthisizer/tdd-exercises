__author__ = 'cwu'

import unittest
from military_time_converter import MilitaryTimeConverter


class MilitaryTimeConverterTest(unittest.TestCase):

    militaryTimeConverter = MilitaryTimeConverter()

    def test_setup_hour_int(self):
        self.assertTrue(self.militaryTimeConverter.hour(10) == 10)

    def test_setup_hour_string(self):
        self.assertTrue(self.militaryTimeConverter.hour("10").__eq__(10))

    def test_setup_bad_value(self):
        self.assertTrue(self.militaryTimeConverter.hour("ABCD").__eq__("ABCD"))



#Keep this method to execute all your tests cases through the cmdLine
if __name__ == '__main__':
    unittest.main()
