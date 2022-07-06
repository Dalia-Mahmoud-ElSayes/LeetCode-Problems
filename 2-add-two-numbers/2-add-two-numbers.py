# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        power=0
        L1=0
        L2=0
        
        while l1:
            L1=L1+(l1.val*(10**power))
            power+=1
            l1=l1.next
        power=0
        while l2:
            L2=L2+(l2.val*(10**power))
            power+=1
            l2=l2.next
        sum=str(L1+L2)
        nodes=[]
        for i in range(len(sum)):
            nodes.append(ListNode(val=int(sum[i])))
        for i in range (1,len(nodes)):
            nodes[i].next=nodes[i-1]
        return nodes[-1]            
        