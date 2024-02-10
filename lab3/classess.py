# Task 1: A class with getString and printString methods
class InputOutputString:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Enter a string: ")

    def printString(self):
        print(self.s.upper())
io_string = InputOutputString()
io_string.getString()
io_string.printString()

# Task 2: Shape and Square classes
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2
square = Square(3)
print(square.area())

# Task 3: Rectangle class inheriting from Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
rectangle = Rectangle(2, 4)
print(rectangle.area())

# Task 4: Point class with show, move, and dist methods
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        return f"Point coordinates: ({self.x}, {self.y})"

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
point1 = Point(0, 0)
point2 = Point(3, 4)
print(point1.show())
point1.move(1, 1)
print(point1.dist(point2))

# Task 5: BankAccount class
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} made. New balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Withdrawal denied. Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} made. New balance is {self.balance}")

    def __str__(self):
        return f"BankAccount(owner='{self.owner}', balance={self.balance})"
account = BankAccount('John Doe', 100)
account.deposit(50)
account.withdraw(25)
print(account)

# Task 6: Filter prime numbers from a list
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
prime_numbers_filter = lambda numbers: list(filter(is_prime, numbers))
numbers = [10, 15, 3, 7, 29, 42]
print(prime_numbers_filter(numbers))