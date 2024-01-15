### nested loops
#### (0,0)(0,1)(0,2)(1,0)(1,1)(1,2) etc

for x in range(4):
    for y in range(3):
        print(f'{x},{y}')
    

# Challenge
numbers = [5,2,5,2,2]

for num in numbers:
    print('x'* num)


#mosh solution
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)