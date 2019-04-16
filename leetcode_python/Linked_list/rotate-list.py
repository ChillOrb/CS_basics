
# V1 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def rotateRight(self, l, k):
#         l_ = l
#         while k > 0:
#             l_ = l[-1] + l[:-1]
#             k = k - 1 
#             rotateRight(self,l_,k)
#         return l_  
            

# V2 
# Time:  O(n)
# Space: O(1)

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        n, cur = 1, head
        while cur.next:
            cur = cur.next
            n += 1
        cur.next = head

        cur, tail = head, cur
        for _ in range(n - k % n):
            tail = cur
            cur = cur.next
        tail.next = None

        return cur
