'''
   @Author: manoj kr
   @Date: 2024-07-20 10:25
   @Last Modified by: manoj kr
   @Last Modified time: 2024-07-20 10:40
   @Title :To calculate monthlyPayment that reads in three
            command-line arguments P, Y, and R and calculates the monthly payments you
            would have to make over Y years to pay off a P principal loan amount at R percent
            interest compounded monthly.
'''
class Util:
    @staticmethod
    def monthly_payment(P,Y,R):
        '''
        Description : Static Function to calculate monthlyPayment
        Parameter : reads in three command-line arguments P, Y, and R integer values
        Return : (int)  monthly payments you would have to make
        
        '''
        n=12*Y
        r=R/(12*100)
        payment=(P*r) / (1-(1+r)**(-n))
        return int(payment)
    
if __name__=="__main__":
    p=int(input("Enter the principal loan amount : "))
    y=int(input("Enter the year : "))
    r=float(input("Enter the  interest in percent : "))
    print("the monthly payments you would have to make =",Util.monthly_payment(p,y,r))