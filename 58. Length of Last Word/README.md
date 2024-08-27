# 58. Length of Last Word

## Problem Description 📄

Given a string `s` consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

### Example 1:
**Input:** s = "Hello World"  
**Output:** 5  
**Explanation:** The last word is "World" with length 5.

### Example 2:
**Input:** s = "   fly me   to   the moon  "  
**Output:** 4  
**Explanation:** The last word is "moon" with length 4.

### Example 3:
**Input:** s = "luffy is still joyboy"  
**Output:** 6  
**Explanation:** The last word is "joyboy" with length 6.

### Constraints:
- 1 <= s.length <= 10<sup>4</sup>
- `s` consists of only English letters and spaces `' '`.
- There will be at least one word in `s`.

## Difficulty Level
🟢 Easy

## Code Explanation 🧑‍💻

**Solution Approach:**

The solution is implemented using a class `Solution` with a method `lengthOfLastWord`. This approach is consistent with coding platforms like LeetCode, which often require solutions to be encapsulated in a class.

**Step 1:**  
We start by defining the method `lengthOfLastWord` inside the class `Solution`. The method takes one argument `s`, which is the input string.

**Step 2:**  
Within the method, we use the `rstrip()` method to remove any trailing spaces from the string `s`. This ensures that we only consider actual words when finding the last word.

**Step 3:**  
We split the trimmed string into a list of words using the `split()` method. This splits the string at any whitespace and returns a list of words.

**Step 4:**  
We access the last word in the list using `words[-1]`, which gives the last element of the list.

**Step 5:**  
We return the length of the last word using the `len()` function.

**Edge Cases Considered:**
- Trailing spaces in the string.
- Multiple spaces between words.
- Single-word strings, which are directly evaluated for length.

## Test Cases ✅
| Input                         | Expected Output | Explanation                                                      |
|-------------------------------|-----------------|------------------------------------------------------------------|
| "Hello World"                 | 5               | The last word is "World" which has 5 characters.                 |
| "   fly me   to   the moon  " | 4               | The last word is "moon" which has 4 characters.                  |
| "luffy is still joyboy"       | 6               | The last word is "joyboy" which has 6 characters.                |


<div> **Ranking**
![Screenshot 2024-08-27 192232](https://github.com/user-attachments/assets/c4dde108-ae5e-4cd1-bac0-dd5dc4b5ddd1) </div>
