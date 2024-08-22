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

            # Filipino Pop Culture
            TrueFalseQuestion("The song 'Anak' by Freddie Aguilar is one of the most popular Filipino songs globally.", "True", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Who is known as the 'King of Philippine Movies'?", ["Dolphy", "Fernando Poe Jr.", "Nora Aunor"], "Fernando Poe Jr.", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Who is the Filipino singer known for the international hit 'Pyramid'?", ["Charice Pempengco", "Sarah Geronimo", "Regine Velasquez"], "Charice Pempengco", "Filipino Pop Culture"),
            TrueFalseQuestion("The Filipino rock band 'Eraserheads' is often referred to as the 'Beatles of the Philippines.'", "True", "Filipino Pop Culture"),
            MultipleChoiceQuestion("'Buwan' is a hit song by which Filipino artist?", ["Ben&Ben", "Moira Dela Torre", "Juan Karlos Labajo"], "Juan Karlos Labajo", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Which Filipino singer is known as the 'Asia's Songbird'?", ["Sarah Geronimo", "Regine Velasquez", "Zsa Zsa Padilla"], "Regine Velasquez", "Filipino Pop Culture"),
            MultipleChoiceQuestion("The song 'Tatsulok' by Bamboo is a cover of a song by which original band?", ["Asin", "The Dawn", "Rivermaya"], "Asin", "Filipino Pop Culture"),
            TrueFalseQuestion("The film 'Himala,' starring Nora Aunor, is considered one of the greatest Filipino films of all time.", "True", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Which Filipino film won the Palme d'Or at the Cannes Film Festival in 2000?", ["Oro, Plata, Mata", "Lino Brocka's 'Insiang'", "Brillante Mendoza's 'Kinatay'"], "Brillante Mendoza's 'Kinatay'", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Which film franchise stars Vic Sotto as a superhero who wears a blue suit?", ["Darna", "Lastikman", "Enteng Kabisote"], "Enteng Kabisote", "Filipino Pop Culture")
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
