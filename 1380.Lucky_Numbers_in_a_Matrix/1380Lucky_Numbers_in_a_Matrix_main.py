# 1380. Lucky Numbers in a Matrix
# 
# Given an m x n matrix of distinct numbers, this function returns all lucky numbers in the matrix in any order.
# 
# A lucky number is defined as an element of the matrix that is both the minimum element in its row and the maximum element in its column.
# 
# This solution works by:
# 1. Identifying the minimum elements in each row and storing them in a set `min_n`.
# 2. Identifying the maximum elements in each column and storing them in a set `max_n`.
# 3. The intersection of these two sets `min_n & max_n` will give us the lucky numbers, as they must satisfy both conditions.
# 4. The result is returned as a list.
# 
# Example:
# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only number that is the minimum in its row and maximum in its column.

class Solution:
    def luckyNumbers(self, matrix):
        # Find the minimum value in each row and store them in a set
        min_n = {min(rows) for rows in matrix}
        
        # Find the maximum value in each column by zipping the matrix to get columns as rows
        max_n = {max(columns) for columns in zip(*matrix)} 

        # The lucky numbers are the intersection of the minimums in rows and maximums in columns
        return list(min_n & max_n)
