def alphabet_position(text):
    text = text.lower()
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha_dict = {}
    result = ""

    for i in range(len(alpha)):
        alpha_dict[alpha[i]] = i + 1

    for char in text:
        if char in alpha_dict:
            result += str(alpha_dict[char]) + " "
        
    result = result.rstrip()
    
    return result
    

print(alphabet_position("abcdefghijklmnopqrstuvwxyz"))