class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = [[-1] * len(s) for _ in range(len(s))]
        return self.dfs(0, 0, s, memo)

    def dfs(self, index, open_count, s, memo):
        if index == len(s):
            return open_count == 0
        if memo[index][open_count] != -1:
            return memo[index][open_count] == 1
        is_valid = False
        if s[index] == "*":
            # take "*" as "("
            is_valid |= self.dfs(index + 1, open_count + 1, s, memo)
            # take "*" as ")"
            if open_count > 0:
                is_valid |= self.dfs(index + 1, open_count - 1, s, memo)
            # take "*" as ""
            is_valid |= self.dfs(index + 1, open_count, s, memo)
        elif s[index] == "(":
            is_valid = self.dfs(index + 1, open_count + 1, s, memo)
        else:
            if open_count > 0:
                is_valid = self.dfs(index + 1, open_count - 1, s, memo)
        memo[index][open_count] = 1 if is_valid else 0
        return is_valid