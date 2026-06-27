class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not len(s):
            return True

        # new_string = "".join(char for char in s if char.isalnum())
        new_string = re.sub(r"[^a-zA-Z0-9]", "", s)
        new_string = new_string.replace(' ','').strip().lower()
        
        i = 0
        j = len(new_string)-1
        while i<=j:
            if new_string[i]!=new_string[j]:
                return False
            i+=1
            j-=1

        return True

        
