# Input a single alphabet from the user
alphabet = input("Enter a single alphabet: ").lower()  # Convert input to lowercase for case insensitivity

# Check if the input is a single character
if len(alphabet) == 1:
    # Check if the input is a vowel
    if alphabet in 'aeiou':
        print(f"{alphabet} is a vowel.")
    else:
        print(f"{alphabet} is a consonant.")
else:
    print("Please enter a single alphabet.")
