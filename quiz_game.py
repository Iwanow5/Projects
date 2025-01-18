# different levels of difficulty, easy, hard
# 5 questions per level
# 4 options per question
# Really easy to add/remove/edit questions/difficulty
# function to randomise the questions

import random #for randomising the questions

easy_quiz_data = [
    {
        "question": "How many days is there in July?",
        "options": ["A. 30", "B. 31", "C. 28", "D. 29"],
        "answer": "B",
    },

    {
        "question": "What is the capital of Australia?",
        "options": ["A. Sydney", "B. Melbourne", "C. Dublin", "D. Perth"],
        "answer": "A",
    },

    {
        "question": "How many letters are there in the English alphabet?",
        "options": ["A. 26", "B. 30", "C. 50", "D. 20"],
        "answer": "A",
    },

    {
        "question": "What is the largest planet in our solar system?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "C",
    },

    {
        "question": "How many continents are there in the world?",
        "options": ["A. 23", "B. 14", "C. 7", "D. 4"],
        "answer": "C",
    }
]

hard_quiz_data = [
    {
        "question": "When was the first computer invented?",
        "options": ["A. 1973", "B. 1984", "C. 1942", "D. 1945"],
        "answer": "D",
    },

    {
        "question": "From what material is the Statue of Liberty made?",
        "options": ["A. Bronze", "B. Copper", "C. Steel", "D. Gold"],
        "answer": "A",
    },

    {
        "question": "From what is the japanese alcoholic drink sake made from?",
        "options": ["A. Rice", "B. Wheat", "C. Corn", "D. grapes"],
        "answer": "A",
    },

    {
        "question": "How many brains does an octopus have?",
        "options": ["A. 10", "B. 9", "C. 8", "D. 6"],
        "answer": "B",
    },

    {
        "question": "What is the main language spoken in Brazil?",
        "options": ["A. Portuguese", "B. Spanish", "C. English", "D. Brazillian"],
        "answer": "A",
    },
]

def start_quiz():
    quiz_data = select_difficulty()
    do_quiz(quiz_data)

def select_difficulty():
    difficulty = input("Please select a difficulty level (easy/hard): ")
    if difficulty.lower() == "easy":
        return easy_quiz_data
    elif difficulty.lower() == "hard":
        return hard_quiz_data
    else:
        print("Invalid difficulty level. Please type either 'easy' or 'hard'.")
        return select_difficulty()

def do_quiz(questions):
    random.shuffle(questions)

    final_score = 0
    question_number = 1
    for question in questions:
        print(f"Question {question_number}. {question['question']}")
        
        for option in question["options"]:
            print(option)
        answer = input("Enter only one answer (A, B, C, or D): ").upper()
        
        if answer == question["answer"]:
            print("Correct!\n")
            final_score += 1
        
        else:
            print("Incorrect!, the correct answer was: ", question["answer"], "\n")

    print("Quiz complete!")
    print("Your final score is: ", final_score, "out of", len(questions))
    
    if final_score == len(questions):
        print("Congratulations! You got a perfect score!")
    elif final_score >= len(questions) / 2:
        print("Well done! You got a good score")
    else:
        print("Better luck next time :(")

start_quiz()