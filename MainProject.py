import random
import time
from abc import ABC, abstractmethod
import json

MAX_TIME_LIMIT = 60
# Base class for questions
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

class TrueFalseQuestion(Question):
    def display_question(self):
        print(f"\n{self.question_text} (True/False)")
    
    def check_answer(self, answer):
        return answer.lower() == self.correct_answer.lower()

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
        print(f"\nPerformance history for {self.name}:")
        for i, report in enumerate(self.history, 1):
            print(f"-- Session {i} --")
            for key, value in report.items():
                print (f"{key:20}: {value}")
    
    def save_answers_to_file(self, filename="student_answers.txt"):
        with open(filename, "w") as f:
            for question_id, answer in self.answers.items():
                f.write(f"Question ID: {question_id}, Answer: {answer}\n")

    def save_performance_history_to_file(self, filename="performance_history.txt"):
        with open(filename, "w") as f:
            for i, report in enumerate(self.history, 1):
                f.write(f"Session {i}: {report}\n")

class ExamReviewer:
    def __init__(self, questions):
        self.questions = questions

    def generate_random_questions(self, num_questions, category=None):
        if category:
            filtered_questions = [q for q in self.questions if q.category == category]
        else:
            filtered_questions = self.questions
        return random.sample(filtered_questions, min(num_questions, len(filtered_questions)))

    def customize_session(self):
        category = input("Select a Topic (Philippine Geography, Filipino Pop Culture, Filipino Culture): ").strip()
        num_questions = int(input("Number of Questions: ").strip())
        time_limit = int(input(f"Set a time limit in seconds for each question (Max {MAX_TIME_LIMIT} seconds): ").strip())
        if time_limit > MAX_TIME_LIMIT:
            print(f"Time limit is too high. Setting time limit to {MAX_TIME_LIMIT} seconds.")
            time_limit = MAX_TIME_LIMIT
        return category, num_questions, time_limit

    def start_review(self, student, category, num_questions, time_limit):
        questions = self.generate_random_questions(num_questions, category)
        start_time = time.time()

        for i, question in enumerate(questions):
            elapsed_time = time.time() - start_time
            if elapsed_time > (i + 1) * time_limit:
                print("\nTime's up for this question!\n")
                student.save_answer(i, "")  # Save an empty answer for unanswered questions
                continue

            question.display_question()
            answer = input("Your Answer: ").strip()
            student.save_answer(i, answer)

        student.get_performance_report(questions)

    def save_questions_to_file(self, filename="questions.txt"):
        with open(filename, "w") as f:
            json.dump([q.to_dict() for q in self.questions], f, indent=4)


    def load_questions_from_file(self, filename="questions.txt"):
        with open(filename, "r") as f:
            question_data = json.load(f)
            self.questions = []
            for q_data in question_data:
                if q_data["type"] == "TrueFalseQuestion":
                    question = TrueFalseQuestion(
                        q_data["question_text"],
                        q_data["correct_answer"],
                        q_data["category"]
                    )
                elif q_data["type"] == "MultipleChoiceQuestion":
                    question = MultipleChoiceQuestion(
                        q_data["question_text"],
                        q_data["options"],
                        q_data["correct_answer"],
                        q_data["category"]
                    )
                self.questions.append(question)

# Main Program
def main():
    student_name = input("Enter your name: ").strip()
    student = Student(student_name)

    exam_reviewer = ExamReviewer([])

    try:
        exam_reviewer.load_questions_from_file()
        print("Questions loaded from file.")
    except FileNotFoundError:
        print("File not found. Using default questions.")
        questions = [
            TrueFalseQuestion("The 'Mano' gesture is a sign of respect...", "True", "Filipino Culture"),
            MultipleChoiceQuestion("Which of the following is considered the national hero...", ["Jose Rizal", "Andres Bonifacio", "Emilio Aguinaldo"], "Jose Rizal", "Filipino Culture"),
            TrueFalseQuestion("The capital city of the Philippines is Quezon City.", "False", "Philippine Geography"),
            MultipleChoiceQuestion("Who is known as the 'King of Philippine Movies'?", ["Dolphy", "Fernando Poe Jr.", "Nora Aunor"], "Fernando Poe Jr.", "Filipino Pop Culture"),
            # Add more questions to each category
        ]
        exam_reviewer = ExamReviewer(questions)
        exam_reviewer.save_questions_to_file()

    category, num_questions, time_limit = exam_reviewer.customize_session()
    exam_reviewer.start_review(student, category, num_questions, time_limit)

    student.save_answers_to_file()
    student.save_performance_history_to_file()
    student.view_performance_history()

if __name__ == "__main__":
    main()
    #test
