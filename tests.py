import unittest

from converters import *

class TestConverters(unittest.TestCase):
    ''' A Test Case for our converter library

    '''
    def test_days_to_seconds(self):
        self.assertEqual(432000, days_to_seconds(5))
    
    def test_celsius_to_fahrenheit(self):
        self.assertEqual(32, celsius_to_fahrenheit(0))
        self.assertEqual(104, celsius_to_fahrenheit(40))
        self.assertEqual(102.2, celsius_to_fahrenheit(39))
    
    def test_fahrenheit_to_celsius(self):
        self.assertEqual(0, fahrenheit_to_celsius(32))
        self.assertEqual(40, fahrenheit_to_celsius(104))
        self.assertEqual(39, fahrenheit_to_celsius(102.2))
        
    def test_surface_of_circle(self):
        self.assertAlmostEqual(28.274, surface_of_circle(3), places=3)

    def test_cube_volume(self):
        self.assertEqual(120, cube_volume(4, 5, 6))
    
    def test_usd_to_chf(self):
        self.assertAlmostEqual(0.917, usd_to_chf(1), places=1)

    def test_mwst(self):
        self.assertAlmostEqual(39.42-36.50, mwst(39.42), places=2)

    def test_joules_to_calories(self):
        self.assertAlmostEqual(0.239, joules_to_calories(1), places=3)

    def test_kmh_to_mph(self):
        self.assertAlmostEqual(62.137, kmh_to_mph(100), places=2)

    def test_distance_between_points(self):
        from math import sqrt
        self.assertAlmostEqual(sqrt(18), distance_between_points((1,2), (4,5)), places=1)

    def test_cat_and_dog_speech(self):
        self.assertEquals('miau', cat_and_dog_speech('katze'))
        self.assertEquals('wuff', cat_and_dog_speech('hund'))

    def test_element_in_list(self):
        self.assertTrue(element_in_list('purple', ['blue', 'purple', 'pink']))
        self.assertFalse(element_in_list('yellow', ['blue', 'purple', 'pink']))

if __name__ == '__main__':
    unittest.main()
