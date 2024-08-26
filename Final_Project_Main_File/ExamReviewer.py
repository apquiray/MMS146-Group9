import random
import json
import time
import threading
import sys
from TrueFalseQuestion import TrueFalseQuestion
from MultipleChoiceQuestion import MultipleChoiceQuestion

# This is the max time limit for the timer per question.
MAX_TIME_LIMIT = 60

# This declare global variables.
timed_out = False
question_answered = False

# This declares the maximum number of questions per category.
MAX_QUESTIONS_PER_CATEGORY = {
    "Filipino Culture": 10,
    "Filipino Pop Culture": 30,
    "Philippine Geography": 30
}

"""
A tool or resource designed to help students prepare for exams.
"""
class ExamReviewer:
    def __init__(self, questions):
        self.questions = questions

    
    # This method displays a message to the user when the time is up.
    def timeout(self):
        global timed_out
        print("\nTime's up! You didn't answer in time. Please press Enter.")
        timed_out = True
    
    # This method displays a countdown timer on the same line.
    def countdown_timer(self, duration):
        global timed_out
        global question_answered

        # This will show how much the time is left for the user to answer.
        while duration > 0 and not timed_out and not question_answered:
            sys.stdout.write(f"\rAnswer (Time Left: {duration} seconds): ")
            sys.stdout.flush()
            time.sleep(1)
            duration -= 1

        # This clears the line when done.
        if not timed_out and not question_answered:
            print("\r", end="")  
            sys.stdout.flush()

    # This method generates a random question for the user.
    def generate_random_questions(self, num_questions, category=None):
        # This checks if a category is provided.
        if category:
            # This filters the questions to only include those that match the specified category.
            filtered_questions = [q for q in self.questions if q.category == category]
        else:
            # If no category is specified, this will use all available questions.
            filtered_questions = self.questions
        # This returns a random selection of questions.
        # The number of questions returned is the smaller of the requested number and the total available filtered questions.
        return random.sample(filtered_questions, min(num_questions, len(filtered_questions)))

    # This method is for the user to customize the exam reviewer.
    def customize_session(self):
        # This is a dictionary that maps user input numbers to category names.
        category_map = {
            "1": "Philippine Geography",
            "2": "Filipino Pop Culture",
            "3": "Filipino Culture"
        }
        # This prints the options for the user to select a topic.
        print("\nSelect a Topic:")
        print("1. Philippine Geography")
        print("2. Filipino Pop Culture")
        print("3. Filipino Culture")

        # This is a loop until the user provides a valid category choice.
        while True:
            # This prompts the user to enter a category number.
            category_choice = input("Please enter the number corresponding to your category: ").strip()
            # This checks if the entered category is valid or it existed in the category_map.
            if category_choice in category_map:
            # This gets the corresponding category name from the map.
                category = category_map[category_choice]
                # This exits the loop once a valid choice is made.
                break
            else:
                # This informs the user of the invalid choice and prompt again.
                print("Invalid category choice. Please only enter values among 1, 2, 3.")
        
        # This retrieves the maximum number of questions available for the selected category.
        max_questions = MAX_QUESTIONS_PER_CATEGORY[category]

        # This is also a loop until the user provides a valid category choice.
        while True:
            try:
                # This prompts the user to enter the number of questions.
                num_questions = int(input(f"Number of Questions (Max {max_questions} Questions): ").strip())
                # This validates the entered number of questions.
                if num_questions <= 0:
                    print("Number of questions must be greater than 0. Please enter a valid number.")
                elif num_questions > max_questions:
                    print(f"Number of questions exceeds the maximum limit for {category} ({max_questions}). Please enter a valid number.")
                elif num_questions > len(self.questions):
                    print(f"Number of questions exceeds the available questions ({len(self.questions)}). Please enter a valid number.")
                else:
                    # This also exits the loop once a valid choice is made.
                    break
            except ValueError:
                # This informs the user of invalid input (not an integer) and prompt again.
                print("Invalid input. Please enter a valid number.")
        
        # Another loop until the user provides a valid time limit per question.
        while True:
            try:
                # This prompts the user to enter a time limit in seconds for each question.
                time_limit = int(input(f"Set a time limit in seconds for each question (Max {MAX_TIME_LIMIT} seconds): ").strip())
                # This validates the entered time limit.
                if time_limit <= 0:
                    raise ValueError("Time limit must be a positive integer.")
                if time_limit > MAX_TIME_LIMIT:
                    print(f"Time limit is too high. Setting time limit to {MAX_TIME_LIMIT} seconds.")
                    time_limit = MAX_TIME_LIMIT
                # Another exit from the loop once a valid time limit is entered.
                break
            except ValueError:
                 # This informs the user of invalid input (not a valid positive integer) and prompt again.
                print("Invalid input. Please enter a valid number for the time limit.")

        # This returns the selected category, number of questions, and time limit to the caller.
        return category, num_questions, time_limit
    
    # This method starts the exam reviewer for the user.
    def start_review(self, student, category, num_questions, time_limit):
        global timed_out, question_answered

        # This generates a list of random questions based on the selected category and number of questions.
        questions = self.generate_random_questions(num_questions, category)

        # A loop through each question in the generated list.
        for i, question in enumerate(questions):
            print(f"\nQuestion {i + 1}/{num_questions}:")
             # This calls the method to display the current question.
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

    # This is a method that saves the questions from the question bank to the question.txt file.
    def save_questions_to_file(self, filename="questions.txt"):
        with open(filename, "w") as f:
            """ 
            This converts each question in the questions list to a dictionary using the to_dict() method
            and then save the list of dictionaries as a JSON array in the file
            """
            json.dump([q.to_dict() for q in self.questions], f, indent=4)

    # This is a method that loads the saved questions from the questions.txt to the exam reviewer.
    def load_questions_from_file(self, filename="questions.txt"):
        with open(filename, "r") as f:
            # This loads the JSON data from the file into a variable.
            question_data = json.load(f)

            # This clears the current questions list.
            self.questions = []

            # This is a loop through each dictionary in the loaded JSON data.
            for q_data in question_data:
                # This determines the type of question based on the "type" field in the dictionary.
                if q_data["type"] == "TrueFalseQuestion":
                    # This will create a new TrueFalseQuestion object using the data from the dictionary.
                    question = TrueFalseQuestion(
                        # The question text
                        q_data["question_text"],
                        # The correct answer (True/False)
                        q_data["correct_answer"],
                        # The category of the question
                        q_data["category"]
                    )
                elif q_data["type"] == "MultipleChoiceQuestion":
                    # This will create a new MultipleChoiceQuestion object using the data from the dictionary.
                    question = MultipleChoiceQuestion(
                        # The question text
                        q_data["question_text"],
                        # The list of multiple-choice options
                        q_data["options"],
                        # The correct answer (one of the options)
                        q_data["correct_answer"],
                        # The category of the question
                        q_data["category"]
                    )
                # This adds the created question object to the questions list.
                self.questions.append(question)