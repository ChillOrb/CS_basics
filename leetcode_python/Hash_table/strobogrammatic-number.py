
"""

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.

"""

# Time:  O(n)
# Space: O(1)

# V1  :  need to double check 
class Solution:
    def isStrobogrammatic(self, nums):
        lookup = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        for i, num in enumerate(list(nums)):
            #print (num)
            if str(num) in lookup:
                pass
            else:
                return False
        return True 

# V2 
class Solution:
    # @param {string} num
    # @return {boolean}
    def isStrobogrammatic(self, num):
        lookup = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        n = len(num)
        for i in range((n+1) / 2):
            if num[n-1-i] not in self.lookup or \
               num[i] != self.lookup[num[n-1-i]]:
                return False
        return True