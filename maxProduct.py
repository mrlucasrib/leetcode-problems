class Solution:
    def maxProduct(self, nums: int) -> int:
        prodMax = nums[0]
        indexFirstNeg = 0 if nums[0] < 0 else -1
        accNeg = [0]
        accAfterFirstNeg = 1
        for n in range(len(nums) - 1, 0, -1):
            if nums[n] < 0:
                accNeg.append(accNeg[-1] + 1)
            elif nums[n] == 0:
                accNeg.append(0)
            else:
                accNeg.append(accNeg[-1])
        accNeg.reverse()

        currProd = 0 if accNeg[0] == 0 and nums[0] < 0 else nums[0]


        for i in range(1, len(nums)):
            if nums[i] == 0:
                currProd = nums[i]
                accAfterFirstNeg = 1
                indexFirstNeg = -1
            elif nums[i] < 0:
                if accNeg[i] > 0 or currProd < 0:
                    currProd = currProd * nums[i] if currProd != 0 else nums[i]
                else:
                    if accAfterFirstNeg != 1:
                        currProd = nums[i] * accAfterFirstNeg if currProd != 0 else nums[i]
                    else: currProd = 0
            else:
                currProd = currProd * nums[i] if currProd != 0 else nums[i]


            if currProd > prodMax:
                prodMax = currProd
        
            if indexFirstNeg != -1:
                accAfterFirstNeg *= nums[i]
            else:
                indexFirstNeg = i if nums[i] < 0 else -1
            

        return prodMax
print(Solution().maxProduct([3,-1,4]), 4)
print(Solution().maxProduct([-2,0,-1]), 0)
print(Solution().maxProduct([1,0,-1,2,3,-5,-2]), 60)
print(Solution().maxProduct([-1,1,2,1]), 2)
print(Solution().maxProduct([2,3,-2,4]), 6)
print(Solution().maxProduct([-2,1,0,-3]), 1)