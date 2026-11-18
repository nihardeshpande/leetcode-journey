class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        #using the bucket sort method so that the array indices  are the count of elements and the values are the elements occuring that many times
        freq = [[] for i in range (len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range (len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res