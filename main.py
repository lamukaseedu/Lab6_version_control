'''
    Name: Lam Nguyen
    Partner: Arossa Adhikary
    Due Date: 10/31/23
    Lab 6: Version Control
'''


# Encodes an inputted password by shifting each digit up by 3 numbers.
def encode(password):
    separated_string = []
    # Each element in the password appended to a list and then shifted up by 3 numbers
    for i in password:
        separated_string.append(int(i))
        separated_string[-1] += 3
        # If the element is greater than 9 after the shifting, it will subtract it by 10 to simulate
        # going back around to the start, or starting back at 0.
        if separated_string[-1] > 9:
            separated_string[-1] -= 10

    encoded_password = ''
    # All the separated elements in the list are then put back into a string.
    for i in separated_string:
        encoded_password += str(i)

    return encoded_password


def main():
    # Code will keep going until the user exits.
    while True:
        # Prints the menu and asks the user to enter an option.
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        menu_option = int(input("Please enter an option: "))

        # If menu option 1 is selected, it will ask for a password to encode,
        # then it will encode the password and store the encoded password.
        if menu_option == 1:
            password = input("\nPlease enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        # If menu option 2 is selected, it will decode the stored encoded password and print it.
        elif menu_option == 2:
            print(f"The encoded password is {encoded_password},", end='')
            print(f"and the original password is {decode(encoded_password)}.")
        # Exits the program when menu option 3 is inputted.
        elif menu_option == 3:
            break


if __name__ == '__main__':
    main()
