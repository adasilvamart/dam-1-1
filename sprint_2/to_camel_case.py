def to_camel_case(text):
    camelCaseText = ""
    nextUpper = False
    
    for index in range(len(text)):
        if text[index] == '-' or text[index] == '_':
            nextUpper = True
        elif nextUpper:
            camelCaseText += text[index].upper()
            nextUpper = False
        else:
            camelCaseText += text[index]

    return camelCaseText

    

#print(to_camel_case("A-B-C"))
#print(to_camel_case("Ramon_holas"))
print(to_camel_case('the_steal-warrior_'))
print(to_camel_case('the-steal_warrior-'))
print(to_camel_case('-the_steal_warrior'))
print(to_camel_case('_the-steal-warrior'))
