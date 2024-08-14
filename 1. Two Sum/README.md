# 1. Two Sum

## Problem Description 📄

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.

- You may assume that each input would have exactly one solution, and you may not use the same element twice.
- You can return the answer in any order.

### Example 1:
- **Input:** `nums = [2,7,11,15]`, `target = 9`
- **Output:** `[0, 1]`
- **Explanation:** Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

### Example 2:
- **Input:** `nums = [3,2,4]`, `target = 6`
- **Output:** `[1, 2]`

### Example 3:
- **Input:** `nums = [3,3]`, `target = 6`
- **Output:** `[0, 1]`

### Constraints:
- `2 <= nums.length <= 10^4`
- `-10^9 <= nums[i] <= 10^9`
- `-10^9 <= target <= 10^9`
- Only one valid answer exists.

## Difficulty Level
![Difficulty](https://via.placeholder.com/20/00FF00/000000?text=+) Easy

## Solution 🧑‍💻

The "Two Sum" problem is a classic example of how to use a hash map (or dictionary) to efficiently find pairs of elements that sum to a given target. The steps of the solution are outlined below:

### Step 1: Initialize a Dictionary
- We start by initializing an empty dictionary called `previousMap` to store the numbers we have seen so far along with their indices.

### Step 2: Iterate Through the Array
- We loop through the array `nums`, and for each element, we calculate the difference between the `target` and the current element.

### Step 3: Check the Dictionary
- For each element, we check if the calculated difference is already in the dictionary. If it is, we have found the two numbers that sum up to the target, so we return their indices.

### Step 4: Update the Dictionary
- If the difference is not found in the dictionary, we add the current number and its index to the dictionary for future reference.

### Step 5: Return the Result
- Once we find the two numbers that sum up to the target, we return their indices as a list.

## Ranking

![Screenshot 2024-08-14 225312](https://github.com/user-attachments/assets/6cace7f4-2839-468f-9614-8678f77c3394)
