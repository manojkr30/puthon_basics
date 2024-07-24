'''
   @Author: manoj kr
   @Date: 2024-07-20 4:20
   @Last Modified by: manoj kr
   @Last Modified time: 2024-07-20 4:38
   @Title : To the Util Class add dayOfWeek static function that takes a date as input and
            prints the day of the week that date
'''
class Util:
    @staticmethod
    def dayOfWeek(m, d, y):
        '''
        Description : static function that takes a date as input and
                      prints the day of the week that date. 
        Parameter : should take three command-line arguments: m (month), d (day), and y (year).
        Return : (int) value range between 0 --> 6 
                       where, 0 for Sunday, 1 for Monday, 2 for Tuesday, and so forth.
        '''
        y1= y - (14 - m)//12
        x = y1 + y1//4 - y1//100 + y1//400
        m1= m + 12*((14-m)//12)-2
        d = (d+x+(31*m1)//12)%7
        return int(d)
    
    @staticmethod
    def display(day):
     '''
        Description : static function that to display the day oin string formate based on the input int value.             
        Parameter : should take  one int(day) where value ranges between 0 --> 6.
        Return : day in String formate.
     '''
     if(day==0):
        return "Sunday"
     elif(day==1):
        return "Monday"
     elif(day==2):
        return "Tuesday"
     elif(day==3):
        return "Wednesday"
     elif(day==4):
        return "Thurstday"
     elif(day==5):
        return "Friday"
     elif(day==6):
        return "Saturday"
    
if __name__=="__main__":
    month=int(input("Enter the Month my number :"))
    day=int(input("Enter the Day :"))
    year=int(input("Enter the Year :"))
    print(Util.display(Util.dayOfWeek(month,day,year)))
