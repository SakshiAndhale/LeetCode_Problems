class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # If the list is empty, return an empty string
        if not strs:
            return ""
        
        # Assume the first string is the common prefix
        prefix = strs[0]
        
        # Iterate over the other strings in the list
        for s in strs[1:]:
            # While the current string doesn't start with the prefix, shorten the prefix
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # Remove the last character from the prefix
                # If the prefix becomes empty, return an empty string
                if not prefix:
                    return ""
        
        # Return the common prefix after iterating through all strings
        return prefix
