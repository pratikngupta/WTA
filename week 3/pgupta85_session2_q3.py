"""
    Nane: Pratik Narendra Gupta
    Program: Software Engineering - 3rd year
"""

"""
Question 3
You are given two non-empty linked lists that represent two non-negative integers. The digits of each integer are stored in reverse order, and each node in the linked list contains a single digit. Your task is to add the two numbers represented by these linked lists and return the sum as a new linked list.

You can assume that the input linked lists do not contain any leading zeros, except the number 0 itself. 

Example:
Input: 
Linked List 1 = 7->8->2, Linked List 2 = 8->4->3
Output:
Linked List Result = 5->3->6
Explanation
287 + 348 = 635
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(list_1, list_2):
    carry = 0
    dummy = ListNode()
    current = dummy

    while list_1 or list_2:
        val1 = list_1.val if list_1 else 0
        val2 = list_2.val if list_2 else 0

        total_sum = val1 + val2 + carry
        carry = total_sum // 10
        current.next = ListNode(total_sum % 10)
        current = current.next

        if list_1:
            list_1 = list_1.next
        if list_2:
            list_2 = list_2.next

    if carry:
        current.next = ListNode(carry)

    return dummy.next


# Helper function to convert a list to a linked list in reverse order
def list_to_linkedlist(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list in reverse order
def linkedlist_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst

if __name__ == "__main__":
    # Test case 1
    print("Test case 1")
    l1 = list_to_linkedlist([7, 8, 2])
    l2 = list_to_linkedlist([8, 4, 3])
    result = addTwoNumbers(l1, l2)
    print("Input:")
    print("Linked List 1 =", linkedlist_to_list(l1), "Linked List 2 =", linkedlist_to_list(l2))
    print("Output:")
    print("Linked List Result =", linkedlist_to_list(result))
    assert linkedlist_to_list(result) == [5, 3, 6]

    # Test case 2
    print("\nTest case 2")
    l1 = list_to_linkedlist([2, 4, 3])
    l2 = list_to_linkedlist([5, 6, 4])
    result = addTwoNumbers(l1, l2)
    print("Input:")
    print("Linked List 1 =", linkedlist_to_list(l1), "Linked List 2 =", linkedlist_to_list(l2))
    print("Output:")
    print("Linked List Result =", linkedlist_to_list(result))
    assert linkedlist_to_list(result) == [7, 0, 8]

    # Test case 3
    print("\nTest case 3")
    l1 = list_to_linkedlist([0])
    l2 = list_to_linkedlist([0])
    result = addTwoNumbers(l1, l2)
    print("Input:")
    print("Linked List 1 =", linkedlist_to_list(l1), "Linked List 2 =", linkedlist_to_list(l2))
    print("Output:")
    print("Linked List Result =", linkedlist_to_list(result))
    assert linkedlist_to_list(result) == [0]

    # Test case 4
    print("\nTest case 4")
    l1 = list_to_linkedlist([9, 9, 9, 9, 9, 9, 9])
    l2 = list_to_linkedlist([9, 9, 9, 9])
    result = addTwoNumbers(l1, l2)
    print("Input:")
    print("Linked List 1 =", linkedlist_to_list(l1), "Linked List 2 =", linkedlist_to_list(l2))
    print("Output:")
    print("Linked List Result =", linkedlist_to_list(result))
    assert linkedlist_to_list(result) == [8, 9, 9, 9, 0, 0, 0, 1]



