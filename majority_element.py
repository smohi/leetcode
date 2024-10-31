def majorityElement(self, nums: List[int]) -> int:
        maj_can, count = None, 0
    
        for num in nums:
            if count == 0:
                maj_can = num
            count += (1 if num == maj_can else -1)
        
        return maj_can
