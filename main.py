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
    
    def print_choices(self):
        # most likely you are going to format this shit
        return self.choices
    
    def get_difficulty(self):
        return self.difficulty
    
    def get_type(self):
        return self.question_type
    
    def get_answer(self):
        return self.correct_answer