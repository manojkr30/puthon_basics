'''
   @Author: manoj kr
   @Date: 2024-07-19 15:51
   @Last Modified by: manoj kr
   @Last Modified time: 2024-07-19 15:56
   @Title : Swap Two Numbers

'''

def main():
    num1=int(input("Enter 1st number :"))
    num2=int(input("Enter 1st number :"))
    print("Before swap")
    print("1st number num1=",num1)
    print("2st number num2=",num2)
    temp=num1
    num1=num2
    num2=temp
    print("After swap")
    print("1st number num1=",num1)
    print("2st number num2=",num2)

if __name__=="__main__":
    main()