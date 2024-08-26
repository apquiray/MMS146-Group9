from Question import Question

    """
    The class MultipleChoiceQuestion is a subclass and inherits the Question superclass.
    """
class MultipleChoiceQuestion(Question):
    def __init__(self, question_text, options, correct_answer, category):
        super().__init__(question_text, correct_answer, category)
        self.options = options

    """
    This method displays the question to users.
    This is followed by options ranging from A, B, C, etc. 
    """
    def display_question(self):
        print(f"\n{self.question_text}")
        for i, option in enumerate(self.options):
            letter = chr(65 + i)
            print(f"{letter}: {option}")
        
    """
    This method checks the answer to see whether it is acceptable on the conditions given.
    """
    def check_answer(self, answer):
        try:
            index = ord(answer.upper()) - 65
            selected_option = self.options[index]
            return selected_option == self.correct_answer
        except (ValueError, IndexError):
            return False
    """
    This method creates a dictionary containing the attributes of the MultipleChoiceQuestion.
    Making it easier to store or retrieve information on the MultipleChoicequestions.
    """
    def to_dict(self):
        data = super().to_dict()
        data["options"] = self.options
        return data
