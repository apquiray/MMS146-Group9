from Question import Question

class TrueFalseQuestion(Question):
    def display_question(self):
        print(f"\n{self.question_text} (True/False)")
    
    def check_answer(self, answer):
        return answer.lower() == self.correct_answer.lower()
