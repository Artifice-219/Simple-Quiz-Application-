class Question:
    def __init__(self, question, question_type, difficulty, choices, correct_answer):
        self.question = question
        self.question_type = question_type
        self.difficulty = difficulty
        self.choices = choices
        self.correct_answer = correct_answer
    # methods
    def get_question(self):
        return self.question
    
    def get_choices(self):
        # most likely you are going to format this shit
        return self.choices
    
    def get_difficulty(self):
        return self.difficulty
    
    def get_type(self):
        return self.question_type
    
    def get_answer(self):
        letters = ['a','b','c','d']
        current_index = 0

        for item in self.choices:
            if(item == self.correct_answer):
                return letters[current_index]
            current_index += 1
            # TODO 18 : As this is a playsafe approach make sure this shit works


class User:
    def __init__(self, name):
        #TODO 6 : HAVE SOME DEFAULT VALUES FOR THE NAME HERE
        self.name = name
        # default values
        self.score = 0
        self.life = 3

    # setter
    def set_name(self, new_name):
        self.name = new_name
    
    def add_score(self, score_increment):
        self.score += score_increment
    
    # getters
    def get_score(self):
        return self.score
    
    def get_name(self):
        return self.name
    
    def get_life(self):
        return self.life