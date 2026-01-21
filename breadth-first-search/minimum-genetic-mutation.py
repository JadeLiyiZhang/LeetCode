from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        seen = set(startGene)
        queue = deque([(startGene, 0)])
        while queue:
            curr, step = queue.popleft()
            if curr == endGene:
                return step
            
            for i in range(len(curr)):
                for char in "ACGT":
                    new_word = curr[:i] + char + curr[i + 1:]
                    if new_word not in seen and new_word in bank:
                        queue.append([new_word, step + 1])
                        seen.add(new_word)
        
        return -1
