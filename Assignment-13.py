def is_palindrome(s):
    # Remove any non-alphanumeric characters and convert to lowercase
    cleaned_string = ''.join(filter(str.isalnum, s)).lower()
    # Check if the cleaned string is the same forward and backward
    return cleaned_string == cleaned_string[::-1]

# Prompt the user to enter a string
input_string = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')
