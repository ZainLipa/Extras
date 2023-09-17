# Program of the Day: Random Quote Generator

import random

# List of inspirational quotes
quotes = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "In the middle of every difficulty lies opportunity. - Albert Einstein",
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill"
]

def generate_random_quote():
    return random.choice(quotes)

# Example usage
random_quote = generate_random_quote()
print("Random Quote of the Day:")
print(random_quote)
