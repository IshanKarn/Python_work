# Write a test method to test store_single_response function work or not

# We write a test that verifies one aspect of the way AnonymousSurvey behaves.
# We’ll write a test to verify that a single response to the survey question is
# stored properly. We’ll use the assertIn() method to verify that the response
# is in the list of responses after it’s been stored.

# test_survey.py

# import unittest
# from survey import AnonymousSurvey

# class TestAnonymousSurvey(unittest.TestCase):
#     """Test for the class AnonymousSurvey."""
    
#     def test_store_single_response(self):
#         """Test that a single response is stored properly."""
#         question = "What language did you learn first to speak?"
#         my_survey = AnonymousSurvey(question)
#         my_survey.store_single_response('Hindi')
#         self.assertIn('Hindi', my_survey.responses)
    
# if __name__ == '__main__':
#     unittest.main()
 
# ---------------------------------------------------------------------------------------
     
# This is good, but a survey is useful only if it generates more than one
# response. Let’s verify that three responses can be stored correctly. To do
# this, we add another method to TestAnonymousSurvey

# test_survey.py (updated)

# import unittest
# from survey import AnonymousSurvey

# class TestAnonymousSurvey(unittest.TestCase):
#     """Test for the class AnonymousSurvey."""
    
#     def test_store_single_response(self):
#         """Test that a single response is stored properly."""
#         question = "What language did you learn first to speak?"
#         my_survey = AnonymousSurvey(question)
#         my_survey.store_single_response('Hindi')
#         self.assertIn('Hindi', my_survey.responses)
        
#     def test_store_three_response(self):
#         """Test that three responses are stored properly."""
#         question = "What language did you learn first to speak?"
#         my_survey = AnonymousSurvey(question)
#         responses = ['Hindi', 'English', 'Sanskrit']
#         for response in responses:
#             my_survey.store_single_response(response)
#         for response in responses:
#             self.assertIn(response, my_survey.responses)
        
# if __name__ == '__main__':
#     unittest.main() 


# test_survey.py (updated)

import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Test for the class AnonymousSurvey."""
    
    def setUp(self):
        """Create a survey and a set of responses for use in all test methods."""
        question = "What language did you learn first to speak?"
        self.survey = AnonymousSurvey(question)
        self.responses = ['Hindi', 'English', 'French']
        
    def test_store_single_response(self):
        """Is single response stored properly?"""
        self.survey.store_single_response(self.responses[0])
        self.assertIn(self.responses[0], self.survey.responses)
        
    def test_store_three_responses(self):
        """Are multiple responses stored properly?"""
        for response in self.responses:
            self.survey.store_single_response(response)
        for response in self.responses:
            self.assertIn(response, self.survey.responses)
            
if __name__ == '__main__':
    unittest.main()
    
# In above update the method setUp() does two things: it creates a survey instance,
# and it creates a list of responses. 
# Each of these is prefixed by self, so they can be used anywhere in the class.