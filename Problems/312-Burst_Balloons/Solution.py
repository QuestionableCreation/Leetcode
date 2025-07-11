class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def Pop(nums:List[int],index:int):
            num1, num2= getNumbers(nums,index)
            coins=num1*num2*nums.pop(index)
            return coins
        
        
        def getNumbers(nums:List[int],index:int): 
            if index-1<0:
                num1=1
            else:
                num1=nums[index-1]
            if index+1>=len(nums):
                num2=1
            else:
                num2=nums[index+1]
            return num1, num2
            
            
        coins=0
        biggest=0
        i=0
        while i< len(nums):
        
            if (nums[i]==1):
                coins+=Pop(nums,i)
            else:
                if nums[i]>nums[biggest]:
                    biggest=i
                i+=1
        
        while nums:
            if biggest==0:
                biggest=1
            coins+=Pop(nums,biggest-1)
            biggest-=1
        
        return coins
            
        


# Main method to run the code
if __name__ == "__main__":
    sol = Solution()
    nums = [3, 1, 5, 8]  # Example input
    result = sol.maxCoins(nums)
    print("Maximum coins:", result)