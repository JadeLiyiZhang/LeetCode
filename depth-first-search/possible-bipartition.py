class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        table = defaultdict(list)
        for a, b in dislikes:
            table[a].append(b)
            table[b].append(a)

        # color: 0: not processed yet; 1: group 1; 2: group 2
        color = [0] * (n + 1)
        for i in range(n + 1):
            if color[i] == 0:
                color[i] = 1
                q = deque([i])
                while q:
                    cur_person = q.popleft()
                    for dislike in table[cur_person]:
                        if color[dislike] == 0:
                            color[dislike] = 3 - color[cur_person]
                            q.append(dislike)
                        elif color[dislike] == color[cur_person]:
                            return False
        return True