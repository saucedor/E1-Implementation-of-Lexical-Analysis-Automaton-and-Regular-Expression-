'''
Author: César Ignacio Saucedo Rodríguez 
Date: March 20, 2025
'''

import re

def test_regex(input_string):
    """
    Checks whether the string belongs to the language defined by a regular expression.
    Rejects strings that contain certain prohibited substrings.

    Args:
    string (str): The string to check.

    Returns:
    bool: True if the string matches the pattern, False otherwise.

    """
    pattern = r'^(?!.*(?:1101|1122|1011|1012))[012]+$'
    return bool(re.fullmatch(pattern, input_string))

def main (): 
    """
    Interact with the user and test input strings.

    Args:
        None.

    Returns:
        None: Exits the program when the user inputs 'exit'.
    """
    while True:
        input_string = input("Enter a string composed of 0s, 1s, and 2s: ")
        if input_string.lower() == 'exit':
            break
        elif test_regex(input_string):
            print(f"The input string '{input_string}' belongs to the language.")
        else:
            print(f"The input string '{input_string}' does NOT belong to the language.")

# Runs the main function if the script is executed directly.
if __name__ == "__main__":
    main()
