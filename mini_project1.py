def run_quiz():
    questions = [
        {
            "question": "Which language is primarily used for data analysis?",
            "options": ["A) Python", "B) HTML", "C) CSS", "D) JavaScript"],
            "answer": "A"
        },
        {
            "question": "What does SQL stand for?",
            "options": ["A) Structured Query Language", "B) Simple Question Logic", "C) Sequential Query List", "D) Standard Query Link"],
            "answer": "A"
        },
        {
            "question": "Which chart is best for showing parts of a whole?",
            "options": ["A) Line Chart", "B) Pie Chart", "C) Scatter Plot", "D) Histogram"],
            "answer": "B"
        },
        {
            "question": "What is the primary purpose of data visualization?",
            "options": ["A) Store data", "B) Analyze raw numbers", "C) Present insights clearly", "D) Delete old data"],
            "answer": "C"
        }
    ]

    score = 0

    for index, q in enumerate(questions):
        print(f"\nQ{index + 1}: {q['question']}")
        for option in q['options']:
            print(option)
        
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        if user_answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}) {q['options'][ord(q['answer']) - 65][3:]}")

    print(f"\nYour final score is {score}/{len(questions)}")

if __name__ == "__main__":
    run_quiz()