# Program of the Day: Word Frequency Counter

def count_word_frequency(text):
    # Convert text to lowercase and split it into words
    words = text.lower().split()

    # Create a dictionary to store word frequencies
    word_count = {}

    for word in words:
        # Remove punctuation marks
        word = word.strip(".,!?;:\"")
        
        # If the word is not empty, update its count in the dictionary
        if word:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

    return word_count

# Example usage
text = "This is a sample text. Sample text is used to demonstrate word frequency counting."
word_frequency = count_word_frequency(text)

print("Word Frequency:")
for word, count in word_frequency.items():
    print(f"{word}: {count}")
