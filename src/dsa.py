from course import Course


class DSA_Course(Course):
    def __init__(self):
        super().__init__(name="Data Structures and Algorithms")
        self.progress_bar = 50
