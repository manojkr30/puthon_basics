'''
   @Author: manoj kr
   @Date: 2024-07-19 10:26
   @Last Modified by: manoj kr
   @Last Modified time: 2024-07-19 10:50
   @Title : Print the year is a Leap Year or not.

'''


def isleap(year):
    '''
    Description:
       To Check the given year is valid as year and check it is leap year or Not.
    Parameters:
        year(int): the year given to check
    Returns:
        print:leap year or not  
    '''
    if(year>0 and year<10000):
        if((year % 4 == 0 and year % 100 != 0 ) or year % 400 == 0):
            print(year,"is a Leap Year")
        else:
            print(year,"is Not Leap Year")
    else:
        print("The Enterd Year is Not Valid !")


year = int(input("Enter the year :"))
isleap(year)