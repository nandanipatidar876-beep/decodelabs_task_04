# Project 4: General Knowledge Quiz
# Created by: Nandani Patidar

print("=================================")
print("     GENERAL KNOWLEDGE QUIZ")
print("=================================")

score = 0

# Question 1
answer1 = input("1. What is the capital of France? ").strip().lower()

if answer1 == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Paris.")

# Question 2
answer2 = input("\n2. Which planet is known as the Red Planet? ").strip().lower()

if answer2 == "mars":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is Mars.")

# Question 3
answer3 = input("\n3. How many continents are there in the world? ").strip()

if answer3 == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong! The correct answer is 7.")

# Final Score
print("\n=================================")
print("Quiz Completed!")
print("Your Final Score:", score, "/ 3")
print("=================================")

# Performance Message
if score == 3:
    print("Excellent! You got all answers correct.")
elif score == 2:
    print("Good job! You scored 2 out of 3.")
elif score == 1:
    print("Keep practicing! You scored 1 out of 3.")
else:
    print("Better luck next time!")