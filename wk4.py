# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
# Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
try:
    filename = input("Enter the file name to read:(file.txt, home.txt or about.txt) ")
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print("\nyour Original file Content\n", content)
        modified_content = content.upper()
        with open('modified content.txt', 'w', encoding='utf-8') as new_file:
            new_file.write(modified_content)
        #Modified content written to 'modified content.txt
        # Show the modified content to the user
        print("\n\n\nModified Content:\n", modified_content)
except FileNotFoundError:
    print(f"Error: The file '{filename}' does not exist.")
except IOError:
    print(f"Error: Could not read the file '{filename}'.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")