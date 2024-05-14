class Course:
    def __init__(self, name):
        self.progress_bar = 0
        self.name = name
        self.questions = None
        self.answers = None

    def course_name(self):
        print(self.name)
