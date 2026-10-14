class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Current implementation leverages Python's built-in conversion:
        # - int(a, 2) converts binary string a to an integer.
        # - int(b, 2) does the same for b.
        # - Adding the two integers yields the sum.
        # - bin(...)[2:] converts the sum back to a binary string (dropping the '0b' prefix).
        #
        # Time Complexity: O(n + m), where n = len(a), m = len(b).
        #   Converting each string to an integer scans all bits, and bin() also scans the result.
        # Space Complexity: O(n + m) for the intermediate integer representations and the output string.
        #
        # This meets the problem's constraints, but a more "manual" approach can achieve O(1) extra space
        # (excluding the output) by iterating from the end of both strings, adding bits with a carry, and
        # building the result in a list. That approach avoids the overhead of big‑integer conversion.
        #
        # If you aim for the optimal in‑place style, consider the following high‑level steps:
        #   1. Initialize a carry = 0 and an empty list for the result.
        #   2. Loop while there are remaining bits in a or b or a non‑zero carry.
        #   3. Sum the current bits (if any) and the carry.
        #   4. Append (sum % 2) to the result list and update carry = sum // 2.
        #   5. After the loop, reverse the result list and join into a string.
        #
        # The current solution is concise and passes all tests, but practicing the manual addition
        # solidifies understanding of binary arithmetic and can be marginally faster for very large inputs.
        return bin(int(a, 2) + int(b, 2))[2:]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna