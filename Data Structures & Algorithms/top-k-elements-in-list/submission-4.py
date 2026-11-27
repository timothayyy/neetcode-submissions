class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        top_k = heapq.nlargest(k, count, key=count.get)
            
        return top_k

        
        
        
        

            
                
                    
            

            

        



        