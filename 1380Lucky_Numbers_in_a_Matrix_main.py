# 1380. Lucky Numbers in a Matrix

class Solution:
    def luckyNumbers (self, matrix):
        min_n = {min(rows) for rows in matrix}
        max_n = {max(columns) for columns in zip(*matrix)} 
        
        return list(min_n & max_n)
