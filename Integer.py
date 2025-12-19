# Integer (int) is most commonly used for whole numbers, where you don’t need fractions or decimals.
# Integer are commonly used for:
# 1. Counting / Numbering
# 2. Whole number math
# 3. Whole number input
# 4. Condition / Logic

# Example

print("Welcome to quiz counter program\n")

student_name = input("Please input the name of the student: ")

total_questions = int(
    input("Please input how many questions are in the quiz: "))

correct_answers = int(input(f"How many did {student_name} answer correctly: "))

wrong_answer = total_questions - correct_answers

score_percentage = (correct_answers * 100) // total_questions

print(f"\n{student_name} answered \n{wrong_answer} questions incorrectly & {correct_answers} questions correctly\n")
print(f"{student_name}'s score is {score_percentage}%\n")
if score_percentage > 75:
    print(f"{student_name} has PASSED the quiz")

else:
    print(f"{student_name} has FAILED the quiz")
