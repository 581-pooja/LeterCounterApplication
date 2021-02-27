print("==============================================================")
print("Welcome to the letter Counter Application:\n")
name  = input("What is Your name: ").title().strip()
print("Hello " + name + "!")
print("I will count the number of times that a specific letter occurs in a message.\n")
msg = input("Please enter a message: ")
msg = msg.lower()

letter = input("which letter would you like to count the occurrence of: ")
letter = letter.lower()
letter_count = msg.count(letter)
print(name, ",your message has",str(letter_count) + " " + letter + "'s in it.")
print("==============================================================")


name = "              pooja Bhagat"
print(name.strip())
# Strip: It removes the whitespaces from the input in the beginning

name = "pooja bhagat"
print(name.title())
# Title: words start with uppercased characters and all remaining cased characters have lower case.



# Casting
# print(str(4) + "gh")
# print(float(4))
# print(bool(1))
# print(bool(5))
# print(bool(0))
# print(int("5") + 78)

