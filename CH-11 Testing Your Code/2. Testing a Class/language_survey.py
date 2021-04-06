# To show that the AnonymousSurvey class works, let’s write a program that uses the class.

# language_survey.py

from survey import AnonymousSurvey

# Define a question, and make a survey.
question = "What language do you learn first to speak?"
my_survey = AnonymousSurvey(question)

# Show the question, and store the responses to the question.
my_survey.show_question()
print("Enter 'q' at anytime to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_single_response(response)
    
# Show the survey result
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()