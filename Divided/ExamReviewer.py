import random
import time
import json
from TrueFalseQuestion import TrueFalseQuestion
from MultipleChoiceQuestion import MultipleChoiceQuestion

MAX_TIME_LIMIT = 60

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
        category_map = {
            "1": "Philippine Geography",
            "2": "Filipino Pop Culture",
            "3": "Filipino Culture"
        }

        print("\nSelect a Topic:")
        print("1. Philippine Geography")
        print("2. Filipino Pop Culture")
        print("3. Filipino Culture")

        while True:
            category_choice = input("Please enter the number corresponding to your category: ").strip()

            if category_choice in category_map:
                category = category_map[category_choice]
                break
            else:
                print("Invalid category choice. Please only enter values among 1, 2, 3.")

        while True:
            try:
                num_questions = int(input("Number of Questions: ").strip())
                if num_questions <= 0:
                    print("Number of questions must be greater than 0. Please enter a valid number.")
                elif num_questions > len(self.questions):
                    print(f"Number of questions exceeds the available questions ({len(self.questions)}). Please enter a valid number.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        while True:
            try:
                time_limit = int(input(f"Set a time limit in seconds for each question (Max {MAX_TIME_LIMIT} seconds): ").strip())
                if time_limit > MAX_TIME_LIMIT:
                    print(f"Time limit is too high. Setting time limit to {MAX_TIME_LIMIT} seconds.")
                    time_limit = MAX_TIME_LIMIT
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for the time limit.")

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
