# Lucky Numbers in a Matrix

## Problem Description 📄
Given an m x n matrix of distinct numbers, this function returns all lucky numbers in the matrix in any order.

A lucky number is defined as an element of the matrix that is both the minimum element in its row and the maximum element in its column.

## Difficulty Level
![Difficulty](https://via.placeholder.com/20/00FF00/000000?text=+) Easy

## Code Explanation 🧑‍💻

**Solution Approach:**

**Step 1:**  
Identify the minimum element in each row. This is done by iterating through each row of the matrix and finding the smallest number in that row. The result is stored in a set called `min_n`.

**Step 2:**  
Identify the maximum element in each column. To achieve this, the matrix is transposed using the `zip(*matrix)` function, which allows the columns to be accessed as rows. The largest number in each "column-row" is then found and stored in a set called `max_n`.

**Step 3:**  
The intersection of the two sets `min_n` and `max_n` is computed. The intersection contains all the numbers that are both the minimum in their row and the maximum in their column, which defines the lucky numbers.

**Step 4:**  
Finally, the intersection set is converted into a list and returned as the output of the function.

## Test Cases ✅
| Input                           | Expected Output | Explanation                                                          |
|---------------------------------|-----------------|----------------------------------------------------------------------|
| [[3,7,8],[9,11,13],[15,16,17]]  | [15]            | 15 is the minimum in its row and maximum in its column.               |
| [[1,10,4,2],[9,3,8,7],[15,16,17,12]] | [12]        | 12 is the minimum in its row and maximum in its column.               |
| [[7,8],[1,2]]                   | []              | There are no numbers that satisfy the conditions.                    |

## Ranking

![Screenshot 2024-08-13 195620](https://github.com/user-attachments/assets/d69f6480-9140-4855-94be-c98f77a7de35)

