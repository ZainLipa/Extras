# Program of the Day: Palindrome Checker

def is_palindrome(word):
    # Remove spaces and convert to lowercase for accurate palindrome check
    word = word.replace(" ", "").lower()
    return word == word[::-1]

# Example usage
word = "racecar"
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
