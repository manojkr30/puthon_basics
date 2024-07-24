'''
   @Author: manoj kr
   @Date: 2024-07-19 16:23
   @Last Modified by: manoj kr
   @Last Modified time: 2024-07-19 16:32
   @Title : To Find the Largest Among Three Numbers
'''
def largest(num1,num2,num3):
    '''
    Description: 
               To return largest number among 3 number given 
    Parameters:
               int(num1,num2,num3): 3 individual number to find largest amount them.
    Returns:
              int: return Largest amoung given 3 number.
    '''
    if num1>num2 and num1>num3:
        return num1
    elif num2>num3:
        return num2
    else:
        return num3

def main():
    num1=int(input("Ether the 1st Number :"))
    num2=int(input("Ether the 2st Number :"))
    num3=int(input("Ether the 3st Number :"))
    print("Largest number is :",largest(num1,num2,num3))

if __name__=="__main__":
    main()