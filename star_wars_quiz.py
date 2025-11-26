import random, json, os, sys
os.system('colour') # FOR WINDOWS TO ENABLE ANSI COLORS BECAUSE WINDOWS IS STUPID
BASE = os.path.join(os.path.dirname(sys.argv[0]))
QUESTIONS_FILE = os.path.join(BASE, 'questions.json')
# QUESTIONS_FILE = os.path.join(os.path.dirname(__file__), 'questions.json') # ALTERNATIVE METHOD IF YOU DONT USE WINDOWS

def pick_difficulty():
    choices = {
        '1': 'easy',
        '2': 'medium',
        '3': 'absolute nerd',
        '4': 'all questions'
    }
    if len(sys.argv) > 1:
        if sys.argv[1] in choices:
                return choices[sys.argv[1]]
        elif sys.argv[1].lower() in choices.values():
            return sys.argv[1].lower()
        elif 'hard' in sys.argv[1].lower():
            return choices['3']
        elif 'all' in sys.argv[1].lower():
            return choices['4']
        else:
            print(f'Invalid difficulty level provided as argument.')
            sys.exit(1)
    else:
        prompt = ("Select a difficulty level:\n"
                    "1. Easy\n"
                    "2. Medium\n"
                    "3. Absolute nerd\n"
                    "4. Do ALL the questions\n"
                    "Enter your choice: ")
        while True:
            choice = input(prompt).strip()
            if choice in choices:
                return choices[choice]
            else:
                print(f"Invalid choice. Please select a valid difficulty level.")
            worded = choice.lower()
            if worded in choices.values():
                return worded
            else:
                print("Invalid choice. Please select a valid difficulty level.")

def load_questions(difficulty: str):
    try:
        with open(QUESTIONS_FILE, 'r', encoding='utf-8') as f:
            questions = json.load(f)
    except FileNotFoundError:
        print(f"Error: Questions file '{QUESTIONS_FILE}' not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: Questions file '{QUESTIONS_FILE}' is not a valid JSON.")
        sys.exit(1)
    if difficulty.lower() == 'all questions':
        filtered_questions = questions
    else:
        filtered_questions = [q for q in questions if q.get('category', '').lower() == difficulty.lower()]
    if not filtered_questions:
        print(f"No questions available for difficulty level '{difficulty}'.")
        print(f'Choosing all questions instead.')
        filtered_questions = questions
    return filtered_questions

def run_quiz(questions):
    score = 0
    random.shuffle(questions)
    running = True
    BACKGROUND_GREEN = '\033[42m'
    BACKGROUND_RED = '\033[41m'
    RESET = '\033[0m'
    for q in questions:
        print(f'-'*32)
        print(f'Question number: {questions.index(q)+1}/{len(questions)}')
        print(f'-'*32)
        print(f"{q['question']}")
        print(f'-'*32)
        choices = q.get('choices', q.get('options', []))
        for idx, option in enumerate(choices, start=1):
            print(f"{idx}. {option}")
            print(f'-'*32)
        while running:
            try:
                user_input = input('Your answer (enter the option number or "q" to quit): ').strip()
                if user_input.lower() == 'q':
                    print(f'Quiz terminated early.')
                    running = False
                    break
                answer = int(user_input)
                if 1 <= answer <= len(choices):
                    break
                else:
                    print('Invalid option. Please enter a valid option number.')
            except ValueError:
                print(f'Please enter a valid integer or "q" to quit')
        
        if not running:
            break
                
        correct_index = q.get('correct_index', 0)
        if answer - 1 == correct_index:
            print(f'{BACKGROUND_GREEN}Correct!{RESET}')
            score += 1
        else:
            correct_answer = choices[correct_index] if 0 <= correct_index < len(choices) else 'unknown'
            print(f'{BACKGROUND_RED}Wrong!{RESET}\nThe correct answer was: {correct_answer}')
    if questions.index(q) == 19:
        print(f'Quiz completed! Your total score is {score} out of {len(questions)}.')
    else:
        print(f'So far your score was {score} out of {questions.index(q)} answered.')
        print(f'You had {len(questions) - questions.index(q)} questions remaining.')                                                                                      

        

def main():
    difficulty = pick_difficulty()
    questions = load_questions(difficulty)
    run_quiz(questions)



if __name__ == "__main__":
    main()
