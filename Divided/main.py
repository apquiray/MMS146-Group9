from Student import Student
from ExamReviewer import ExamReviewer
from TrueFalseQuestion import TrueFalseQuestion
from MultipleChoiceQuestion import MultipleChoiceQuestion

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