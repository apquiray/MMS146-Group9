from Question import Question

'''
This class is inherited from the Question class
and handles True or False type questions for the reviewer.
'''
class TrueFalseQuestion(Question):

    # This method displays the question prompt
    def display_question(self):
        print(f"\n{self.question_text} (T for True, F for False)")
    
    # This method validates the user's answer
    # It also checks if the user's answer matches the expected response
    def check_answer(self, answer):
        # Checks if the answer is True
        if answer.upper() == "T":
            return self.correct_answer.lower() == "true"
        # Checks if the answer is False
        elif answer.upper() == "F":
            return self.correct_answer.lower() == "false"
        # This will make the answer wrong if the user does not respond.
        else:
            return False
