import string

def to_camel_case(text):

    for char in text:
        if char in ('-', '_'):
            if char !=


    


print(to_camel_case('the_steal-warrior_'))
print(to_camel_case('the-steal_warrior-'))
print(to_camel_case('-the_steal_warrior'))
print(to_camel_case('_the-steal-warrior'))
