class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq ={}
        for i in nums:
            if i not in freq:
                freq[i] = 0
            freq[i]+=1
        big = -1
        sorted
        freq_sort = sorted(freq, key=lambda i: freq[i], reverse=True)
        return freq_sort[:k]


        