"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Nhi Tran
Lab Time:
"""

def norm():
    num =  int(input("Enter Number: "))
    num_list = []
    for i in range(num):
        num_list.append(float(input()))
    
    max_num = max(num_list)

    for num in num_list:
        
        final_num = num / max_num
        print(f'{final_num:.2f}')

if __name__ == "__main__":
    norm()