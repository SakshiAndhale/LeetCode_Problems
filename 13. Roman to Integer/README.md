# 13. Roman to Integer

## Problem Description 📄

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

### Example 1:
**Input:** s = "III"  
**Output:** 3  
**Explanation:** III = 3.

### Example 2:
**Input:** s = "LVIII"  
**Output:** 58  
**Explanation:** L = 50, V = 5, III = 3.

### Example 3:
**Input:** s = "MCMXCIV"  
**Output:** 1994  
**Explanation:** M = 1000, CM = 900, XC = 90, IV = 4.

### Constraints:
- 1 <= s.length <= 15
- s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- It is guaranteed that s is a valid Roman numeral in the range [1, 3999].

## Difficulty Level
🟢 Easy

## Code Explanation 🧑‍💻

**Solution Approach:**

**Step 1:**  
We start by defining a dictionary `roman_to_int` that maps each Roman numeral character to its corresponding integer value. This helps in quickly looking up the integer value of any Roman numeral symbol.

**Step 2:**  
We initialize a variable `total` to store the resulting integer value as we process the Roman numeral string.

**Step 3:**  
We iterate through the string `s` from left to right. During each iteration, we check if the current numeral is less than the next one. If it is, we subtract the current numeral's value from `total` (to handle cases like `IV` or `IX`). Otherwise, we add the current numeral's value to `total`.

**Step 4:**  
Finally, we return `total`, which now holds the integer equivalent of the Roman numeral string.

**Edge Cases Considered:**
- Roman numerals with subtraction cases (e.g., `IV`, `IX`, `XL`).
- Single-character strings, which are always directly converted to their integer equivalents.


## Test Cases ✅
| Input     | Expected Output | Explanation |
|-----------|-----------------|-------------|
| "III"     | 3               | III is the sum of three I's (1 + 1 + 1). |
| "LVIII"   | 58              | L = 50, V= 5, III = 3. |
| "MCMXCIV" | 1994            | M = 1000, CM = 900, XC = 90, IV = 4, so total = 1994. |

## Ranking

![Screenshot 2024-08-10 123912](https://github.com/user-attachments/assets/f8dc09aa-f42c-4745-94ed-e278d822da5a)

