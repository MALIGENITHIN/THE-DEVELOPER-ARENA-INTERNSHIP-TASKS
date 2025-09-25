# Python Quiz App

def run_quiz(questions):
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}. {q['question']}")
        for option in q['options']:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        
        if answer == q['answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer is {q['answer']}")
    
    print("\n🎯 Quiz Completed!")
    print(f"Your final score: {score}/{len(questions)}")
    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.2f}%")

# Python Basic Questions
questions = [
    {
        "question": "Which of the following is the correct file extension for Python files?",
        "options": ["A. .pyth", "B. .pt", "C. .py", "D. .p"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. def", "C. fun", "D. define"],
        "answer": "B"
    },
    {
        "question": "Which data type is used to store True/False values?",
        "options": ["A. int", "B. str", "C. bool", "D. float"],
        "answer": "C"
    },
    {
        "question": "What is the output of: print(2 ** 3)?",
        "options": ["A. 6", "B. 8", "C. 9", "D. 12"],
        "answer": "B"
    },
    {
        "question": "Which of the following is NOT a Python data type?",
        "options": ["A. list", "B. tuple", "C. array", "D. dictionary"],
        "answer": "C"
    }
]

# Run the quiz
run_quiz(questions)
