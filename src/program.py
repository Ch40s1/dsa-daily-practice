from dsa import DSA_Course


class Program:
    def __init__(self):
        # sets current program
        self.current_course = None
        # list of available programs
        self.courses = {
            "dsa": self.dsa_program,
            "test": self.test_programs,
            "test2": self.test_programs2,
        }
        self.user_program()

    def user_program(self):
        print("HELOOOOOOO! Welcome")
        for course in self.courses:
            print(course)
        prompt_program = input("what course?\n").lower()
        self.current_course = prompt_program
        self.program_init()

    def program_init(self):
        if self.current_course in self.courses:
            self.courses[self.current_course]()
        else:
            print("No active programs")

    def dsa_program(self):
        print("dsa program active")
        dsa_course = DSA_Course()
        dsa_course.course_name()
        print(f"Progress bar: {dsa_course.progress_bar}")

    def test_programs(self):
        print("test function")

    def test_programs2(self):
        print("test function2")
