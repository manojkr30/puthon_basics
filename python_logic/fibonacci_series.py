'''
   @Author: manoj kr
   @Date: 2024-07-20 10:15
   @Last Modified by: manoj kr
   @Last Modified time: 2024-07-20 10:18
   @Title : Fibonacci series is a special type of series in which the next term is the sum of the
            previous two terms. For example, if 0 and 1 are the two previous terms in a series, then
            the next term will be 1(0+1).
'''
def fibonacci_series(num):
    '''
    Description : gives Nth postion fibonacci number
    Parameter : int(num) the nth postion to find the fibonacci 
    Return : (int) fibonacci number
    '''
    if num==0 or num==1:
        return num
    return fibonacci_series(num-1) + fibonacci_series(num-2)
    

if __name__=="__main__":
    n=int(input("Enther The Nth postion To find Fibonacci Series :"))
    print(fibonacci_series(n))


