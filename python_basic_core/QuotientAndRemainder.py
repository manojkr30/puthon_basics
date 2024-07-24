'''
   @Author: manoj kr
   @Date: 2024-07-19 13:54:30
   @Last Modified by: manoj kr
   @Last Modified time: 2024-07-19 14:20:30
   @Title : Computes the prime factorization of N using brute force.

'''
def quotient_and_remainder(num,div):
    '''
    Description:
       To cacuclate remainder and Quotient.
    Parameters:
        n (int): the Numerator
        div(int):the Denominator
    Returns:
        int,int: return Quotient , Remainder 
    '''
    return num/div ,num%div

def main():
    num=int(input("Enter the Numerator :"))
    div=int(input("Enter the Denominator :"))
    quotient,remainder=quotient_and_remainder(num,div)
    print("Quotient =",quotient)
    print("Remainder =",remainder)

if __name__=="__main__":
  main()


