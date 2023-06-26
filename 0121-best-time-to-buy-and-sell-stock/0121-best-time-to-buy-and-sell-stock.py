class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest=prices[0]
        maks=0
        for i in prices:
            if i>lowest:
                maks=max(i-lowest,maks)
            else:
                lowest=i
        return maks
