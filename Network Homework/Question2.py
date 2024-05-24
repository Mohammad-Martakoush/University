
######################################
########## questions two #############

def binary_to_decimal(binary_str):
    try:
        decimal_number = int(binary_str, 2)
        return decimal_number
    except ValueError:
        print("Please type a binary number")
        return None

def main():
    binary_str = input("Type a binary number : ")
    
    decimal_number = binary_to_decimal(binary_str)
    
    if decimal_number is not None:
        print(f"You'r binary number is : {binary_str} and in decimal is : {decimal_number}")

if __name__ == "__main__":
    main()
