class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_product = 1
        
        # Convert the integer to a string to easily iterate over each digit
        for digit in str(n):
            d = int(digit)
            digit_sum += d
            digit_product *= d
            
        return n % (digit_sum + digit_product) == 0