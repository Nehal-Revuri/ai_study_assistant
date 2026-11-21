def show_menu():
	print("""

[AI STUDY ASSISTANT]

1. Manage study questions
2. Ask AI a question
3. Generate practice questions
4. View learning progress
5. Exit

""")

def main():
	while True:
		show_menu()
		user_input = input("Please select an option: ")

		if user_input == "1" or user_input == "4":
			print("""
feature not implemented yet
""")
		elif user_input == "5":
			print("""

Please come back soon!
""")
			break
		elif user_input == "2" or user_input == "3":
			print("""

Error
""")
		else:
			print("""

Please select a valid option from the menu above
""")

if __name__ == "__main__":
	main()


