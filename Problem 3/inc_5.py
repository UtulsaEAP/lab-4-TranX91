"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name: Nhi Tran
Lab Time:
"""

def inc_5():
    first_int = int(input("Enter First Integer: "))
    second_int = int(input("Enter Second Integer: "))
    
    if second_int >= first_int:
        for i in range(first_int, second_int + 1, 5,):
            print(i, end = ' ')
        print()
    else:
     print('Second integer can\'t be less than the first.')

if __name__ == '__main__':
    inc_5()