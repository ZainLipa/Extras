# Program of the Day: File Word Counter

def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            word_count = len(content.split())
            return word_count
    except FileNotFoundError:
        return "File not found. Please provide a valid file path."

# Example usage: Count words in a text file
file_path = "sample_text.txt"  # Replace with the path to your text file
result = count_words_in_file(file_path)
print(f"The number of words in the file is: {result}")
