class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1

        res = []

        for i in range(len(sorted_nums)):
            counter[sorted_nums[i]] -= 1

            if i and sorted_nums[i] == sorted_nums[i - 1]: # Check duplicates for first number
                continue

            for j in range(i + 1, len(sorted_nums)):
                counter[sorted_nums[j]] -= 1
                if j - 1 > i and sorted_nums[j] == sorted_nums[j - 1]: # Check dupe for second number
                    continue

                # 0 = n[i] + n[j] + n[k] --> n[k] = -1 * (n[i] + n[j]) | target = n[k]
                target = -1 * (sorted_nums[i] + sorted_nums[j])
                if counter[target] > 0:
                    res.append([sorted_nums[i], sorted_nums[j], target])

            for j in range(i + 1, len(sorted_nums)):
                counter[sorted_nums[j]] += 1

        return res








