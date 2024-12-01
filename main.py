import sys
import random
from Classes import *

# main container
questions = []

# creating some fucking questions
# TODO 14 : GET ALL THIS SHIT ON THERE OWN FILE
question_1 = Question("how are you?", 'sample', 'test', ['a', 'b', 'c'], 'a')
question_2 =  Question(
        question="What is the capital of France?", 
        question_type="Multiple Choice", 
        difficulty="Easy", 
        choices=["Berlin", "Madrid", "Paris", "Rome"], 
        correct_answer="Paris"
    )
question_3 = Question(
        question="Which element has the atomic number 1?", 
        question_type="Multiple Choice", 
        difficulty="Easy", 
        choices=["Oxygen", "Hydrogen", "Carbon", "Nitrogen"], 
        correct_answer="Hydrogen"
    )
question_4 = Question(
        question="What is the integral of x^2?", 
        question_type="Mathematics", 
        difficulty="Medium", 
        choices=["x^3 + C", "x^2 + C", "2x + C", "x^3 - C"], 
        correct_answer="x^3 + C"
    )
question_5 = Question(
        question="Who wrote '1984'?", 
        question_type="Multiple Choice", 
        difficulty="Medium", 
        choices=["Aldous Huxley", "George Orwell", "Mark Twain", "Ernest Hemingway"], 
        correct_answer="George Orwell"
    )
question_6 =   Question(
        question="Which planet is known as the Red Planet?", 
        question_type="Multiple Choice", 
        difficulty="Easy", 
        choices=["Earth", "Mars", "Jupiter", "Saturn"], 
        correct_answer="Mars"
    )


questions.append(question_1)
questions.append(question_2)
questions.append(question_3)
questions.append(question_4)
questions.append(question_5)
questions.append(question_6)


# TODO 15 : GET THIS FUNCTIONS ON THIER OWN FILE
def throw_question():
    index = random.randint(0,len(questions)-1)
    return questions[index]

def get_userDetails():
    username = str(input('Youre username ? : '))

    new_user = User(username)

    # grettings 
    print(f'Hello there  {new_user.get_name()}')

def main():
    choice = str(input(f'Would you like to play ? : ( y/n )')).lower()

    if(choice == 'n'):
        sys.exit()


    print('Game starts')
    get_userDetails()
    current_question = throw_question()

    print(current_question.get_question())

    # pretty printing the choices for current_question
    letters = ['A', 'B', 'C', 'D']
    letters_index = 0

    for choice in current_question.get_choices():
        print(f'{letters[letters_index]} {choice}')
        letters_index += 1

        # loop back the letters index to not be out of bounds
        if(letters_index > len(letters)-1):
            letters_index = 0

    # get answers here
    player_answer = str(input('Youre answer ? : ')).lower()

    if(player_answer != current_question.get_answer()):
        print(f'Incorrect the answer is {current_question.get_answer()}')
        print(f'Youre answer is {player_answer}')
    else:
        print(f'Correct ')
main(),