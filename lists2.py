names = ['James','John','Simon','Mary','Faye']
print(names[2:]) # get's the last three items
print(names[1:4]) # middle elements returned
print(names)# returns everything from beginning to end
names[1] = 'Jon'
print(names[1])


# challenge: find the largest number in list

numbers = [3,6,10,5,4,2]

max = numbers[0]
for num in numbers:
    if num > max:
        max = num

print(max)

#multidimensional list
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0][1]) # 2

for row in matrix:
    for item in row:
        print(item)


numbers.append(12)
print(numbers) # [3, 6, 10, 5, 4, 2, 12]
numbers.insert(0,20)
print(numbers) # [20, 3, 6, 10, 5, 4, 2, 12]
numbers.remove(5)
print(numbers) # [20, 3, 6, 10, 4, 2, 12]
# numbers.pop() removes the last number
# numbers.index(6) returns index of the first occurence of thsi number
# print(50 in numbers) returns False if not present
print(12 in numbers) # returns True
# numbers.sort() doesn't return values
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
numbers2 = numbers.copy()
numbers.append(100)
print(numbers)
print(numbers2)

## challenge

nums = [2,2,6,7,6,6,4,1]

uniques = []

for num in nums:
    if num not in uniques:
        uniques.append(num)

print(uniques)