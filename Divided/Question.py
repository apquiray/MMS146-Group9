from abc import ABC, abstractmethod

class Question(ABC):
    def __init__(self, question_text, correct_answer, category):
        self.question_text = question_text
        self.correct_answer = correct_answer
        self.category = category

    @abstractmethod
    def display_question(self):
        pass

    @abstractmethod
    def check_answer(self, answer):
        pass

    def to_dict(self):
        return {
            "question_text": self.question_text,
            "correct_answer": self.correct_answer,
            "category": self.category,
            "type": self.__class__.__name__
        }
