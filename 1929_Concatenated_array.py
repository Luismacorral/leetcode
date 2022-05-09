def getConcatenation(nums):
        ans = []
        print(range(len(nums)))
        
        for j in nums*2:
            ans.append(j)
        return ans

print(getConcatenation([1,2,3,4]))