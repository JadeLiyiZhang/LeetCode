class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dist = [[math.inf for _ in range(len(mat[0]))] for _ in range(len(mat))]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    dist[i][j] = 0

                neighbors = []

                if i > 0:
                    neighbors.append(dist[i-1][j])
                if j > 0:
                    neighbors.append(dist[i][j-1])

                dist[i][j] = min(min(neighbors)+1, dist[i][j]) if neighbors else dist[i][j]

        for i in range(len(mat)-1, -1, -1):
            for j in range(len(mat[0])-1, -1, -1):
                if mat[i][j] == 0:
                    dist[i][j] = 0

                neighbors = []

                if i < len(mat)-1:
                    neighbors.append(dist[i+1][j])
                if j < len(mat[0])-1:
                    neighbors.append(dist[i][j+1])

                dist[i][j] = min(min(neighbors)+1, dist[i][j]) if neighbors else dist[i][j]

        return dist     