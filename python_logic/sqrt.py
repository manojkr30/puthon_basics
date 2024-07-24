'''
   @Author: manoj kr
   @Date: 2024-07-20 
   @Last Modified by: manoj kr
   @Last Modified time: 2024-07-20
   @Title : a static function sqrt to compute the square root of a nonnegative number c
            given in the input using Newton's method:
'''

def sqrt(c):
    if c < 0:
        raise ValueError("Input must be a nonnegative number.")
    
    epsilon = 1e-15  # Desired accuracy threshold
    t = c  # Initial guess for square root

    while abs(t - c / t) > epsilon * t:
        t = (c / t + t) / 2.0
    
    return t

# Example usage:
if __name__ == "__main__":
    c = float(input("Enter a non negative number: "))
    square_root = sqrt(c)
    print(f"The square root of {c} is approximately {square_root}")
