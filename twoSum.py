class solution(object):
    
    def twoSum(self, nums, target):
        
        my_dict = {}
        
        for index, value in enumerate(nums):
            
            complement = target - value
            
            if complement in my_dict:
                 return [my_dict[complement], index]
            my_dict[value] = index
        
        return None
    
    "Notes: The time complexity of this solution is O(n) and the space complexity is O(n)."