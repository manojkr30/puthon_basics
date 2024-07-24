'''
   @Author: manoj kr
   @Date: 2024-07-20 12:11
   @Last Modified by: manoj kr
   @Last Modified time: 2024-07-20 12:24
   @Title : Prime number is also a special type of number. When
            the number is divided greater than 1 and divided by 1 or itself is referred to as the Prime
            number. 0 and 1 are not counted as prime numbers.
'''
def is_prime(num):
    '''
    Description : To check given number is Prime number or not
    Parameter : int(num) the number need to check wether it is prime number or not 
    Return :boolean True or false 
            True -> the given number is Prime Number
            Fale -> the given number is Not Prime Number
    '''
    if(num<=1):
        return False
    for i in range(2,int(num/2+1)):
        if(num%i==0):
            return False
    return True

if __name__=="__main__":
    num=int(input("Enter the Number to find Prime Or Not :"))
    if(is_prime(num)):
        print(num,"is a Prime")
    else:
        print(num,"is Not Prime")


    
