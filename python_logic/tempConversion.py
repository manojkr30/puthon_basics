'''
   @Author: manoj kr
   @Date: 2024-07-20 2:41
   @Last Modified by: manoj kr
   @Last Modified time: 2024-07-20 2:56
   @Title : temperatur Conversion static function, given the temperature
            in fahrenheit as input outputs the temperature in Celsius or vice versa
'''
class Util:
    '''
    class Util having to static methods for Temperature Conversion
    '''
    @staticmethod 
    def celsius_to_fahrenheit(celsius):
        '''
         Description : To temperatur Conversion from celsius to fahrenheit.
         Parameter : int(celsius) the value of temperatur in celsius.
         Return : int return the carasponding temperatur value in fahrenheit.
        '''
        return (celsius*9/5)+32
        
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        '''
         Description : To temperatur Conversion from fahrenheit to celsius.
         Parameter : int(celsius) the value of temperatur in fahrenheit.
         Return : int return the carasponding temperatur value in celsius.
        '''
        return (fahrenheit-32)*(5/9)

if __name__=="__main__":
     print("press option to convert Temperature :\n 1->celsius_to_fahrenheit\n 2->fahrenheit_to_celsius")
     option=int(input())
     if(option==1):
        celsius=int(input("Enter the Temperature in celsius °C="))
        print(Util.celsius_to_fahrenheit(celsius),"°F")
     elif(option==2):
         fahrenheit=int(input("Enter the Temperature in fahrenheit °F="))
         print(Util.fahrenheit_to_celsius(fahrenheit),"°C") 
     else:
          print("select the Valid Option!..")