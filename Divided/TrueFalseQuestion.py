from Question import Question

class TrueFalseQuestion(Question):
    '''
    This class is inherited from the Question class
    and handles True or False type questions for the reviewer.
    '''

    # This method displays the question prompt
    def display_question(self):
        print(f"\n{self.question_text} (T for TRUE, F for FALSE)")

    # This method validates the users answer
    # It also checks if the users answer matches the expected response
    def check_answer(self, answer):
        # Checks if answer is True
        if answer.upper() == "T":
            return self.correct_answer.lower() == "true"
        # Checks if answer is False
        elif answer.upper() == "F":
            return self.correct_answer.lower() == "false"
        # Invalid response
        else:
            return False
