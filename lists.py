names = ["John", "Bob", "Sam", "Mary"]
names[0] = 'john'
print(names[0])

#prints first three list values
print(names[0:3]) 
print(names) # doesn't change original value

numbers = [1,2,3,4,5]
numbers.append(6)
print(numbers)
numbers.insert(5,20)
print(numbers)
print(1 in numbers) # True
print(len(numbers)) # 7


for item in numbers:
    print(item)


numbers = range(5)
for number in numbers:
    print(number) # 0 1 2 3 4



for number in range(5,10,2):
    print(number)