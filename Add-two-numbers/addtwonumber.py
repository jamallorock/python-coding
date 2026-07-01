from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry

            carry = total // 10
            digit = total % 10

            current.next = ListNode(digit)

            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


def build_linked_list(values):
    dummy = ListNode(0)
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def linked_list_to_list(node):
    values = []

    while node:
        values.append(node.val)
        node = node.next

    return values

def main():
    l1 = build_linked_list([1, 3, 5, 6])
    l2 = build_linked_list([1, 2, 1, 1])

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    print(linked_list_to_list(result))

if __name__ == "__main__":
    main()
