from Question import Question

class TrueFalseQuestion(Question):
    '''
    This class handles True or False type questions for the reviewer.
    This class inherits from the Question class and contains the methods 
    display_question and check_answer.
    '''
    def display_question(self):
    '''
    This method displays the current questions to the user with the options 
    to answer with 'True' or 'False' and prompts the user to choose between
    T for True and F for false.
    '''
        print(f"\n{self.question_text} (T for TRUE, F for FALSE)")
    
    def check_answer(self, answer):
    '''
    This method validates the user's answer. True if the user's answer matches
    the correct answer, otherwise, False if the answer provided is invalid.
    '''
        if answer.upper() == "T":
            return self.correct_answer.lower() == "true"
        elif answer.upper() == "F":
            return self.correct_answer.lower() == "false"
        else:
            return False
