'''
   @Author: manoj kr
   @Date: 2024-07-19 11:00:30
   @Last Modified by: manoj kr
   @Last Modified time: 2024-07-19 1:23:30
   @Title : Flip Coin and print percentage of Heads and Tails

'''

import random

def flipCoin():
    return random.random()

numerOfTimes = int(input("enter the number of times to Flip Coin :"))
heads = tails =0
for coin in range(1,numerOfTimes+1):
    if(flipCoin() < 0.5):
        tails +=1
    else:
        heads +=1
print("percentage of Head is",round((heads/numerOfTimes)*100 , 2))
print("percentage of Tail is",round((tails/numerOfTimes)*100 , 2))