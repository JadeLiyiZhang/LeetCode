# ==========================================================
# 3161. Block Placement Queries
# Difficulty : Hard
# Language   : Python
# Solution   : #1
# Runtime    : 3830 ms (Beats 63%)
# Memory     : 78.6 MB (Beats 91%)
# Link       : https://leetcode.com/problems/block-placement-queries/
# ==========================================================

class Solution:
    def getResults(self, queries: list[list[int]]) -> list[bool]:
        limit = max(query[1] for query in queries)

        # 树状数组：记录哪些位置有障碍物
        bit = [0] * (limit + 2)

        def add(pos, value):
            pos += 1
            while pos < len(bit):
                bit[pos] += value
                pos += pos & -pos

        def count_at_most(pos):
            total = 0
            pos += 1
            while pos > 0:
                total += bit[pos]
                pos -= pos & -pos
            return total

        def kth(k):
            """返回第 k 个障碍物的位置，k 从 1 开始。"""
            pos = 0
            step = 1 << (len(bit).bit_length() - 1)

            while step:
                nxt = pos + step
                if nxt < len(bit) and bit[nxt] < k:
                    k -= bit[nxt]
                    pos = nxt
                step >>= 1

            return pos

        # 线段树：gap[pos] = pos 与左边最近障碍物的距离
        size = 1
        while size <= limit:
            size *= 2
        tree = [0] * (size * 2)

        def update(pos, value):
            index = size + pos
            tree[index] = value
            index //= 2

            while index:
                tree[index] = max(tree[index * 2], tree[index * 2 + 1])
                index //= 2

        def prefix_max(pos):
            """查询位置 0 到 pos 的最大 gap。"""
            left, right = size, size + pos + 1
            result = 0

            while left < right:
                if left & 1:
                    result = max(result, tree[left])
                    left += 1
                if right & 1:
                    right -= 1
                    result = max(result, tree[right])
                left //= 2
                right //= 2

            return result

        # 把 0 当作左边界
        add(0, 1)
        obstacle_count = 1
        answer = []

        for query in queries:
            x = query[1]
            rank = count_at_most(x)

            if query[0] == 1:
                prev = kth(rank)
                nxt = kth(rank + 1) if rank < obstacle_count else None

                # 插入 x 后，原来的大间隙被拆成两段
                update(x, x - prev)
                if nxt is not None:
                    update(nxt, nxt - x)

                add(x, 1)
                obstacle_count += 1

            else:
                length = query[2]
                prev = kth(rank)

                # 完整的障碍物间隙，或最后一个障碍物到 x 的间隙
                largest = max(prefix_max(x), x - prev)
                answer.append(largest >= length)

        return answer