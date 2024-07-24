'''
   @Author: manoj kr
   @Date: 2024-07-19 13:45:30
   @Last Modified by: manoj kr
   @Last Modified time: 2024-07-19 13:52:00
   @Title : Computes the prime factorization of N using brute force.

'''

def is_prime(n):
    '''
    Description:
       Its take number of integer type and ckeck that number is Prime or Not.
    Parameters:
        n (int): The number to check Prime Or NOt.
    Returns:
        boolean: return True if number is Prime or It return False if Number is Not Prime.
    '''
    i=2
    while(i<=n/2):
        if(n%i == 0):
            return False
        i+=1
    return True
def main():
    num = int(input("Enter the Number to find the prime factors : "))
    for i in range(1,num+1):
        if(is_prime(i)==True):
            print(i)
        
if __name__ == "__main__":
    main()