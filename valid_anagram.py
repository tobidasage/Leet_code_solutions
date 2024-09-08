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


#solution().validAnagram(word1, word2)

class solution2(object):
    def valid_anagram2(self, s, t):
        
        if len(s) != len(t):
            print("False")
            return False
        
        count_s, count_t = {}, {}
        
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
            
        for c in range(len(s)):
            if count_t[t[c]] == count_s[s[c]]:
                print("True")
                return True
        
word1 = 'anagram'
word2 = 'nagamar'
    
solution2().valid_anagram2(word1, word2)

