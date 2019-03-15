def changeVowels1(user_input, vowels):
    user_input = list(user_input)

    for index in range(0, len(user_input)):
        if user_input[index].lower() in vowels:
            user_input[index] = vowels[user_input[index].lower()]

    return ("".join(user_input))

def changeVowels2(user_input, vowels):
    temp_string = ""
    for char in user_input:
        if char.lower() in vowels:
            char = vowels[char.lower()]
        temp_string += char
    
    return temp_string
    
vowels = {
    'a': '$',
    'e': '$',
    'i': '$',
    'o': '$',
    'u': '$'
}
user_input = input("Please input a phrase and I will replace the vowels with \'$\': ")
print (changeVowels1(user_input, vowels))
print (changeVowels2(user_input, vowels))