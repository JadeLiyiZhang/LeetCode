class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]
        elif rowIndex==1:
            return [1,1]
        
        res=[[1],[1,1]]
        
        
        for i in range(1,rowIndex):
            g=[0]*(len(res[i])+1)
            
            g[0],g[-1]=1,1
            for j in range(1,len(g)-1):
                g[j]=res[i][j-1]+res[i][j]
            res.append(g)
            
        return res[-1]
        