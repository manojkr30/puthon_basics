'''
   @Author: manoj kr
   @Date: 2024-07-20 3:11
   @Last Modified by: manoj kr
   @Last Modified time: 2024-07-20 3:26
   @Title : toBinary that outputs the binary (base 2) representation of
            the decimal number typed as the input. It is based on decomposing the number into
            a sum of powers of 2. For example, the binary representation of 106 is 11010102,
            which is the same as saying that 106 = 64 + 32 + 8 + 2. Ensure necessary padding
            to represent 4 Byte String.
'''

def to_binary(decimal):
    '''
    Description : 
    Parameter : int(num) the nth postion to find the fibonacci 
    Return : 
    '''
    binary=""
    while(decimal!=0):
        rem=str(decimal%2)
        binary=rem+binary
        decimal//=2
    return binary

if __name__=="__main__":
    decimal=int(input("Enter the Decimal value ="))
    print("binary representation of",decimal,"=",to_binary(decimal))