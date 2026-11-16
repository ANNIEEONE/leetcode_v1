class Solution(object):
    def plusOne(self, digits):
        # Traverse from the last index down to 0
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        # If all digits were 9, prepend 1 to the array of 0s
        return [1] + digits