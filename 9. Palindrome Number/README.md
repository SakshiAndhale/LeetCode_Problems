# PALINDROME NUMBER

# Problem Description 📄

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
Constraints:

-231 <= x <= 231 - 1


# Difficulty Level
- !#00FF00 'Easy'
- !#c5f015 `#c5f015`

# Code Explanation 🧑‍💻

Solution Approach:

Step 1:
Check if the given integer x is negative. If x is negative, it cannot be a palindrome since the negative sign would appear at the beginning of the number when read from left to right, and at the end when read from right to left. Therefore, we immediately return False for negative numbers.

Step 2:
Convert the integer x into a string. This allows us to easily reverse the sequence of digits and compare the original sequence with its reverse. This is done using the str(x) function in Python, which converts the integer to a string representation.

Step 3:
Reverse the string using Python’s slicing syntax [::-1]. This syntax reads the string from end to start, effectively reversing it. We then compare this reversed string with the original string to check if they are the same.

Step 4:
Return True if the original string and the reversed string are identical, indicating that x is a palindrome. Otherwise, return False. The chosen approach is efficient and straightforward, leveraging Python's built-in string manipulation capabilities.

# Find the Python Code Above

# Ranking
![Screenshot 2024-08-09 233201](https://github.com/user-attachments/assets/3784f66c-d55c-4e37-9ba5-392d0644cc44)
