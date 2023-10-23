# Task 2 - Find unique quadruplets

def Quadruplet(nums, target):
    nums.sort()
    ans, a = [], []

    def sum(count ,start, target):
        if count != 2:
            for i in range(start, len(nums) - count + 1):
                if i > start and nums[i] == nums[i-1]:
                    continue
                a.append(nums[i])
                sum(count-1, i+1, target-nums[i])
                a.pop()
            return
        
        l, r = start, len(nums) - 1
        while l < r:
            if nums[l] + nums[r] < target:
                l += 1
            elif nums[l] + nums[r] > target:
                r -= 1
            else:
                ans.append(a + [nums[l], nums[r]])
                l += 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1

    sum(4, 0, target)
    return ans

# Test cases
test_1 = Quadruplet([1, 0, -1, 0, -2, 2], 0)
test_2 = Quadruplet([2,2,2,2,2], 8)

print(test_1, test_2, sep="\n")