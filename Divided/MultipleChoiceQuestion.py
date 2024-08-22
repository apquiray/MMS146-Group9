from Question import Question

class MultipleChoiceQuestion(Question):
    def __init__(self, question_text, options, correct_answer, category):
        super().__init__(question_text, correct_answer, category)
        self.options = options

    def display_question(self):
        print(f"\n{self.question_text}")
        for i, option in enumerate(self.options):
            print(f"{i}: {option}")
    
    def check_answer(self, answer):
        try:
            selected_option = self.options[int(answer)]
            return selected_option == self.correct_answer
        except (ValueError, IndexError):
            return False

    def to_dict(self):
        data = super().to_dict()
        data["options"] = self.options
        return data