"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name: Nhi Tran
Lab Time:
"""

def password_mod():
    word = input()
    password = ''

    for character in word:
        if (character == 'i'):
            password += '!'
        elif (character == 'a'):
            password += '@'
        elif (character == 'm'):
            password += 'M'
        elif (character == 'B'):
            password += '8'
        elif (character =='s'):
            password += '$'
        elif (character == '.'):
            password += '!'
        else:
            password += character
    print(password)
    

if __name__ == "__main__":
    password_mod()