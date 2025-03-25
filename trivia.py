trivia = [
    {
        "questions": "What Country is Paris located in?",
        "options": ["United Kingdom", "United States", "Germany", "France"],
        "answer": "France"
    },
    {
        "questions": "What is the capital of Romania?",
        "options": ["Bucharest", "Sibiu", "Dej", "Oradea"],
        "answer": "Bucharest"
    },
    {
        "questions": "What continent is Ghana located in?",
        "options": ["North America", "South America", "Asia", "Africa"],
        "answer": "Africa"
    },
    {
        "questions": "What country does France share its longest land border with?",
        "options": ["United States", "Germany", "Brazil", "Africa"],
        "answer": "Africa"
    },
    {
        "questions": "What is considered the country that never gets dark?",
        "options": ["Norway", "Sweden", "Poland", "Finland"],
        "answer": "Finland"
    },
    {
        "questions": "What is a city in Brazil?",
        "options": ["Salvador", "Puebla", "Monterrey", "Bilbao"],
        "answer": "Salvador"
    }
]

###This function was made by Kush Vapiwala
def run_trivia(trivia):
    score = 0
    for q in trivia:
        print(q["questions"])
        for i, option in enumerate(q["options"]):
            print(f"{i+1}. {option}")
        answer = int(input("Enter your guess(1-4): ")) - 1
        correct_answer = q["options"][answer]
        if correct_answer == q["answer"]:
            print("Correct!")
            score += 1
        else: 
            print("Incorrect!")
    print(f"Your final score was {score} points Good job!")

run_trivia(trivia)
