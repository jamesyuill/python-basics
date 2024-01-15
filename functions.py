
#define functions first

def greet_user(first_name, last_name):
    print(f'Hi there, {first_name} {last_name}!')
    print(f'Welcome aboard!')

# additional positional arguments

greet_user('James', 'Smith')
greet_user(last_name='Levon',first_name='Mary') # keyword arguments (not necessary)

# calc_cost(total=50,shipping=5,discount=0.1) #keyword arguments


def square(number):
    return number * number

result = square(3)
print(square(3))
print(result)



 
def convertToEmoji(message):
    words = message.split(' ')
    emojis = {
    ":)":"😀",
    ":(":"😔"
}

    output = ''
    for word in words:
        output += emojis.get(word, word) + ' '
    return output


message = input('>')

print(convertToEmoji(message))