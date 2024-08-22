class Solution(object):
    def contains_Duplicate(self, nums):
        
        '''
        Return true if any values appears more that once,
        and false if not.
        '''
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                
                if nums[i] == nums[j] and i != j:
                    return True
        
         #this solves in o(n^2) time complexity very slow
        return False
    
    def contains_Duplicate2(self, nums):
        
        my_hashMap = {}
        
        for index, value in enumerate(nums):
            
            if value in my_hashMap:
                return True
            
            my_hashMap[value] = index
            
            #this solves in o(n) time complexity, faster than the previous function
            
        return False
                
            
        
        
Values = [1, 2, 3, 4, 5, 6, 7, 6, 9, 10]

print(Solution().contains_Duplicate2(Values))
