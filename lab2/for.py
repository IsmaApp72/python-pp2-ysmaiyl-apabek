#task1
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x) #output:apple,banana,cherry
#task2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x) #output:apple,cherry
#task3
for x in range(6):
    print(x) #output:0,1,2,3,4,5
#task4
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x) #output:apple
