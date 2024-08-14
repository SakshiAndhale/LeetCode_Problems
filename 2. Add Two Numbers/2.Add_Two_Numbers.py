# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        # Initialize the node with a value and a pointer to the next node
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # Create a dummy node that will serve as the starting point of the result linked list
        dummy = ListNode()
        # Initialize the current node to dummy and carry to 0
        current = dummy
        carry = 0

        # Loop until both l1 and l2 are exhausted and no carry is left
        while l1 or l2 or carry:
            # If l1 is not None, take its value, otherwise take 0
            v1 = l1.val if l1 else 0
            # If l2 is not None, take its value, otherwise take 0
            v2 = l2.val if l2 else 0

            # Calculate the sum of l1, l2, and carry
            val = v1 + v2 + carry

            # Update the carry for the next addition
            carry = val // 10
            # The new digit is the remainder of val divided by 10
            val = val % 10
            # Create a new node with the computed value and attach it to the result linked list
            current.next = ListNode(val)
            
            # Move the current pointer to the next node
            current = current.next
            # Move to the next node in l1, if it exists
            l1 = l1.next if l1 else None
            # Move to the next node in l2, if it exists
            l2 = l2.next if l2 else None

        # Return the result linked list, starting from the next node of dummy (skipping the initial dummy node)
        return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(arr):
    # Create a dummy node to start the linked list
    dummy = ListNode()
    # Initialize the current node to dummy
    current = dummy
    # Loop through each number in the list
    for num in arr:
        # Create a new node with the current number and attach it to the list
        current.next = ListNode(num)
        # Move the current pointer to the next node
        current = current.next
    # Return the linked list starting from the node after dummy
    return dummy.next

# Helper function to print the linked list
def print_linked_list(node):
    # Loop through the linked list until the end is reached
    while node:
        # Print the value of the current node
        print(node.val),
        # Move to the next node
        node = node.next
    # Print a new line at the end
    print

# Create linked lists l1 and l2 from the provided lists
l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])

# Create a solution object and use it to add the two numbers
solution = Solution()
result = solution.addTwoNumbers(l1, l2)

# Print the result linked list
print_linked_list(result)  # Output: 7 0 8
