

def check_dictionary(name):
    result = {letter: name.count(letter) for letter in name}
    return result



name = input("What is your name? ")
print(check_dictionary(name))