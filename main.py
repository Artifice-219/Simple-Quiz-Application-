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

def get_userDetails():
    username = str(input('Youre username ? : '))

    new_user = User(username)

    # grettings 
    print(f'Hello there  {new_user.get_name()}')

def main():
    print('Game starts')

    get_userDetails()



main()