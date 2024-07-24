'''
   @Author: manoj kr
   @Date: 2024-07-20 10:07
   @Last Modified by: manoj kr
   @Last Modified time: 2024-07-20 10:14
   @Title : Given N distinct Coupon Numbers, how many random numbers do you
            need to generate a distinct coupon number? This program simulates this random
            process.
'''
import random

class CouponCollector:
    @staticmethod
    def generate_random_number():
        '''
        Description : produce random number range from 1000 to 9999 using randint buildin fuction in random module
        Return : unique integer range between 1000 to 9999 
        '''
        return random.randint(1000,9999)

    @staticmethod
    def collect_coupons(n):
        '''
        Description : Given N distinct Coupon Numbers, how many random numbers do you
                    need to generate a distinct coupon number ? This program simulates this random
                    process.
        Parameter : N value which represents N numbers of coupon numbers
        Return : set which contains N unique coupon numbers

        '''
        collected_coupons = set()
        while len(collected_coupons) < n:
            random_number = CouponCollector.generate_random_number()
            collected_coupons.add(random_number)
        return collected_coupons

if __name__ == "__main__":
    N = int(input("Enter the number of distinct coupon numbers: "))
    coupons= CouponCollector.collect_coupons(N)
    print(f"Total random numbers needed to collect all {N} distinct coupons: {coupons}")
  