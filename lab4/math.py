# Task 1: Convert degree to radian with print output
import math
def task1_degree_to_radian(degree):
    radian = math.radians(degree)
    print(f"Input degree: {degree}\nOutput radian: {radian}")

# Task 2: Calculate the area of a trapezoid with print output
def task2_trapezoid_area(base1, base2, height):
    area = ((base1 + base2) / 2) * height
    print(f"Height: {height}\nBase, first value: {base1}\nBase, second value: {base2}\nExpected Output: {area}")

# Task 3: Calculate the area of a regular polygon with print output
def task3_polygon_area(sides, length):
    area = (sides * (length ** 2)) / (4 * math.tan(math.pi / sides))
    print(f"Input number of sides: {sides}\nInput the length of a side: {length}\nThe area of the polygon is: {area}")

# Task 4: Calculate the area of a parallelogram with print output
def task4_parallelogram_area(base, height):
    area = base * height
    print(f"Length of base: {base}\nHeight of parallelogram: {height}\nExpected Output: {area}")

# Execute tasks with print statements
task1_degree_to_radian(15)
task2_trapezoid_area(5, 6, 5)
task3_polygon_area(4, 25)
task4_parallelogram_area(5, 6)

