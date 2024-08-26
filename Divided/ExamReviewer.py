import random
import json
import time
import threading
import sys
from TrueFalseQuestion import TrueFalseQuestion
from MultipleChoiceQuestion import MultipleChoiceQuestion

MAX_TIME_LIMIT = 60

# Declare global variables
timed_out = False
question_answered = False

MAX_QUESTIONS_PER_CATEGORY = {
    "Filipino Culture": 10,
    "Filipino Pop Culture": 30,
    "Philippine Geography": 30
}

class ExamReviewer:
    def __init__(self, questions):
        self.questions = questions

    def timeout(self):
        global timed_out
        print("\nTime's up! You didn't answer in time. Please press Enter.")
        timed_out = True

    def countdown_timer(self, duration):
        """
        This function displays a countdown timer on the same line.
        """
        global timed_out
        global question_answered

        while duration > 0 and not timed_out and not question_answered:
            sys.stdout.write(f"\rAnswer (Time Left: {duration} seconds): ")
            sys.stdout.flush()
            time.sleep(1)
            duration -= 1

        if not timed_out and not question_answered:
            print("\r", end="")  # Clear the line when done
            sys.stdout.flush()

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
        
        max_questions = MAX_QUESTIONS_PER_CATEGORY[category]

        while True:
            try:
                num_questions = int(input(f"Number of Questions (Max {max_questions} Questions): ").strip())
                if num_questions <= 0:
                    print("Number of questions must be greater than 0. Please enter a valid number.")
                elif num_questions > max_questions:
                    print(f"Number of questions exceeds the maximum limit for {category} ({max_questions}). Please enter a valid number.")
                elif num_questions > len(self.questions):
                    print(f"Number of questions exceeds the available questions ({len(self.questions)}). Please enter a valid number.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        while True:
            try:
                time_limit = int(input(f"Set a time limit in seconds for each question (Max {MAX_TIME_LIMIT} seconds): ").strip())
                if time_limit <= 0:
                    raise ValueError("Time limit must be a positive integer.")
                if time_limit > MAX_TIME_LIMIT:
                    print(f"Time limit is too high. Setting time limit to {MAX_TIME_LIMIT} seconds.")
                    time_limit = MAX_TIME_LIMIT
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for the time limit.")

        return category, num_questions, time_limit

    def start_review(self, student, category, num_questions, time_limit):
        global timed_out, question_answered

        questions = self.generate_random_questions(num_questions, category)

        for i, question in enumerate(questions):
            print(f"\nQuestion {i + 1}/{num_questions}:")
            question.display_question()

            # Reset the flags for each question
            timed_out = False
            question_answered = False

            # Create a timer that will call the timeout function
            timer = threading.Timer(time_limit, self.timeout)

            # Start the countdown in a separate thread
            countdown_thread = threading.Thread(target=self.countdown_timer, args=(time_limit,))

            # Start the timer and countdown
            timer.start()
            countdown_thread.start()

            # Get the Answer
            answer = input()

            # Set question answered flag to True
            question_answered = True

            # Cancel the timer to stop it
            timer.cancel()

            # Wait for the countdown thread to finish
            countdown_thread.join()

            # Check if the question timed out
            if timed_out:
                continue  # If timed out, skip saving and go to the next question
            else:
                student.save_answer(i, answer)

        # Provide performance report
        student.get_performance_report(questions, category)

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
