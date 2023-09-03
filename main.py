# Function to generate Fibonacci sequence up to n numbers
def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]  # Initialize the sequence with the first two Fibonacci numbers

    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence

# Get user input for the number of Fibonacci numbers to generate
n = int(input("Enter the number of Fibonacci numbers to generate: "))

# Generate and print the Fibonacci sequence
fibonacci_numbers = generate_fibonacci(n)
print("Fibonacci Sequence (first", n, "numbers):")
print(fibonacci_numbers)
