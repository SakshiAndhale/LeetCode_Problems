# 14. Longest Common Prefix

## Problem Description 📄
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

## Difficulty Level
🟢 Easy

## Code Explanation 🧑‍💻

**Solution Approach:**

**Step 1:**  
Start by checking if the input list `strs` is empty. If it is, return an empty string since there can be no common prefix.

**Step 2:**  
Assume the first string in the list is the common prefix. This assumption helps us compare this prefix with the rest of the strings in the list.

**Step 3:**  
Iterate over the remaining strings in the list. For each string, check if it starts with the current prefix. If it doesn’t, progressively shorten the prefix by removing its last character until the string starts with this prefix or the prefix becomes empty.

**Step 4:**  
If the prefix becomes empty at any point, return an empty string since no common prefix exists among the strings. Otherwise, after iterating through all the strings, return the resulting prefix, which is the longest common prefix.


## Test Cases ✅
| Input                                        | Expected Output | Explanation                                                           |
|----------------------------------------------|-----------------|-----------------------------------------------------------------------|
| ["flower","flow","flight"]                   | "fl"            | The common prefix "fl" is present in all the input strings.           |
| ["dog","racecar","car"]                      | ""              | There is no common prefix among the input strings.                    |

## Ranking

![Screenshot 2024-08-10 125734](https://github.com/user-attachments/assets/b41a075e-b7b5-4cc9-ae21-adc632deb30c)
