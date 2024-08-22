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
        category = input("Select a Topic (Philippine Geography, Filipino Pop Culture, Filipino Culture): ").strip()
        num_questions = int(input("Number of Questions: ").strip())
        time_limit = int(input(f"Set a time limit in seconds for each question (Max {MAX_TIME_LIMIT} seconds): ").strip())
        if time_limit > MAX_TIME_LIMIT:
            print(f"Time limit is too high. Setting time limit to {MAX_TIME_LIMIT} seconds.")
            time_limit = MAX_TIME_LIMIT
        return category, num_questions, time_limit

    def start_review(self, student, category, num_questions, time_limit):
        questions = self.generate_random_questions(num_questions, category)

        for i, question in enumerate(questions):
            print(f"\nQuestion {i + 1}/{len(questions)}:")
            start_time = time.time()
            question.display_question()

            while True:
                elapsed_time = time.time() - start_time
                remaining_time = max(0, time_limit - elapsed_time)
                print(f"Time remaining: {int(remaining_time)} seconds", end='\r')

                if remaining_time <= 0:
                    print("\nTime's up for this question!\n")
                    student.save_answer(i, "")  # Save an empty answer for unanswered questions
                    break

                if input("Your Answer: ").strip():
                    answer = input("Your Answer: ").strip()
                    student.save_answer(i, answer)
                    break

            time.sleep(1)  # To ensure the loop doesn't run too quickly

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