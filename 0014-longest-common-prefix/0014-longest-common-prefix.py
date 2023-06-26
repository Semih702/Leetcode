class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=""
        if not strs[0]:
            return ""
        for i in range(min(len(s) for s in strs)):
            if len(set(j[i] for j in strs))==1:
                prefix+=strs[0][i]
            else:
                return prefix
        return prefix