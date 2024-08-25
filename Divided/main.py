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
            MultipleChoiceQuestion("Which film franchise stars Vic Sotto as a superhero who wears a blue suit?", ["Darna", "Lastikman", "Enteng Kabisote"], "Enteng Kabisote", "Filipino Pop Culture"),

            # 11-20
            MultipleChoiceQuestion("The film 'Kita Kita' is a romantic comedy set in which country?", ["Japan", "Italy", "France"], "Japan", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Who is the director of the critically acclaimed film 'Heneral Luna'?", ["Jerrold Tarog", "Lav Diaz", "Brillante Mendoza"], "Jerrold Tarog", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Who starred as the lead role in the 2018 film 'Goyo: Ang Batang Heneral'?", ["Enrique Gil", "Alden Richards", "Paulo Avelino"], "Paulo Avelino", "Filipino Pop Culture"),
            MultipleChoiceQuestion("The 2001 Filipino film 'Dekada '70' is based on a novel written by which author?", ["Lualhati Bautista", "F. Sionil José", "Ricky Lee"], "Lualhati Bautista", "Filipino Pop Culture"),
            TrueFalseQuestion("'Eat Bulaga!' is the longest-running noontime variety show in the Philippines.", "True", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Which Filipino TV drama featured the love team known as 'AlDub'?", ["Pangako Sa 'Yo", "Kalyeserye", "Mara Clara"], "Kalyeserye", "Filipino Pop Culture"),
            MultipleChoiceQuestion("'Ang Probinsyano,' starring Coco Martin, is based on a 1997 film by which actor?", ["Robin Padilla", "Fernando Poe Jr.", "Rudy Fernandez"], "Fernando Poe Jr.", "Filipino Pop Culture"),
            TrueFalseQuestion("'Maalaala Mo Kaya' is a long-running drama anthology that features true stories of ordinary Filipinos.", "True", "Filipino Pop Culture"),
            MultipleChoiceQuestion("'FPJ's Ang Probinsyano' celebrated its 1000th episode in which year?", ["2018", "2019", "2020"], "2019", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Which Filipino actress starred as 'Marimar' in the 2007 Philippine adaptation of the Mexican telenovela?", ["Marian Rivera", "Angel Locsin", "Anne Curtis"], "Marian Rivera", "Filipino Pop Culture"),

            # 21-30
            MultipleChoiceQuestion("The Filipino TV series 'Encantandia' features a story about four kingdoms. What are these kingdoms collectively called?", ["Sang'gre", "Diwata", "Lireo"], "Sang'gre", "Filipino Pop Culture"),
            TrueFalseQuestion("Lea Salonga provided the singing voice for two Disney princesses, Jasmine in 'Aladdin' and Mulan in 'Mulan.'", "True", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Who is the Filipino boxer known as 'Pacman' and is also a former Senator?", ["Nonito Donaire", "Manny Pacquiao", "Gerry Peñalosa"], "Manny Pacquiao", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Which Filipino actress is known as the 'Star for All Seasons'?", ["Vilma Santos", "Sharon Cuneta", "Nora Aunor"], "Vilma Santos", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Who became the first-ever Miss Universe from the Philippines in 1969?", ["Pia Wurtzbach", "Gloria Diaz", "Margie Moran"], "Gloria Diaz", "Filipino Pop Culture"),
            TrueFalseQuestion("The comedian Dolphy is also known as the 'Comedy King' of the Philippines.", "True", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Jose Rizal, the national hero of the Philippines, wrote which famous novel in Spanish?", ["Noli Me Tangere", "El Filibusterismo", "Florante at Laura"], "Noli Me Tangere", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Which Filipino actor became the first Asian to win the Best Actor award at the Venice Film Festival?", ["Dolphy", "Christopher de Leon", "John Arcilla"], "John Arcilla", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Who was the first Filipino to win a Grammy Award?", ["Lea Salonga", "Bruno Mars", "apl.de.ap"], "Bruno Mars", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Which Filipino fashion designer is known for dressing international celebrities like Beyoncé and Jennifer Lopez?", ["Rajo Laurel", "Michael Cinco", "Monique Lhuilier"], "Michael Cinco", "Filipino Pop Culture"),

            # Philippine Geography

            
            #This set of questions is about Philippine Geography, covering landmarks, natural features, and the general geography of the country.
            #11-20
            MultipleChoiceQuestion("Mount Apo, the highest peak in the Philippines, is located in which island?", ["Luzon", "Visayas", "Mindanao"], "Mindanao", "Philippine Geography"),
            TrueFalseQuestion("The Taal Volcano is located within a lake in the province of Batangas.", "True", "Philippine Geography"),
            MultipleChoiceQuestion("Which island in the Philippines is known for its white sand beaches and is a popular tourist destination?", ["Boracay", "Siargao", "Camiguin"], "Boracay", "Philippine Geography"),
            MultipleChoiceQuestion("The Hundred Islands National Park is located in which province?", ["Pangasinan", "Zambales", "La Union"], "Pangasinan", "Philippine Geography"),
            TrueFalseQuestion("The Puerto Princesa Subterranean River is one of the New 7 Wonders of Nature.", "True", "Philippine Geography"),
            TrueFalseQuestion("The Philippines is part of the Pacific Ring of Fire, making it prone to earthquakes and volcanic eruptions.", "True", "Philippine Geography"),
            TrueFalseQuestion("The Philippines has a tropical maritime climate, characterized by high temperatures, high humidity, and abundant rainfall.", "True", "Philippine Geography"),
            MultipleChoiceQuestion("Which of the following is a major agricultural product of the Philippines?", ["Rice", "Wheat", "Barley"], "Rice", "Philippine Geography"),
            TrueFalseQuestion("The Sierra Madre is the longest mountain range in the Philippines.", "True", "Philippine Geography"),
            MultipleChoiceQuestion("Which Philippine island is the largest by land area?", ["Luzon", "Mindanao", "Samar"], "Luzon", "Philippine Geography")
        
        
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
