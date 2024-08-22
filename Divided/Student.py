class Student:
    def __init__(self, name):
        self.name = name
        self.answers = {}
        self.history = []

    def save_answer(self, question_id, answer):
        self.answers[question_id] = answer

    def get_performance_report(self, questions):
        correct = 0
        total = len(questions)
        for q_id, question in enumerate(questions):
            if question.check_answer(self.answers.get(q_id, "")):
                correct += 1
        percentage = (correct / total) * 100
        report = {
            "Correct Answers": correct,
            "Incorrect Answers": total - correct,
            "Score": f"{correct}/{total}",
            "Percentage": f"{percentage:.2f}%"
        }
        self.history.append(report)
        print(report)

    def view_performance_history(self):
        print(f"Performance history for {self.name}:")
        for i, report in enumerate(self.history, 1):
            print(f"Session {i}: {report}")
    
    def save_answers_to_file(self, filename="student_answers.txt"):
        with open(filename, "w") as f:
            for question_id, answer in self.answers.items():
                f.write(f"Question ID: {question_id}, Answer: {answer}\n")

    def save_performance_history_to_file(self, filename="performance_history.txt"):
        with open(filename, "w") as f:
            for i, report in enumerate(self.history, 1):
                f.write(f"Session {i}: {report}\n")