# Function to calculate the Fibonacci sequence
def fibonacci(n):
    # Initialize the first two terms of the sequence
    a = 0
    b = 1
    
    # Print the first two terms of the sequence
    print(a)
    print(b)
    
    # Loop through the remaining terms of the sequence
    for i in range(2, n):
        # Calculate the next term of the sequence
        c = a + b
        
        # Print the next term of the sequence
        print(c)
        
        # Update the values of a and b for the next iteration
        a = b
        b = c

# Get user input for the number of terms in the sequence
n = int(input("Enter the number of terms: "))

# Call the fibonacci function with the user input
fibonacci(n)
