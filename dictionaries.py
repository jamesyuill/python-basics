# dictionaries - like objects in js
# key value pairs

customer = {
   "name":'James Potato',
   "age": 30,
   "is_Verified": True
}

print(customer["name"])
print(customer.get("name"))
print(customer.get("birthdate")) # None
print(customer.get("birthdate", 'Jan 1 1980')) # default value
customer["name"] = "Jack Smith"
print(customer.get("name"))
customer["birthdate"] = "Jan 1 1980"
print(customer.get('birthdate'))


# challenge 

phone = input('Phone: ')

lookup = {
    '1':'One',
    '2':'Two',
    '3':"Three",
    '4':"Four",
    '5':'Five'
}

output = ''
for char in phone:
    output += lookup.get(char,'!') + ' '

print(output)
    
