#task1
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model")) #output:Mustang
#task2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"]=2020
print(car) #output:{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}
#task3
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"]="red"
print(car) #output:{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}
#task4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car) #output:{'brand': 'Ford', 'year': 1964}
#task5
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car) #output:{}

