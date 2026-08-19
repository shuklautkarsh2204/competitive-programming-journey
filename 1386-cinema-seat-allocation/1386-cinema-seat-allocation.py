class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}
        for row, seat in reservedSeats:
            if row not in rows:
                rows[row] = set()
            rows[row].add(seat)

        ans = (n - len(rows)) * 2

        for seats in rows.values():

            left = {2, 3, 4, 5}
            middle = {4, 5, 6, 7}
            right = {6, 7, 8, 9}

            if left.isdisjoint(seats) and right.isdisjoint(seats):
                ans += 2

            elif (left.isdisjoint(seats) or
                  middle.isdisjoint(seats) or
                  right.isdisjoint(seats)):
                ans += 1

        return ans