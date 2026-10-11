class Solution:
    def longestCommonPrefix(self, strs):
        prefix = strs[0]

        for i in range(1, len(strs)):
            word = strs[i]

            while not word.startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return ""

        return prefix