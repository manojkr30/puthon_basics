'''
 @Author: manoj kr
   @Date: 2024-07-20 12:35
   @Last Modified by: manoj kr
   @Last Modified time: 2024-07-20 12:45
   @Title : Reverse a number is by using for loop or while loop.
'''

def reverse_number(num):
    '''
    Description : To Reverse a given number is by using for while loop and return reversed number.
    Parameter : int(num) the number need to Reverse.
    Return : int(reverseno) the number reversed.
    '''
    reverseno=0
    while num!=0:  
        reverseno =reverseno*10+num%10
        num=num//10
    return reverseno

if __name__=="__main__":
    num=int(input("Enter the Number to reverse :"))
    print(reverse_number(num))
    

    