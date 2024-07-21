# 1. The Range Riddle
# Task 1: Every Other Day
days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
for i in range(len(days_of_week)):
    if i % 2 == 0:
        print(days_of_week[i])

# 2. Loop Condition Logic
# Task 1: Loop Condition Exploration
while True:  # Infinite loop for demonstration
    answer = input("Do you want to stop? (yes/no): ")
    if answer.lower() == "yes":
        break
    print("The loop continues...")

# Task 2: Conditional Exit
iteration = 0
while iteration < 5:
    print(f"Iteration {iteration + 1}")
    iteration += 1

# 3. Python's Random Game Night (Extra Credit)
# Task 1: Random Choice Game
import random

items = ["apple", "banana", "cherry", "date", "fig"]
selected_item = random.choice(items)

print("Guess the selected item from the list:", items)

while True:
    guess = input("Enter your guess: ")
    if guess == selected_item:
        print("Congratulations! You guessed correctly.")
        break
    else:
        print("Wrong guess. Try again!")
