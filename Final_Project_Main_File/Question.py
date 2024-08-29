from abc import ABC, abstractmethod

'''
A sentence is worded or expressed to elicit information.
'''
class Question(ABC):

    """
    An abstract method that represents the general quiz questions.
    Initializes the Question with its text (statement), the correct answer, and category.
    """
    def __init__(self, question_text, correct_answer, category):
        self.question_text = question_text
        self.correct_answer = correct_answer
        self.category = category

    """
    Abstract method to define how the question is displayed to the user
    """
    @abstractmethod
    def display_question(self):
        pass
    
    """
    Abstract method that checks if the user's answer is correct
    The abstract method checks if the user's answer is correct.
        
    This is done by comparing the user's answer to the correct answer specified in the code. 
    This method has different implementations per subclass. 
    """
    @abstractmethod
    def check_answer(self, answer):
        pass

    """
    A dictionary containing the attributes of the object question
    Making it easier to store or retrieve information on the questions
    This method creates a dictionary containing the characteristics of the object question.
    Making it easier to store or retrieve information on the questions.
    """   
    def to_dict(self):
        return {
            # The question itself
            # Stores text question itself
            "question_text": self.question_text,
            # The correct answer  
            # Stores the defined correct answer
            "correct_answer": self.correct_answer,
            # The topic category
            # Stores the defined topic category
            "category": self.category,
            # The type of question, multiple choice or true/false.
            # Defines the type of question, multiple choice or true/false
            "type": self.__class__.__name__
        }
