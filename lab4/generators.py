def generate_squares(N):
    """Generator that yields the squares of numbers up to N."""
    for number in range(1, N + 1):
        yield number ** 2

def even_numbers(n):
    """Generator that yields even numbers up to n."""
    for number in range(n + 1):
        if number % 2 == 0:
            yield number

def divisible_by_3_and_4(n):
    """Generator that yields numbers divisible by 3 and 4 up to n."""
    for number in range(n + 1):
        if number % 3 == 0 and number % 4 == 0:
            yield number

def squares(a, b):
    """Generator that yields the squares of numbers from a to b."""
    for number in range(a, b + 1):
        yield number ** 2

def countdown(n):
    """Generator that counts down from n to 0."""
    while n >= 0:
        yield n
        n -= 1

# Task 1: Test generate_squares
N_squares = 5
print(f"Squares up to {N_squares}:")
for square in generate_squares(N_squares):
    print(square)

# Task 2: Get input from the user and print even numbers
n_input = int(input("Enter the number N for even numbers: "))
print(', '.join(str(num) for num in even_numbers(n_input)))

# Task 3: Test divisible_by_3_and_4
N_divisible = 12
print(f"Numbers divisible by 3 and 4 up to {N_divisible}:")
for number in divisible_by_3_and_4(N_divisible):
    print(number)

# Task 4: Testing the squares generator
a, b = 1, 5
print(f"Squares from {a} to {b}:")
for square in squares(a, b):
    print(square)

# Task 5: Testing the countdown generator
countdown_start = 10
print(f"Countdown from {countdown_start} to 0:")
for number in countdown(countdown_start):
    print(number)
