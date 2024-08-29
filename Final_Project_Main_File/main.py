from Student import Student
from ExamReviewer import ExamReviewer
from TrueFalseQuestion import TrueFalseQuestion
from MultipleChoiceQuestion import MultipleChoiceQuestion

# Main Program
"""
Start the main program to run the exam reviewer application 
"""
def main():
    """
    Prompt the user to enter their name and create a new Student object 
    """
    student_name = input("Enter your name: ").strip()
    student = Student(student_name)

    """
    Initialize the ExamReviewer with an empty list of exam questions
    """
    exam_reviewer = ExamReviewer([])

    """
    Attempt to load exam questions from an external file using the ExamReviewer object. If the file is successfully loaded, the questions are ready for review. 
    If the file is missing, a FileNotFoundError is caught, and the program uses a predefined list of questions instead.
    """
    try:
        exam_reviewer.load_questions_from_file()
        print("Questions loaded from file.")
    except FileNotFoundError:
        print("File not found. Using default questions.")
        questions = [

            # Filipino Culture
            # This set of questions is about Filipino culture, including traditions, festivals, national symbols, and well-known practices. 
            # 1-10
            MultipleChoiceQuestion("Which of the following is considered the national hero of the Philippines?", ["Jose Rizal", "Andres Bonifacio", "Emilio Aguinaldo"], "Jose Rizal", "Filipino Culture"),
            MultipleChoiceQuestion("The 'Ati-Atihan' festival is celebrated in honor of which saint?", ["Santo Niño", "San Isidro", "San Miguel"], "Santo Niño", "Filipino Culture"),
            MultipleChoiceQuestion("The 'Sinulog' festival is held in which city?", ["Cebu City", "Davao City", "Manila"], "Cebu City", "Filipino Culture"),
            MultipleChoiceQuestion("Which Filipino dish is known for its sour taste and is commonly made with tamarind or other sour fruits?", ["Adobo", "Sinigang", "Kare-Kare"], "Sinigang", "Filipino Culture"),
            TrueFalseQuestion("The 'Mano' gesture is a sign of respect where the younger person takes the hand of an elder and touches it to their forehead.", "True", "Filipino Culture"),
            TrueFalseQuestion("The traditional Filipino dress for women is called the 'Barong Tagalog.'", "False", "Filipino Culture"),
            TrueFalseQuestion("The Bahay Kubo is a traditional Filipino house made of bamboo and nipa palm.", "True", "Filipino Culture"),
            TrueFalseQuestion("The 'Lechon' is a traditional Filipino dish made from roasted chicken.", "False", "Filipino Culture"),
            TrueFalseQuestion("The Filipino festival 'Panagbenga' is also known as the Flower Festival and is celebrated in Baguio City.", "True", "Filipino Culture"),
            TrueFalseQuestion("The traditional Filipino 'Pahiyas' festival is celebrated to give thanks for a bountiful harvest.", "True", "Filipino Culture"),

            # 11-20
            MultipleChoiceQuestion("Which of the following dishes is a Filipino dessert made from sticky rice, coconut milk, and sugar?", ["Halo-Halo", "Leche Flan", "Bibingka"], "Bibingka", "Filipino Culture"),
            MultipleChoiceQuestion("'Adobo' is a popular Filipino dish made with which main ingredients?", ["Chicken or Pork", "Rice and Fish", "Vegetables"], "Chicken or Pork", "Filipino Culture"),
            MultipleChoiceQuestion("Which of the following is a Filipino cultural practice during Christmas where children go from house to house singing carols?", ["Simbang Gabi", "Pabasa", "Panunuluyan"], "Panunuluyan", "Filipino Culture"),
            TrueFalseQuestion("The dish 'Sinigang' is typically sour due to the use of tamarind or other souring agents.", "True", "Filipino Culture"),
            TrueFalseQuestion("'Balut' is a fertilized duck egg that is boiled and eaten as a popular street food in the Philippines.", "True", "Filipino Culture"),
            TrueFalseQuestion("'Lechon' refers to a roasted pig, which is a centerpiece in Filipino celebrations.", "True", "Filipino Culture"),
            TrueFalseQuestion("The 'Bayanihan' spirit is the Filipino practice of communal unity and cooperation.", "True", "Filipino Culture"),
            TrueFalseQuestion("'Pamamanhikan' is the traditional Filipino practice where the groom's family visits the bride's family to formally ask for her hand in marriage.", "True", "Filipino Culture"),
            TrueFalseQuestion("The 'Simbang Gabi' is a series of nine dawn masses leading up to Christmas.", "True", "Filipino Culture"),
            TrueFalseQuestion("'Harana' is a traditional Filipino courtship practice where a man serenades a woman outside her window.", "True", "Filipino Culture"),

            # 21-30
            MultipleChoiceQuestion("Which festival in the Philippines is known for its colorful and elaborate masks?", ["Pahiyas", "MassKara", "Pintados"], "MassKara", "Filipino Culture"),
            MultipleChoiceQuestion("The 'Parol' is a traditional Filipino decoration made during which season?", ["Christmas", "Easter", "All Saints' Day"], "Christmas", "Filipino Culture"),
            MultipleChoiceQuestion("What Filipino dish consists of rice cooked in coconut milk and served with sweet caramelized toppings?", ["Bico", "Sapin-sapin", "Kutsinta"], "Bico", "Filipino Culture"),
            MultipleChoiceQuestion("Which of the following is a popular Filipino street food that is made from skewered grilled chicken or pork intestines?", ["Isaw", "Lumpia", "Betamax"], "Isaw", "Filipino Culture"),
            MultipleChoiceQuestion("In the Filipino dish 'Kare-kare', what is its main ingredient?", ["Chicken", "Beef/Oxtail", "Pork"], "Beef/Oxtail", "Filipino Culture"),
            TrueFalseQuestion("The Sinulog Festival is held in Cebu in honor of the Santo Niño.", "True", "Filipino Culture"),
            TrueFalseQuestion("The Kadayawan Festival is celebrated in Davao to give thanks for a bountiful harvest.", "True", "Filipino Culture"),
            TrueFalseQuestion("The 'Santacruzan' is a religious-historical parade held in May to honor the search for the True Cross by Queen Helena.", "True", "Filipino Culture"),
            TrueFalseQuestion("Taho is a common snack sold in the Philippines. It is a soybean pudding mixed with sago and tapioca pearls.", "True", "Filipino Culture"),
            TrueFalseQuestion("Bagoong is a side dish made from fermented leaves.", "False", "Filipino Culture"), 

            # Filipino Pop Culture
            # This set of questions is about Philippine Pop Culture, covering Filipino music, film, television, and famous personalities.
            # 31-40
            MultipleChoiceQuestion("Who is known as the 'King of Philippine Movies'?", ["Dolphy", "Fernando Poe Jr.", "Nora Aunor"], "Fernando Poe Jr.", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Who is the Filipino singer known for the international hit 'Pyramid'?", ["Charice Pempengco", "Sarah Geronimo", "Regine Velasquez"], "Charice Pempengco", "Filipino Pop Culture"),
            MultipleChoiceQuestion("'Buwan' is a hit song by which Filipino artist?", ["Ben&Ben", "Moira Dela Torre", "Juan Karlos Labajo"], "Juan Karlos Labajo", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Which Filipino singer is known as the 'Asia's Songbird'?", ["Sarah Geronimo", "Regine Velasquez", "Zsa Zsa Padilla"], "Regine Velasquez", "Filipino Pop Culture"),
            MultipleChoiceQuestion("The song 'Tatsulok' by Bamboo is a cover of a song by which original band?", ["Buklod", "The Dawn", "Rivermaya"], "Buklod", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Which Filipino film won the Palme d'Or at the Cannes Film Festival in 2000?", ["Oro, Plata, Mata", "Lino Brocka's 'Insiang'", "Raymond Red's 'Anino'"], "Raymond Red's 'Anino'", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Which film franchise stars Vic Sotto as a superhero who wears a blue suit?", ["Darna", "Lastikman", "Enteng Kabisote"], "Enteng Kabisote", "Filipino Pop Culture"),
            TrueFalseQuestion("The song 'Anak' by Freddie Aguilar is one of the most popular Filipino songs globally.", "True", "Filipino Pop Culture"),
            TrueFalseQuestion("The Filipino rock band 'Eraserheads' is often referred to as the 'Beatles of the Philippines.'", "True", "Filipino Pop Culture"),
            TrueFalseQuestion("The film 'Himala,' starring Nora Aunor, is considered one of the greatest Filipino films of all time.", "True", "Filipino Pop Culture"),

            # 41-50
            MultipleChoiceQuestion("The film 'Kita Kita' is a romantic comedy set in which country?", ["Japan", "Italy", "France"], "Japan", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Who is the director of the critically acclaimed film 'Heneral Luna'?", ["Jerrold Tarog", "Lav Diaz", "Brillante Mendoza"], "Jerrold Tarog", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Who starred as the lead role in the 2018 film 'Goyo: Ang Batang Heneral'?", ["Enrique Gil", "Alden Richards", "Paulo Avelino"], "Paulo Avelino", "Filipino Pop Culture"),
            MultipleChoiceQuestion("The 2001 Filipino film 'Dekada '70' is based on a novel written by which author?", ["Lualhati Bautista", "F. Sionil José", "Ricky Lee"], "Lualhati Bautista", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Which Filipino TV drama featured the love team known as 'AlDub'?", ["Pangako Sa 'Yo", "Kalyeserye", "Mara Clara"], "Kalyeserye", "Filipino Pop Culture"),
            MultipleChoiceQuestion("'Ang Probinsyano,' starring Coco Martin, is based on a 1997 film by which actor?", ["Robin Padilla", "Fernando Poe Jr.", "Rudy Fernandez"], "Fernando Poe Jr.", "Filipino Pop Culture"),
            MultipleChoiceQuestion("'FPJ's Ang Probinsyano' celebrated its 1000th episode in which year?", ["2018", "2019", "2020"], "2019", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Which Filipino actress starred as 'Marimar' in the 2007 Philippine adaptation of the Mexican telenovela?", ["Marian Rivera", "Angel Locsin", "Anne Curtis"], "Marian Rivera", "Filipino Pop Culture"),
            TrueFalseQuestion("'Eat Bulaga!' is the longest-running noontime variety show in the Philippines.", "True", "Filipino Pop Culture"),
            TrueFalseQuestion("'Maalaala Mo Kaya' is a long-running drama anthology that features true stories of ordinary Filipinos.", "True", "Filipino Pop Culture"),

            # 51-60
            MultipleChoiceQuestion("The Filipino TV series 'Encantandia' features a story about four kingdoms. Name one of the kingdom called in the story?", ["Sang'gre", "Diwata", "Lireo"], "Lireo", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Who is the Filipino boxer known as 'Pacman' and is also a former Senator?", ["Nonito Donaire", "Manny Pacquiao", "Gerry Peñalosa"], "Manny Pacquiao", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Which Filipino actress is known as the 'Star for All Seasons'?", ["Vilma Santos", "Sharon Cuneta", "Nora Aunor"], "Vilma Santos", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Who became the first-ever Miss Universe from the Philippines in 1969?", ["Pia Wurtzbach", "Gloria Diaz", "Margie Moran"], "Gloria Diaz", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Jose Rizal, the national hero of the Philippines, which one of these did he NOT write?", ["Noli Me Tangere", "El Filibusterismo", "Florante at Laura"], "Florante at Laura", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Which Filipino actor became the first Asian to win the Best Actor award at the Venice Film Festival?", ["Dolphy", "Christopher de Leon", "John Arcilla"], "John Arcilla", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Who was the first Filipino to win a Grammy Award?", ["Lea Salonga", "Larry Ramos", "apl.de.ap"], "Larry Ramos", "Filipino Pop Culture"),
            MultipleChoiceQuestion("Which Filipino fashion designer is known for dressing international celebrities like Beyoncé and Jennifer Lopez?", ["Rajo Laurel", "Michael Cinco", "Monique Lhuilier"], "Michael Cinco", "Filipino Pop Culture"),
            TrueFalseQuestion("Lea Salonga provided the singing voice for two Disney princesses, Jasmine in 'Aladdin' and Mulan in 'Mulan.'", "True", "Filipino Pop Culture"),
            TrueFalseQuestion("The comedian Dolphy is also known as the 'Comedy King' of the Philippines.", "True", "Filipino Pop Culture"),

            # Philippine Geography
            # This set of questions is about Philippine Geography, covering landmarks, natural features, and the general geography of the country.
            # 61-70
            MultipleChoiceQuestion("The Philippines is an archipelago made up of how many islands?", ["7,641", "8,641", "6,437"], "7,641", "Philippine Geography"),
            MultipleChoiceQuestion("The Philippines is divided into how many regions?", ["17", "15", "20"], "17", "Philippine Geography"),
            MultipleChoiceQuestion("Which region is known as the 'Rice Granary of the Philippines'?", ["Ilocos Region", "Central Luzon", "Cagayan Valley"], "Central Luzon", "Philippine Geography"),
            MultipleChoiceQuestion("Baguio City is located in which province?", ["Benguet", "La Union", "Pangasinan"], "Benguet", "Philippine Geography"),
            MultipleChoiceQuestion("The Chocolate Hills are found in which province?", ["Bohol", "Cebu", "Negros Oriental"], "Bohol", "Philippine Geography"),
            MultipleChoiceQuestion("The Banaue Rice Terraces, often referred to as the 'Eight Wonder of the World,' are located in which region?", ["Cordillera Administrative Region", "Ilocos Region", "Central Luzon"], "Cordillera Administrative Region", "Philippine Geography"),
            TrueFalseQuestion("The capital city of the Philippines is Quezon City.", "False (The capital is Manila)", "Philippine Geography"),
            TrueFalseQuestion("The longest river in the Philippines is the Cagayan River.", "True", "Philippine Geography"),
            TrueFalseQuestion("The region of Mindanao is known for the large volcanic island of Mindanao.", "True", "Philippine Geography"),
            TrueFalseQuestion("Palawan is known as the 'Last Frontier' of the Philippines due to its biodiversity.", "True", "Philippine Geography"),

            # 71-80
            MultipleChoiceQuestion("Mount Apo, the highest peak in the Philippines, is located in which island?", ["Luzon", "Visayas", "Mindanao"], "Mindanao", "Philippine Geography"),
            MultipleChoiceQuestion("Which island in the Philippines is known for its white sand beaches and is a popular tourist destination?", ["Boracay", "Siargao", "Camiguin"], "Boracay", "Philippine Geography"),
            MultipleChoiceQuestion("The Hundred Islands National Park is located in which province?", ["Pangasinan", "Zambales", "La Union"], "Pangasinan", "Philippine Geography"),
            MultipleChoiceQuestion("Which of the following is a major agricultural product of the Philippines?", ["Rice", "Wheat", "Barley"], "Rice", "Philippine Geography"),
            MultipleChoiceQuestion("Which Philippine island is the largest by land area?", ["Luzon", "Mindanao", "Samar"], "Luzon", "Philippine Geography"),
            TrueFalseQuestion("The Taal Volcano is located within a lake in the province of Batangas.", "True", "Philippine Geography"),
            TrueFalseQuestion("The Puerto Princesa Subterranean River is one of the New 7 Wonders of Nature.", "True", "Philippine Geography"),
            TrueFalseQuestion("The Philippines is part of the Pacific Ring of Fire, making it prone to earthquakes and volcanic eruptions.", "True", "Philippine Geography"),
            TrueFalseQuestion("The Philippines has a tropical maritime climate, characterized by high temperatures, high humidity, and abundant rainfall.", "True", "Philippine Geography"),
            TrueFalseQuestion("The Sierra Madre is the longest mountain range in the Philippines.", "True", "Philippine Geography"),

            # 81-90
            MultipleChoiceQuestion("What is the primary source of energy in the Philippines?", ["Solar", "Wind", "Hydropower", "Geothermal"], "Geothermal", "Philippine Geography"),
            MultipleChoiceQuestion("What province is found in the northernmost part of the Philippines?", ["Ilocos", "Cagayan", "Zamboanga", "Batanes"], "Batanes", "Philippine Geography"),
            MultipleChoiceQuestion("What is the capital of the province of Cebu?", ["Lapu-Lapu City", "Mandaue City", "Cebu City", "Talisay City"], "Cebu City", "Philippine Geography"),
            MultipleChoiceQuestion("What is the oldest city in the Philippines?", ["Quezon City", "Cebu City", "Davao City", "Zamboanga City"], "Cebu City", "Philippine Geography"),
            MultipleChoiceQuestion("What is known as the surfing capital of the Philippines?", ["Boracay", "La Union", "Bohol", "Siargao"], "Siargao", "Philippine Geography"),
            TrueFalseQuestion("The Philippines experiences an average of 20 typhoons each year.", "True", "Philippine Geography"),
            TrueFalseQuestion("The Philippines is one of the top producers of coconut products in the world.", "True", "Philippine Geography"),
            TrueFalseQuestion("Mount Mayon is known for its almost perfect cone shape.", "True", "Philippine Geography"),
            TrueFalseQuestion("The capital of Negros Oriental is Bacolod City.", "False", "Philippine Geography"),
            TrueFalseQuestion("The island of Palawan is located in the Visayas region.", "False", "Philippine Geography"),
        ]
        """
        These questions will be used for the exam review process.
        The questions are also saved to a file to ensure persistence.
        """
        exam_reviewer = ExamReviewer(questions)
        exam_reviewer.save_questions_to_file()
    
    """
    Start a review session and allow the student to customize the session settings such as category, number of questions, and time limit. 
    """
    while True:
        category, num_questions, time_limit = exam_reviewer.customize_session()
        exam_reviewer.start_review(student, category, num_questions, time_limit)

        """
        Save the student's answers and performance history after each review session.
        """
        student.save_answers_to_file()
        student.save_performance_history_to_file()
        student.view_performance_history()

        """
        The program will now prompt the student to decide if they want to have another review session.
        """
        while True:
            again = input("\nWould you like to have another review session? Yes or No: ").strip().lower()
            # If the student chooses "yes", the program will start a new session.
            if again == "yes":
                print("New Session!")
                # This exits the inner loop and starts a new session.
                break
            # If the student chooses "no", the program will display a motivational message and prepare to end. 
            elif again == "no":
                print("You got this! Good luck :)\n")
                # This exits both loops to end the program.
                break
            # If the input is invalid, the program will ask the student to enter "Yes" or "No" again.  
            else:
                print("Invalid input. Please enter 'Yes' or 'No'.")
        # This exits the outer loop to end the program.
        if again == "no":
            break

# The program checks if it's being run as the main module. If so, it will execute the main function.
if __name__ == "__main__":
    main()
