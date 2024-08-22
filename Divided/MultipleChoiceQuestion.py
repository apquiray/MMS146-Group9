from Question import Question

class MultipleChoiceQuestion(Question):
    def __init__(self, question_text, options, correct_answer, category):
        super().__init__(question_text, correct_answer, category)
        self.options = options

    def display_question(self):
        print(f"\n{self.question_text}")
        for i, option in enumerate(self.options):
            letter = chr(65 + i)
            print(f"{letter}: {option}")
    
    def check_answer(self, answer):
        try:
            index = ord(answer.upper()) - 65
            selected_option = self.options[index]
            return selected_option == self.correct_answer
        except (ValueError, IndexError):
            return False

    def to_dict(self):
        data = super().to_dict()
        data["options"] = self.options
        return data
