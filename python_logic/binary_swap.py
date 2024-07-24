'''


   @Author: manoj kr
   @Date: 2024-07-19 15:57
   @Last Modified by: manoj kr
   @Last Modified time: 2024-07-19 16:04
   @Title : to read an integer as an Input, convert to Binary using toBinary
function and perform the following functions.
i. Swap nibbles and find the new number.
ii. Find the resultant number is the number is a power of 2.
A nibble is a four-bit aggregation, or half an octet. There are two nibbles in a byte.


'''


def to_binary(number):
    return format(number, '08b')

def swap_nibbles(binary):
    if len(binary) != 8:
        raise ValueError("Binary string must be 8 bits long")
    first_nibble = binary[:4]
    second_nibble = binary[4:]
    return second_nibble + first_nibble

def is_power_of_two(number):
    return (number > 0) and (number & (number - 1)) == 0

def main():
    number = int(input("Enter an integer: "))
    
    binary = to_binary(number)
    print(f"Binary representation: {binary}")

    swapped_binary = swap_nibbles(binary)
    print(f"Binary after swapping nibbles: {swapped_binary}")

    swapped_number = int(swapped_binary, 2)
    print(f"Number after swapping nibbles: {swapped_number}")

    power_of_two = is_power_of_two(swapped_number)
    print(f"Is the resultant number a power of 2? {power_of_two}")

if __name__ == "__main__":
    main()
