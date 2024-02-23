"""
Complete the following python code to reverse the string entered by the user.

Name: Nhi Tran
Lab Time:
"""

def reverse_string():
    word = str(input())
    inverse = ['Done', 'done', 'd']
    while word not in inverse:
        word = str(input())
        print(word[::-1])
        
    
    

if __name__ == "__main__":
    reverse_string()