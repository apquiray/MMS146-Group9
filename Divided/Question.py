from abc import ABC, abstractmethod

class Question(ABC):
    '''
    An abstract base class that represents the general quiz questions.
    '''
    
    def __init__(self, question_text, correct_answer, category):
    """
    Initializes the Question with its text (statement), the correct answer, and category.
    """
        self.question_text = question_text
        self.correct_answer = correct_answer
        self.category = category

    @abstractmethod
    def display_question(self):
    """
    Abstract method to define how the question is displayed to the user
    """
        pass    # Empty method for the abstract

    @abstractmethod
    """
    Abstract method that checks if the user’s answer is correct
    """
    def check_answer(self, answer):
        pass    # Empty method for the abstract

    def to_dict(self):
    """
    Creates a dictionary containing the properties of each question         
    """

        return {
            "question_text": self.question_text,       # The question itself
            "correct_answer": self.correct_answer,     # The correct answer    
            "category": self.category,                 # The topic category
            "type": self.__class__.__name__            # The type of question, multiple choice or true/false.
        }
