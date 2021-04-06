# # test_cities.py

# import unittest
# from city_function import get_location_info

# class LocationTestCase(unittest.TestCase):
#     """Test for 'city_function.py'."""
    
#     def test_location_info(self):
#         """Do location names like 'Santiago, Chile' work?"""
#         location_info = get_location_info('santiago', 'chile')
#         self.assertEqual(location_info, "Santiago Chile")
        
# if __name__ == '__main__':
#     unittest.main()



# test_cities.py (updated)
# unit test for updated city_function with three parameter is added

import unittest
from city_function import get_location_info

class LocationTestCase(unittest.TestCase):
    """Test for 'city_function.py'."""
    
    def test_location_info(self):
        """Do location names like 'Santiago, Chile' work?"""
        location_info = get_location_info('santiago', 'chile')
        self.assertEqual(location_info, "Santiago, Chile")
        
    def test_location_population_info(self):
        """Do location and population info like 'Santiago, Chile - population 5000000' work?"""
        location_population_info = get_location_info('santiago', 'chile', 5000000)
        self.assertEqual(location_population_info, 'Santiago, Chile - population 5000000')
        
if __name__ == '__main__':
    unittest.main()