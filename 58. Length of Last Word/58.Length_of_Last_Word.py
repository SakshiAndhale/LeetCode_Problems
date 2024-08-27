class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Step 1: Strip any trailing spaces from the string
        s = s.rstrip()
        
        # Step 2: Split the string into a list of words based on spaces
        words = s.split()
        
        # Step 3: Get the last word from the list
        last_word = words[-1]
        
        # Step 4: Return the length of the last word
        return len(last_word)

# Testing the function with the given examples
solution = Solution()
print(solution.lengthOfLastWord("Hello World"))  # Output: 5
print(solution.lengthOfLastWord("   fly me   to   the moon  "))  # Output: 4
print(solution.lengthOfLastWord("luffy is still joyboy"))  # Output: 6
