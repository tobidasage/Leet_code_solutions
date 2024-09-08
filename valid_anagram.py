class solution(object):
    def validAnagram(self, s, t):
        
        if len(s) != len(t):
            print('False')
            return False
        
        my_list1 = list(s)
        my_list2 = list(t)
        
        for i in range(len(my_list1)):
            if my_list1[i] in my_list2:
                my_list2.remove(my_list1[i])
        
        if not my_list2:
            print('True')
            return True
        
        print('False')
        return False

word1 = 'anagram'
word2 = 'nagamar'

solution().validAnagram(word1, word2)

'''
This is in O(n) time but it is 
too slow of a solution, 
we have to integrate hashing to solve this
'''