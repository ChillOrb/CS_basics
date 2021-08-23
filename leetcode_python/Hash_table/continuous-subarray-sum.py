"""

Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.

 

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
0 <= sum(nums[i]) <= 231 - 1
1 <= k <= 231 - 1


"""

# V0
class Solution(object):
    def checkSubarraySum(self, nums, k):
        _dict = {0:-1}
        tmp = 0
        for i in range(len(nums)):
            tmp += nums[i]
            if k != 0:
                tmp = tmp % k
            if tmp in _dict:
                if i - _dict[tmp] > 1:
                    return True
            else:
                _dict[tmp] = i
        return False

# V0'
# IDEA : HASH TABLE
# DEMO
#    ...: nums = [23,2,4,6,7]
#    ...: k = 6 
#    ...: s = Solution()
#    ...: r = s.checkSubarraySum(nums,k)
#    ...: print (r)
#    ...: 
# num  =  23 lookup : {0: -1}
# num  =  2 lookup : {0: -1, 5: 0}
# num  =  4 lookup : {0: -1, 5: 0, 1: 1}
# True
class Solution(object):
    def checkSubarraySum(self, nums, k):
        count = 0
        lookup = {0: -1}                   # init the lookup hash table 
        for i, num in enumerate(nums):
            count += num                   # keep adding num up  (as count)
            if k != 0:
                # beware of it
                count %= k                 # get mode of count by k, since it's as same as num when check if it's k's multiplier
            """
            ###  beware of it 
            via the "count in lookup" trick, we can compare with the 
            "whole sub-array sum with different start point" in the array 
            """
            if count in lookup:
                # beware of it
                if i - lookup[count] > 1:  # if there is any element in the nums that can sum up as k's multiplier and the length of this sub array is at least 2 (>1)
                    return True
            else:
                lookup[count] = i          # get the index of each sum 

        return False

# V0''
# IDEA : BRUTE FROCE (TIME OUT ERROR)
class Solution(object):
    def checkSubarraySum(self, nums, k):
        _dict = {}
        tmp = 0
        cache = []
        j = 1
        for i in range(len(nums)):
            tmp = sum(nums[:i])
            cache.append(tmp)
            if tmp not in _dict:
                _dict[tmp] = 1
            else:
                _dict[tmp] += 1
            if tmp % k == 0
                return True
            elif i > 1:
                for j in range(0, i):
                    if cache[j] - cache[j-1] % j == 0:
                        return True
        return False
      
# V1 
# http://bookshadow.com/weblog/2017/02/26/leetcode-continuous-subarray-sum/
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dmap = {0 : -1}
        total = 0
        for i, n in enumerate(nums):
            total += n
            m = total % k if k else total
            if m not in dmap: dmap[m] = i
            elif dmap[m] + 1 < i: return True
        return False

# V1'
# https://leetcode.com/problems/continuous-subarray-sum/discuss/236976/Python-solution
class Solution():
    def checkSubarraySum(self, nums, k):
        dic = {0:-1}
        summ = 0
        for i, n in enumerate(nums):
            if k != 0:
                summ = (summ + n) % k
            else:
                summ += n
            if summ not in dic:
                dic[summ] = i
            else:
                if i - dic[summ] >= 2:
                    return True
        return False

# V1''
# https://www.jiuzhang.com/solution/continuous-subarray-sum/#tag-highlight-lang-python
class Solution:
    # @param {int[]} A an integer array
    # @return {int[]}  A list of integers includes the index of the 
    #                  first number and the index of the last number
    def continuousSubarraySum(self, A):
        ans = -0x7fffffff
        sum = 0
        start, end = 0, -1
        result = [-1, -1]
        for x in A:
            if sum < 0:
                sum = x
                start = end + 1
                end = start
            else:
                sum += x
                end += 1
            if sum > ans:
                ans = sum
                result = [start, end]
        return result

# V2 
# Time:  O(n)
# Space: O(k)
class Solution(object):
    def checkSubarraySum(self, nums, k):
        count = 0
        lookup = {0: -1}
        for i, num in enumerate(nums):
            count += num
            if k:
                count %= k
            if count in lookup:
                if i - lookup[count] > 1:
                    return True
            else:
                lookup[count] = i
        return False
