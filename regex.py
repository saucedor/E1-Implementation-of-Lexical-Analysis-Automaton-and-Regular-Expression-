'''
Author: César Ignacio Saucedo Rodríguez 
Date: March 20, 2025
'''

def test_regex(input_string):
    """
    Checks if the string belongs to the defined language (without using automata).

    Language rules:
    - Can only contain 0s, 1s, and 2s.
    - Cannot have the following substrings: '1101', '1122', '1011', '1012'
    """
    if len(input_string) == 0:
        return False
    
    for c in input_string:
        if c not in {'0', '1', '2'}:
            return False

    invalid_sequences = ['1101', '1122', '1011', '1012']
    for seq in invalid_sequences:
        if seq in input_string:
            return False

    return True

def main():
    """
    Interact with the user and test input strings.

    The user can input strings one by one.
    Typing 'exit' will stop the program.
    """
    while True:
        input_string = input("Enter a string (only 0s, 1s, and 2s — type 'exit' to quit): ")
        if input_string.lower() == 'exit':
            break
        if test_regex(input_string):
            print(f"The input string '{input_string}' belongs to the language.")
        else:
            print(f"The input string '{input_string}' does NOT belong to the language.")

if __name__ == "__main__":
    main()
