'''
   @Author: manoj kr
   @Date: 2024-07-20 5:07
   @Last Modified by: manoj kr
   @Last Modified time: 2024-07-20 5:34
   @Title : There are 1, 2, 5, 10, 50, 100, 500 and 1000 Rs Notes which can be
            returned by Vending Machine. Write a Program to calculate the minimum number
            of Notes as well as the Notes to be returned by the Vending Machine as a Change.
'''

def display_notes():
    print("The the Change in Rs to be returned by the Vending Machine :")
    print("1000.rs\n500.rs\n100.rs\n50.rs\n10.rs\n5.rs\n2.rs\n1.rs")

def vender_machine(withdraw_amount, total_amount,number_notes):
    '''
        Description : Use Recursion and check for largest value of the Note to return change
                      to get to minimum number of Notes. 
        Parameter : should take three command-line arguments:withdraw_amount(int), total_amount(set),number_notes(int).
        Return : Two Outputs - one the number of minimum Note needed to give the
                 change and second list of Rs Notes that would given in the Change
                       
    '''
    number_notes
    if(withdraw_amount==0):
        return total_amount,number_notes
    elif(withdraw_amount>=1000):
        total_amount.append(1000)
        number_notes+=1
        return vender_machine(withdraw_amount-1000,total_amount,number_notes)
    elif(withdraw_amount>=500):
        total_amount.append(500)
        number_notes+=1
        return vender_machine(withdraw_amount-500,total_amount,number_notes)
    elif(withdraw_amount>=100):
        total_amount.append(100)
        number_notes+=1
        return vender_machine(withdraw_amount-100,total_amount,number_notes)
    elif(withdraw_amount>=50):
        total_amount.append(50)
        number_notes+=1
        return vender_machine(withdraw_amount-50,total_amount,number_notes)
    elif(withdraw_amount>=10):
        total_amount.append(10)
        number_notes+=1
        return vender_machine(withdraw_amount-10,total_amount,number_notes)
    elif(withdraw_amount>=5):
        total_amount.append(5)
        number_notes+=1
        return vender_machine(withdraw_amount-5,total_amount,number_notes)
    elif(withdraw_amount>=2):
        total_amount.append(2)
        number_notes+=1
        return vender_machine(withdraw_amount-2,total_amount,number_notes)
    else :
        total_amount.append(1)
        number_notes+=1
        return vender_machine(withdraw_amount-1,total_amount,number_notes)
    
if __name__=="__main__":
    display_notes()
    amount=int(input("Enter the ammount to Withdraw :"))
    notes_rs,number_notes=vender_machine(amount,[],0)
    print("The minimum number of Notes : ",number_notes)
    print("withdraw Notes :",notes_rs)


