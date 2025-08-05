# Create a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
# Perform the operation based on the user's input and print the result.
# Example: If a user inputs 10, 5, and +, your program should display 10 + 5 = 15.
F_num = float(input("enter number A: "))
S_num = float(input("enter number B: "))
operator = input("Enter the operation (+, -, *, /): ")

# mathematical operations
if operator == '+':
	addition = F_num + S_num
	print(f"{F_num} + {S_num} = {addition}")
elif operator == '-':
	subtraction = F_num - S_num
	print(f"{F_num} - {S_num} = {subtraction}")
elif operator == '*':
	multiplication = F_num * S_num
	print(f"{F_num} * {S_num} = {multiplication}")
elif operator == '/':
	if S_num != 0:
		division = F_num / S_num
		print(f"{F_num} / {S_num} = {division}")
	else:
		print("Error: Division by zero is not allowed.")
else:
	print("Please enter the appropriate operator between (*, +, /, -)")
