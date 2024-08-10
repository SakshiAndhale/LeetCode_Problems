class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Dictionary to map Roman numerals to their integer values
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Initialize the total to 0
        total = 0
        
        # Traverse through the string, from left to right
        for i in range(len(s)):
            # If the current value is less than the next value, subtract it (for cases like IV, IX)
            if i + 1 < len(s) and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                total -= roman_to_int[s[i]]
            else:
                # Otherwise, add the value
                total += roman_to_int[s[i]]

        return total
