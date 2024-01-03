class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result=[]
        def try_combo(combination,n,start):
            if(k==len(combination)):
                if(n==0): result.append(combination.copy())
                return
            for i in range(start,10):
                combination.append(i)
                try_combo(combination, n-i,i+1)
                combination.pop()
        try_combo([],n,1)
        return result
            
        