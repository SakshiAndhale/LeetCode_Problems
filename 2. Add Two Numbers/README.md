# Add Two Numbers

## Problem Description 📄
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

## Difficulty Level
![Difficulty](https://via.placeholder.com/20/FFA500/000000?text=+) Medium

## Code Explanation 🧑‍💻

**Solution Approach:**

**Step 1:**  
Define the `ListNode` class to represent each node in a singly linked list. Each node has a value (`val`) and a pointer to the next node (`next`).

**Step 2:**  
In the `Solution` class, the `addTwoNumbers` method is implemented to add two numbers represented by the linked lists `l1` and `l2`. A `dummy` node is used to simplify the process of building the resultant linked list. A `carry` variable is used to handle cases where the sum of the nodes exceeds 9.

**Step 3:**  
The method iterates through both linked lists (`l1` and `l2`) until all nodes and the carry are processed. For each iteration:
- The values of the current nodes from `l1` and `l2` are added along with the carry.
- The carry is updated, and the resulting digit is added to the result linked list.

**Step 4:**  
The resultant linked list is returned, which represents the sum of the two input numbers.


## Test Cases ✅
| Input                          | Expected Output | Explanation                                                        |
|--------------------------------|-----------------|--------------------------------------------------------------------|
| l1 = [2,4,3], l2 = [5,6,4]     | [7,0,8]         | The sum is 342 + 465 = 807, which is represented as [7,0,8] in reverse order. |
| l1 = [0], l2 = [0]             | [0]             | Both numbers are 0, so the sum is also 0.                          |
| l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] | [8,9,9,9,0,0,0,1] | The sum is 9999999 + 9999 = 10009998, represented as [8,9,9,9,0,0,0,1]. |

## Ranking
![Screenshot 2024-08-14 232105](https://github.com/user-attachments/assets/640027e3-bde1-41a0-9f2f-a056e0b13fff)

