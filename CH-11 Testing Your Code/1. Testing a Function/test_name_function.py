# test_name_function.py

# A test case with one method that verifies that the function
# get_formatted_name() works correctly when given a first and last name

# import unittest
# from name_function import get_formatted_name

# class NamesTestCase(unittest.TestCase):
#     """Tests for 'name_function.py'."""
    
#     def test_first_last_name(self):
#         """Do names like 'Aninpro Drones' work?""" 
#         formatted_name = get_formatted_name('aninpro', 'drones')
#         self.assertEqual(formatted_name, 'Aninpro Drones')
        
# if __name__ == '__main__':
#     unittest.main()


# write a second test for people who include a middle name. (test_name_function.py [modified])

import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Test case for 'name_function.py'."""
    
    def test_first_last_name(self):
        """Do names like Anuradha Karn work?"""
        formatted_name = get_formatted_name('anuradha', 'karn')
        self.assertEqual(formatted_name, 'Anuradha Karn')
    
    def test_first_middle_last_name(self):
        """Do names like Elon Reeve Musk work?"""
        formatted_name = get_formatted_name('elon', 'musk', 'reeve')
        self.assertEqual(formatted_name, 'Elon Reeve Musk')
        
if __name__ == '__main__':
    unittest.main()