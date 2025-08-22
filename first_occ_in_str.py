class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n,m=len(haystack),len(needle)
        if m == 0:
            return 0
        for i in range(n-m+1):
            match=True
            for j in range(m):
                if haystack[i + j]!=needle[j]:
                    match=False
                    break
            if match:
                return i
        return -1
    
sol=Solution()
haystack = "sadbutsad"
needle = "sad"
print(sol.strStr(haystack,needle))
        

# output : 0