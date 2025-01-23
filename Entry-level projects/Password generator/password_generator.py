import random
import string

#get letters, digits, special chars
def generate_password(min_Length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    #create string containing different characters
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    #Set empty password, meet no criteria, no values
    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    #generate new_char by randomly selecting characters, add to pwd
    while not meets_criteria or len(pwd) < min_Length:
        new_char = random.choice(characters)
        pwd += new_char

        #determine if char is number / special char
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

    
        meets_criteria = True
        if numbers:
            meets_criteria = meets_criteria and has_number #If should include number, but no number, meet criteria false
        if special_characters:
            meets_criteria = meets_criteria and has_special #false if 1 of 2 things not met

    return pwd

#Generate user input
min_length = int(input("Enter minimum length: "))
has_numbers = input("Do you require numbers (y/n)? ").lower() == "y"
has_special = input("Do you require Special characters (y/n)? ").lower() == "y"
pwd = generate_password(min_length, has_numbers, has_special)
print("The generated password is:", pwd)

