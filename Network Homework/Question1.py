########### question one A ###########

L1=["HTTP","HTTPS","FTP","DNS"]
L2=[80,443,21,53]

result = {key : value for key,value in zip(L1,L2)}
    
print(result)


#######################################
########### questions one B ###########

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    try:
        num = int(input("Enter a number to calculate its factorial: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print(f"The factorial of {num} is {factorial(num)}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()


#######################################
########### questions one C ###########

L = ['Network', 'Bio', 'Programming', 'Physics', 'Music']

for item in L:
    if item.startswith('B'):
        print(item)


######################################
########## questions one D ###########

result = {i : i+1 for i in range(10)}
print(result)
