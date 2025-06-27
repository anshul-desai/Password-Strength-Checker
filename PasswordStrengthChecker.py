import string

password = input("Enter your password: ")

length = True
lower = True
upper = True
digit = True
special = True

if len(password) < 8:
    length = False

if not any(char.islower() for char in password):
    lower = False

if not any(char.isupper() for char in password):
    upper = False

if not any(char.isdigit() for char in password):
    digit = False

if not any(char in string.punctuation for char in password):
    special = False

if length == True and lower == True and upper == True and digit == True and special == True:
    print("Your password is strong!")
else:
    final = "Your password needs"
    if length == False:
        final = final + " to be longer,"
    if lower == False:
        final = final + " at least one lowercase letter,"
    if upper == False:
        final = final + " at least one uppercase letter,"
    if digit == False:
        final = final + " at least one digit,"
    if special == False:
        final = final + " at least one special character,"
    print(final)
