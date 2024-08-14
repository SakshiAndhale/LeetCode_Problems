class Solution:
    def twoSum(self, nums, target):
        # Initialize an empty dictionary to store the value and its index
        previousMap = {}  # value : index

        # Loop through the list of numbers with their index
        for i, n in enumerate(nums):
            # Calculate the difference needed to reach the target
            difference_between_numbers = target - n

            # Check if the difference is already in the dictionary
            if difference_between_numbers in previousMap:
                # If it is, return the indices of the two numbers
                return [previousMap[difference_between_numbers], i]
            
            # Otherwise, add the current number and its index to the dictionary
            previousMap[n] = i
        
        # Return an empty list if no solution is found (this case should not happen)
        return []
