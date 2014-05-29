# Partition
"""
size = int(raw_input())
nums = map(int, raw_input().split(" "))
left = []
right = []
p = nums[0]
for index in xrange(1, len(nums)):
        if nums[index] < p:
                left.append(nums[index])
        else:   
                right.append(nums[index])
print (' '.join(map(str, left)) + " " + str(p) + " " + ' '.join(map(str, right))).strip()
"""

# Quicksort
def quicksort(nums):
        if len(nums) <= 1:
                return nums
        left = []
        right = []
        pivot = nums[0]
        for index in xrange(1, len(nums)):
                if nums[index] < pivot:
                        left.append(nums[index])
                else:
                        right.append(nums[index])
        solution = quicksort(left) + [pivot] + quicksort(right)
        print ' '.join(map(str, solution))
        return solution

size = int(raw_input())
nums = map(int, raw_input().split(" "))
quicksort(nums)

# Runtime Eval (as compared to insertion sort)
"""
size = int(raw_input())
nums = map(int, raw_input().split(" "))
insertNums = list(nums)
quickNums = list(nums)

quickCount = 0
def quicksort(nums):
        global quickCount
        if len(nums) <= 1:
                return nums
        pivot = nums[-1]
        firstGreaterIndex = 0
        for index in xrange(len(nums)-1):
                if nums[index] < pivot:
                        nums[index], nums[firstGreaterIndex] = nums[firstGreaterIndex], nums[index]
                        firstGreaterIndex+=1
                        quickCount+=1
        nums[-1], nums[firstGreaterIndex] = nums[firstGreaterIndex], nums[-1]
        quickCount+=1
        solution = quicksort(nums[0:firstGreaterIndex]) + [nums[firstGreaterIndex]] + quicksort(nums[firstGreaterIndex+1:])
        return solution

quicksort(quickNums)

insertCount = 0
for itemIndex in xrange(1, len(insertNums)):
        item = insertNums[itemIndex]
        for index in xrange(itemIndex-1, -1, -1):
                if insertNums[index] > item:
                        insertNums[index+1] = insertNums[index]
                        insertCount+=1
                        if index == 0:
                                insertNums[index] = item
                else:
                        insertNums[index+1] = item
                        break

print insertCount - quickCount
"""
