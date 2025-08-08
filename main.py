print("-- Welcome to Python Quiz Game --")
print("You'll be given a few questions with four options each.")
print("Your score will be tracked accordingly.")

while True:
    play = input("Press Enter to play the game or type 'q' to exit: ")

    if play.lower() == "q":
        print("Thanks for playing! Goodbye.")
        break

    questions = (
        "Who Developed Python?",
        "What is the capital city of Nepal?",
        "Who is the Prime Minister of Nepal?")

    options = (
        ("A. Biraj Chhetri", "B. Guido Van Rossum", "C. Albert Einstein", "D. None"),
        ("A. Kathmandu", "B. New Delhi", "C. Islamabad", "D. London"),
        ("A. KP Oli", "B. Balen Shah", "C. Harka Sampang Rai", "D. Anmol KC") )
    
    answers = ("B", "A", "A")
    score = 0

    for i in range(len(questions)):
        print(f"Q{i+1}. {questions[i]}")
        for option in options[i]:
            print(option)

        player_answer = input("Enter your choice (A, B, C, D): ").upper()

        if player_answer == answers[i]:
            print(f"Congrats, your option {player_answer} was correct!")
            score += 1
        else:
            print(f"Wrong answer! The correct answer is {answers[i]}.")

    print(f"You scored {score} out of {len(questions)}.")

    again = input("Do you want to play again? (y/n): ").lower()
    if again != "y":
        print("Thanks for playing! See you next time.")
        break

