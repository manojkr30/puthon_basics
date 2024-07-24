'''
   @Author: manoj kr
   @Date: 2024-07-19 15:57
   @Last Modified by: manoj kr
   @Last Modified time: 2024-07-19 16:04
   @Title : Check Whether a Number is Even or Odd
'''
def even_odd(num):
    '''
    Description: To check number is even or odd.  
    Parameters:
            int(num):The number to check  
    Returns:
      boolean: 
              True:if even
              False:if odd

    '''
    return num%2==0


#main method 
def main():
    num=int(input("Enter the number :"))
    if(even_odd(num)):
        print("It is Even Number")
    else:
        print("It is the Odd Number")

if __name__=="__main__":
    main()