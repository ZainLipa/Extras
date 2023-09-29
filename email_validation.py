# Program of the Day: Email Validation

import re

def is_valid_email(email):
    # Regular expression for a basic email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    if re.match(pattern, email):
        return True
    else:
        return False

# Example usage
email = input("Enter an email address: ")

if is_valid_email(email):
    print("Valid email address.")
else:
    print("Invalid email address.")
