# Task 1: Matches a string that has an 'a' followed by zero or more 'b's
def task1(text):
    return bool(re.match(r'ab*', text))

# Task 2: Matches a string that has an 'a' followed by two to three 'b'
def task2(text):
    return bool(re.match(r'ab{2,3}', text))

# Task 3: Find sequences of lowercase letters joined with an underscore
def task3(text):
    return re.findall(r'[a-z]+_[a-z]+', text)

# Task 4: Find sequences of one uppercase letter followed by lowercase letters
def task4(text):
    return re.findall(r'[A-Z][a-z]+', text)

# Task 5: Matches a string that has an 'a' followed by anything, ending in 'b'
def task5(text):
    return bool(re.match(r'a.*b$', text))

# Task 6: Replace spaces, commas, or dots with a colon
def task6(text):
    return re.sub(r'[ ,.]', ':', text)

# Task 7: Convert snake case string to camel case string
def task7(text):
    return ''.join(x.capitalize() or '_' for x in text.split('_'))

# Task 8: Split a string at uppercase letters
def task8(text):
    return re.findall(r'[A-Z][^A-Z]*', text)

# Task 9: Insert spaces between words starting with capital letters
def task9(text):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', text)

# Task 10: Convert camel case string to snake case
def task10(text):
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', text).lower()

def print_regex_exercises():
    print("Task 1:", task1("ab"))
    print("Task 2:", task2("abb"))
    print("Task 3:", task3("my_variable_name"))
    print("Task 4:", task4("HelloWorld"))
    print("Task 5:", task5("acccb"))
    print("Task 6:", task6("hello, world. How are you?"))
    print("Task 7:", task7("my_variable_name"))
    print("Task 8:", task8("SplitCamelCase"))
    print("Task 9:", task9("ThisIsCamelCased"))
    print("Task 10:", task10("ThisIsCamelCased"))

print_regex_exercises()
