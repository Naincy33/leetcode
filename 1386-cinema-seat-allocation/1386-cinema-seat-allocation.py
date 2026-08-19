class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        rows = {}

        # Har row ke reserved seats store karo
        for r, s in reservedSeats:
            rows.setdefault(r, set()).add(s)

        # Jo rows reserved nahi hain:
        # har row mein 2 groups possible
        ans = (n - len(rows)) * 2

        for seats in rows.values():

            left = {2, 3, 4, 5}
            middle = {4, 5, 6, 7}
            right = {6, 7, 8, 9}

            if not (seats & left) and not (seats & right):
                # Left aur Right dono possible
                ans += 2

            elif not (seats & left) or not (seats & middle) or not (seats & right):
                # At least one block possible
                ans += 1

        return ans