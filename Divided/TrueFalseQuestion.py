from Question import Question

class TrueFalseQuestion(Question):
    '''
    A class for true/false questions
    '''
    def display_question(self):
    '''
    Displays the question with T/F options
    '''
        print(f"\n{self.question_text} (True/False)")
    
    def check_answer(self, answer):
    '''
    Checks if the answer is correct
    '''
        if answer.upper() == "T":
            return self.correct_answer.lower() == "true"
        elif answer.upper() == "F":
            return self.correct_answer.lower() == "false"
        else:
            return False
