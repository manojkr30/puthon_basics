'''
   @Author: manoj kr
   @Date: 2024-07-19 11:45
   @Last Modified by: manoj kr
   @Last Modified time: 2024-07-19 11:52
   @Title : Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N

'''
#function to find Nth Harmonic
def harmonic(num):
    '''
    Description:
               To caculate Nth Harmonic 
    Parameters:
              num (int): The Nth number from 1 to num 
    Returns:
           print nth Harmonic number
           
    '''
    if(num != 0):
        harmonic=0
        for i in range(1,num+1):
            harmonic += 1/i
        print("The",num,"th Harmonic Value =",harmonic)
    else:
         print("The Nth value should More than 0")

#main method
def main():
    num=int(input("Enter the Number to Find Nth Harmonic :"))
    harmonic(num)


if __name__=="__main__":
    main()