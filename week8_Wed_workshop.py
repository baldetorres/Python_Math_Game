import random

record = {}
record["counter"] = 0
record["correct"] = 0
record["incorrect"] = 0

incorrect_problems = []
user_answers = []
true_answers = []


def create_math_program():
    play_math_round()
    generate_summary_report()


def play_math_round():
    problem, solution = generate_random_math_problem()
    present_problem_to_user(problem)
    user_guess = accept_user_answer()
    result = evaluate_user_guess(user_guess, solution)
    continue_or_stop_program()


def generate_random_math_problem():
    number_1 = random.randint(0, 10)
    number_2 = random.randint(0, 10)
    list_operations = ["+", "-", "*"]
    rand_operation = random.choice(list_operations)
    answer = 0
    if rand_operation == "+":
        answer = number_1 + number_2
    elif rand_operation == "-":
        answer = number_1 - number_2
    elif rand_operation == "*":
        answer = number_1 * number_2
    rand_problem = "{} {} {} = ?".format(number_1, rand_operation, number_2)
    store_problem = "{} {} {}".format(number_1, rand_operation, number_2)
    incorrect_problems.append(store_problem)
    true_answers.append(answer)
    return rand_problem, answer


def present_problem_to_user(problem):
    print problem


def accept_user_answer():
    user_answer = int(raw_input("Please enter your answer: "))
    user_answers.append(user_answer)
    return user_answer


def evaluate_user_guess(user_answer, real_answer):
    evaluation = ""
    counter = record["counter"] + 1
    record["counter"] = counter

    if user_answer == real_answer:
        evaluation = "Correct"
        counterCorrect = record["correct"] + 1
        record["correct"] = counterCorrect
        incorrect_problems.pop()
        user_answers.pop()
        true_answers.pop()
    else:
        evaluation = "Incorrect"
        counterIncorrect = record["incorrect"] + 1
        record["incorrect"] = counterIncorrect
        incorrect_problems[-1] = "{} = {} ({})".format(incorrect_problems[-1], user_answers[-1], true_answers[-1])
    print evaluation
    return evaluation


def continue_or_stop_program():
    decision = raw_input("Do you wish to solve additional problems?")
    if decision in ("yes", "Yes", "y", "Y"):
        play_math_round()
    elif decision in ("no", "No", "n", "N", ""):
        print "Goodbye"
    else:
        print "Incorrect input"
        continue_or_stop_program()


def generate_summary_report():
    print "List of problems answered wrong(if any)"
    for question in incorrect_problems:
        print question

    correct = record["correct"]
    total = record["counter"]
    success_rate = int((float(correct) / total) * 100)

    print "You have answered correctly {} out of {} problems ({}%)".format(correct, total, success_rate)


create_math_program()