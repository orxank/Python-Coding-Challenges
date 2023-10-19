
num = int(input("enter number: "))

def prime_num(num):
    
    for i in range(2, num):

        if num <= 1:
            return False
        elif num % i == 0:
            return False
        else:
            return True
        
print(prime_num(num))

