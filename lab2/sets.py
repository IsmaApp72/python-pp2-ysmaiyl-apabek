#task1
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
     print("Yes, apple is a fruit!") #output:Yes, apple is a fruit!
#task2
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits) #output:{'orange', 'apple', 'banana', 'cherry'}
#task3
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits) #output:{'cherry', 'orange', 'mango', 'banana', 'grapes', 'apple'}
#task4
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits) #output:{'apple', 'cherry'}
#task5
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits) #output:{'apple', 'cherry'}


    