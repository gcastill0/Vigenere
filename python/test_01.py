def print_uppercase_letters():
    """
    This function iterates through the ASCII values of uppercase English letters
    and prints each letter to the standard output.
    """
    for letter in range(ord('A'), ord('Z') + 1):
        print(chr(letter))

def main():
    """
    Main function to execute the print_uppercase_letters function.
    """
    print_uppercase_letters()

if __name__ == "__main__":
    main()