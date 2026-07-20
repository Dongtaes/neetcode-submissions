# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        queue = deque([dummy])
        lengthStack = 0
        while head:
            if lengthStack == n:
                queue.popleft()
                queue.append(head)
            else:
                lengthStack += 1
                queue.append(head)
            head = head.next
        
        node = queue.popleft()

        node.next = node.next.next if node.next else None
        return dummy.next