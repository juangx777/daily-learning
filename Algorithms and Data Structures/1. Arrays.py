# =================================================================================================
# Static Array
# =================================================================================================

x = [1, 2, 3, 4, 5, 6, 7, 8]
position = 1

# deleting val to ith position
for index in range(position+1, len(x)):
    x[index-1] = x[index]

# inserting val in ith position
for index in range(len(x)-1, position-1, -1):
    x[index+1] = x[index]
x[position] = n


## Exercise

# Leetcode 26
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        ## solution 2
        # two pointers, l pointer used to indicator unique value place position, r pointers used to loop through whole list 
        # time complexity would be big O of n
        # space complexity would be big O of 1
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
            
        return l


# Leetcode 27
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # using two pointers too, k used to indicator the location of non val element
        # i used to scan through the list
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k


# =================================================================================================
# Dynamic Array
# =================================================================================================

## Exercise 

# Leetcode 1929

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        ans = []
        # using range here then we can be flexible how many times we wnanna concate 
        for i in range(2):
            for index in range(len(nums)):
                ans.append(nums[index])

        return ans


# =================================================================================================
# Stacks
# =================================================================================================

## Exercise     

# Leetcode 20

class Solution:
    def isValid(self, s: str) -> bool:

        # using stack DS and hash map in here to find match of each character
        Stack = []
        CloseToOpen = {')':'(', ']':'[', '}':'{'}

        for c in s:
            if c in CloseToOpen:
                # if stack is not empty and last adding open bracket to the stack eqaul to hash map value then pop the value
                if Stack and Stack[-1] == CloseToOpen[c]:
                    Stack.pop()
                else:
                    return False
            # adding open bracket in here 
            else:
                Stack.append()
        
        # Stack should empty if all value match with hash map
        return True if not Stack else False