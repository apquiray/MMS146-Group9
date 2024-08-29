"""A class about a person who is studying at a school or college."""
class Student:

    # This method initializes the attributes of the class.
    def __init__(self, name):
        self.name = name
        self.answers = {}
        self.history = []
    # This method allows the user to save or update their answers to specific questions.
    def save_answer(self, question_id, answer):
        self.answers[question_id] = answer

    # This is a method for the performance report of the user after the review session.
    def get_performance_report(self, questions, category):
        correct = 0
        total = len(questions)
    # This is a loop that iterates all the questions checking if the answer is correct and how many of them are correct.
        for q_id, question in enumerate(questions):
            if question.check_answer(self.answers.get(q_id, "")):
                correct += 1
    # This will calculate the percentage of the user's score.
        percentage = (correct / total) * 100
    # This is the dictionary for the performance report.
        report = {
            "Category": category,
            "Correct Answers": correct,
            "Incorrect Answers": total - correct,
            "Score": f"{correct}/{total}",
            "Percentage": f"{percentage:.2f}%"
        }
        print ()
    # This is a loop to display a summary of the report same as the format above.
        print ("-- Current Score Summary --")
        for key, value in the report.items():
    # This will print what is in the dictionary as well as their corresponding values.
            print(f"{key:20}: {value}")
        self.history.append(report)

    # This is a method for the performance of the user for each session.
    def view_performance_history(self):
        print(f"\nPerformance history for {self.name}:")
    # This loop iterates the history of the user's performance.
        for i, report in enumerate(self.history, 1):
    # This will print what sessions is the user currently in.
            print(f"-- Session {i} --")
    # This loop goes through each performance metric within the current session's report.
            for key, value in the report.items():
    # This will then print the metric's name and value in a formatted manner
                print (f"{key:20}: {value}")
    
    # This saves the answer of the user as a text.
    def save_answers_to_file(self, filename="student_answers.txt"):
        with open(filename, "w") as f:
            for question_id, answer in self.answers.items():
                # This will show the question number and answer of the user.
                f.write(f"Question ID: {question_id}, Answer: {answer}\n")

    # This saves the performance history of the user as a tex.
    def save_performance_history_to_file(self, filename="performance_history.txt"):
        with open(filename, "w") as f:
            for i, report in enumerate(self.history, 1):
                # This will show the performance record of the user per session.
                f.write(f"Session {i}: {report}\n")
