# Nourhan Adel Mohamed El-Hady   ID : 20230452
# Caroline Ayman Isaac           ID : 20230292
# Fatma Nazeih Hanfy             ID : 20230284

def add_binary_num(a, b):
    # Adds two binary numbers represented as strings and returns the sum as a string.
    # Make the numbers the same length by padding with leading zeros.
    if len(a) < len(b):
        a = "0" * (len(b) - len(a)) + a
    elif len(b) < len(a):
        b = "0" * (len(a) - len(b)) + b

    carry = 0
    addition = ""

    for i in range(len(a) - 1, -1, -1):
        sum_digit = int(a[i]) + int(b[i]) + carry  # Calculate the sum of the current digits and carry
        # Handle different sum cases:
        if sum_digit == 0 or sum_digit == 1:
            carry = 0
            addition = str(sum_digit) + addition
        elif sum_digit == 2:
            carry = 1
            addition = "0" + addition
        elif sum_digit == 3:
            carry = 1
            addition = "1" + addition
    # Handle a final carry
    if carry == 1:
        addition = "1" + addition

    return addition



def sub_binary_num(a, b):
    # Subtracts two binary numbers represented as strings and returns the difference as a string.
    # Make the numbers the same length by padding with leading zeros
    if len(a) < len(b):
        a = "0" * (len(b) - len(a)) + a
    elif len(b) < len(a):
        b = "0" * (len(a) - len(b)) + b
    borrow = 0
    subtraction = ""
    for i in range(len(a) - 1, -1, -1):
        diff_digits = int(a[i]) - int(b[i]) - borrow  # Calculate the difference of the current digits and borrow
        # Handle different difference cases:
        if diff_digits >= 0:
            borrow = 0
            subtraction = str(diff_digits) + subtraction
        else:
            borrow = 1
            subtraction = str(diff_digits + 2) + subtraction   # Borrow from the next digit (equivalent to adding 2 in binary)
    return subtraction

def Binary_to_one_complement(Binary):
    # Converts a binary string to its one's complement representation and returns the result as a string
    First_complement = ""
    for bit in Binary:
        if bit == "0":  # If the current bit is 0, flip it to 1
            First_complement = First_complement + "1"
        else:  # If the current bit is 1, flip it to 0
            First_complement = First_complement + "0"
    return First_complement

def binary_to_two_complement(binary):
    # Converts a binary string to its two's complement representation and returns the result as a string.
    one_complement = Binary_to_one_complement(binary)  # Get the one's complement first
    two_complement = add_binary_num(one_complement, '1')  # Add 1 to the one's complement to get the two's complement
    return two_complement

def menu_1():
    # Displays the main menu of the binary calculator.
    print("** Binary Calculator **")
    print("A) Insert new number ")
    print("B) Exist ")

def menu_2(number):
    # Displays the main menu of the selected operation.
    print("** please select the operation **")
    print("A) Compute one's complement")
    print("B) Compute two's complement")
    print("C) addition")
    print("D) subtraction")
    option_2 = input(" select a choice :")
    if option_2 == "A":  # first complement
        First_complement= Binary_to_one_complement(str(number))
        print("The first complement is :", First_complement)
    elif option_2 == "B":  # second complement
        two_complement = binary_to_two_complement(str(number))
        print("The second complement is =", two_complement)
    elif option_2 == "C":  # add operation
        while True:
            num_2 = input("please insert the second binary number: ")  # enter the number that will be added to num_1
            bin_bits = {'0', '1'}  # Set of valid binary digits
            for bit in num_2:  # Validate each digit of the input number
                if bit not in bin_bits:  # If a non-binary digit is found
                    print("ERROR: please insert a valid binary number")
                    break  # Exit the loop if invalid input
            else:  # If all digits are valid
                addition = add_binary_num(number, num_2)  # Call the addition function
                print("The Addition of the two numbers =", addition)
                break  # exit the loop after addition
    elif option_2 == "D":  # second complement
        while True:
            num_2 = input("please insert the second binary number: ")  # enter the number that will be subtracted to num_1
            bin_bits = {'0', '1'}  # Set of valid binary digits
            for bit in num_2:  # Validate each digit of the input number
                if bit not in bin_bits:  # If a non-binary digit is found
                    print("ERROR: please insert a valid binary number")
                    break  # Exit the loop if invalid input
            else:  # If all digits are valid
                subtraction = sub_binary_num(number, num_2)  # Call the subtraction function
                print("The subtraction of the two numbers =", subtraction)
                break


while True:
    # Displays the main menu of the binary calculator
    menu_1()
    option = input("select a choice :")
    if option == "A":
        while True:
            num_1 = input("please insert a binary number: ")
            bin_bits = {'0', '1'}
            for bit in num_1:
                if bit not in bin_bits:
                    print("ERROR: please insert a valid binary number")
                    break
            else:
                menu_2(num_1)
                break

    elif option == "B":
        print("Exit")
        break  # break the hole loop if they choose to exit

    else:
        print(" please select a valid choice")
