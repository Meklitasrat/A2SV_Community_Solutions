class Solution:
    def isPalindrome(self, x: int) -> bool:
        xx = str(x)

        pali= xx[::-1]

        return (pali == xx)
        
