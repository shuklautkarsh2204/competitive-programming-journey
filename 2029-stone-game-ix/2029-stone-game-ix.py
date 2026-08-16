class Solution:
    def stoneGameIX(self, stones):
        cnt = [0, 0, 0]

        for x in stones:
            cnt[x % 3] += 1

        zero, one, two = cnt

        if min(one, two) == 0:
            return max(one, two) > 2 and zero % 2 == 1

        return abs(one - two) > 2 or zero % 2 == 0
        