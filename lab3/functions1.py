# Task 1: Grams to Ounces Conversion Function

def grams_to_ounces(grams):
    ounces = 28.3495231 * grams
    return ounces
print(grams_to_ounces(10))

# Task 2: Fahrenheit to Celsius Conversion Function

def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius
print(fahrenheit_to_celsius(100))

# Task 3: Chicken and Rabbits Puzzle Solver

def solve(num_heads, num_legs):
    for chickens in range(num_heads + 1):
        rabbits = num_heads - chickens
        if 2 * chickens + 4 * rabbits == num_legs:
            return chickens, rabbits
    return None, None  # In case there is no solution
print(solve(35, 94))

# Task 4: Prime Number Filter Function

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(is_prime, numbers))
print(filter_prime([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13]))

# Task 5: String Permutations Function

from itertools import permutations

def string_permutations(s):
    return [''.join(p) for p in permutations(s)]
print(string_permutations('abc'))

# Task 6: Reverse Words in String Function

def reverse_sentence(sentence):
    return ' '.join(reversed(sentence.split()))
print(reverse_sentence('We are ready'))

# Task 7: Check for Consecutive Threes

def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
# Task 8: Spy Game Function

def spy_game(nums):
    code = [0, 0, 7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)  # remove the number at index 0
    return len(code) == 1  # if only 'x' is left, the sequence was found
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))

# Task 9: Volume of a Sphere Function

from math import pi

def volume_of_sphere(radius):
    return (4/3) * pi * radius ** 3
print(volume_of_sphere(5))

# Task 10: Unique Elements Function

def unique_elements(lst):
    unique_lst = []
    for element in lst:
        if element not in unique_lst:
            unique_lst.append(element)
    return unique_lst
print(unique_elements([1,2,2,3,3,3,4,5]))

# Task 11: Palindrome Check Function

def is_palindrome(phrase):
    # Remove spaces and convert to lowercase for comparison
    clean_phrase = ''.join(phrase.split()).lower()
    return clean_phrase == clean_phrase[::-1]
print(is_palindrome('madam'))
print(is_palindrome('A man a plan a canal Panama'))

# Task 12: Histogram Printer Function

def histogram(int_list):
    for num in int_list:
        print('*' * num)
histogram([4, 9, 7])

# task 13

# def game():
#     name = input("Hello! What is your name? \n")
#     guess = 0
#     num = 0
#     gnum = random.randint(1, 20)
#     print("Well, {fname}, I am thinking of a number between 1 and 20.\nTake a guess.".format(fname = name))
#     while num != gnum:
#         num = int(input())
#         if num < gnum:
#             guess += 1
#             print("Your guess is too low.\nTake a guess.")
#         elif num > gnum:
#             guess += 1
#             print("Your guess is too big.\nTake a guess.")
#         elif guess == 3:
#             print("You're out of guesses, try again")
#         else:
#             guess +=1
#             print("Good job, {fname}! You guessed my number in {fguess} guesses!".format(fname = name, fguess = guess))
#             break
# game()
