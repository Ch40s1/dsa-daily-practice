from questions import quiz_questions


def main():

    def run_course():
        while True:
            user_program()

    def user_program():
        user_answer = None
        print("HELOOOOOOO! Welcome")
        for q_id, q_info in quiz_questions.items():
            print(f"questions {q_id}: {q_info['question']}")
            correct_answer = q_info["correct_answer"]
            for option, answer in q_info['options'].items():
                print(f"  {option}) {answer}")
            user_answer = input("Choose answer: ").lower()
            if user_answer == correct_answer:
                print("Correct!")
                continue
            else:
                print("Incorrect")
                print(f"correct answer was: {correct_answer}")
                continue
        prompt_program = input("Type 'exit' to exit?\n").lower()
        if prompt_program == "exit":
            print("exiting program")
            exit()

    run_course()


if __name__ == "__main__":
    main()
