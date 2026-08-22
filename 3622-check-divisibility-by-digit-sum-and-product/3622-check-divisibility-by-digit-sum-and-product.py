class Solution(object):
    def checkDivisibility(self, n):
        add = 0
        mul = 1
        temp = n
        while temp > 0:
            add += temp%10
            mul *= temp%10
            temp //= 10

        test = add + mul    
        if n % test != 0:
            return False
        else:
            return True    