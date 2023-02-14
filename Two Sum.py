# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    ints=list(map(int, nums))
    i=0
    result=[]
    while i<len(ints):
        i=i+1
        if (ints[i-1]+ints[i-2]) == target:
            first_i=i-2
            second_i=i-1   
            result.append(first_i)
            result.append(second_i)
            if (i-2)== -1:
                
                first_i=i-1
                second_i=i
                result.append(first_i)
                result.append(second_i)

            if len(result)==4:
                result = result[2:]        
            return result
         

    
        
print(twoSum([3,2,4],6))
