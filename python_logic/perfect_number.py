'''
   @Author: manoj kr
   @Date: 2024-07-20 11:25
   @Last Modified by: manoj kr
   @Last Modified time: 2024-07-20 11:40
   @Title : When the number is equal to the sum of its positive divisors
           excluding the number, it is called a Perfect Number
'''

def perfec_number(num):
    return sum_of_divisors(num) == num

def sum_of_divisors(num):
    '''
    Description : To check given number is perfect number or not
    Parameter : int(num) the number need to check wether it is perfect number or not 
    Return : boolean True or false 
            True -> the given number is Perfect Number
            Fale -> the given number is Not Perfect Number
    '''
    sum=0
    for i in range(1,int(num/2+1)):
     if(num%i==0):
        sum+=i
    return sum

if __name__=="__main__":
   num=int(input("Enter the number to check the number is perfect or not :"))
   if(perfec_number(num)):
      print(num,"Perfect Number")
   else:
      print(num,"Not Perfect Number")


  
