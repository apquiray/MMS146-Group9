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

    """
    The abstract method checks if the user's answer is correct.
        
    This is done by comparing the user's answer to the correct answer specified in the code. 
    This method has different implementations per subclass. 
    """
    @abstractmethod
    def check_answer(self, answer):
        # The pass is an empty method that is made to be overridden by subclasses
        pass 

    """
    This method creates a dictionary containing the attributes of the object question.
    Making it easier to store or retrieve information on the questions.
    """    
    def to_dict(self):
        return {
            # Stores text question itself
            "question_text": self.question_text, 
            # Stores the defined correct answer  
            "correct_answer": self.correct_answer,  
            # Stores the defined topic category
            "category": self.category,   
            # Defines the type of question, multiple choice or true/false
            "type": self.__class__.__name__            
        }
