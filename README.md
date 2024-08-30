MMS 146 Group 9
Final Project

Members: 
Billones, Jia;
Dean, Pinky Michelle;
Dela Cruz, John Mark;
Geva, Ashley Jade;
Lacap, Kiara Marie;
Lindayag, Rayshanne;
Llantada, Jass;
Quiray, Alyanna Regina;
Reodica, Richelda Mei

Text-based Exam Reviewer


READ ME

1. Run the program on main.py

2. Enter the Name of the User.

3. Select a Topic between the Four Categories:
   - Philippine Geography
   - Filipino Pop Culture
   - Filipino Culture
   - All Categories
- The user will be given a choice between four categories. If the user inputs a wrong character or number, the program will send a message saying the input is invalid and allow the user to enter an input again.

4. Number of Questions
- Each category has a maximum of 30 questions except for the “All Categories,” which has 90, containing all the questions inside the exam reviewer program. 
- The user can choose how many questions will appear on the screen. It can be 1-30 for Philippine Geography, Filipino Pop Culture, and Filipino Culture and 1-90 for “All Categories.”
- If the user enters an incorrect character, a negative number, or exceeds the expected limit, the program will display an invalid input message and prompt the user to enter a valid number.

5. Set a Time Limit
- The user will set a time limit for each question. The maximum is 60 seconds. 
- If the user inputs a wrong character or negative number, the program will send a message saying the input is invalid and allow the user to enter a valid number.
- If the user inputs a number that exceeds the time limit, the program will automatically set the time to its max (60 seconds).
- The timer will appear in real-time on the screen.

6. Answering the Questions
- The exam reviewer program is composed of True or False and Multiple-choice questions. 
- The user will choose between T for True, F for False, or A, B, and C for multiple choice.
- The program is not case-sensitive on this part.
- If the user doesn’t answer in time, the program will automatically label the item wrong. It will then display a message that will inform the user to press enter to continue.

7. Performance Report
- After answering all the questions, the program will automatically save the answers, questions, and performance history of the user in a text file.
- The program will display the current score summary of the review. It will show what is the category during the session, how many correct and incorrect answers, the overall score, and its percentage.
- Besides the current score summary, it will also display the whole performance history of the user in each review if the user decides to have multiple sessions.

8. Another Session 
- At the end of the performance history, the program will ask the user if they like another session. 
- If the user answers yes, it will bring back the user to the “Select a Topic” part. The user will then proceed to the same procedure as the previous session.
- If the user answers no, it will break the loop and end the session. It will display a message to the user saying “You got this! Good luck :)”
- The program is not case-sensitive on this part.
