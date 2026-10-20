class Solution:
    def largestGoodInteger(self, num: str) -> str:
        freq = defaultdict(int)

        maximum = float("-inf")
        prev = num[1]
        count = 1
        
        for n in num[1:]:
            if n != prev:
                count = 1
                prev = n
            else:
                count += 1
                if count == 3: # We only need to compute this once and not for following counts
                    number = 100 * int(n) + 10 * int(n) + int(n)
                    maximum = max(maximum, number)

        if maximum == float("-inf"):
            maximum = ""
        elif maximum == 0:
            maximum = "000"
        else:
            maximum = str(maximum)

        return maximum




