from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = []
        line_len = 0  # sum of word lengths (no spaces)

        def justify(line: List[str], line_len: int, is_last: bool) -> str:
            if is_last or len(line) == 1:
                # left-justified
                s = " ".join(line)
                return s + " " * (maxWidth - len(s))

            total_spaces = maxWidth - line_len
            gaps = len(line) - 1
            base = total_spaces // gaps
            extra = total_spaces % gaps  # left gaps get one more

            parts = []
            for i, w in enumerate(line[:-1]):
                parts.append(w)
                spaces = base + (1 if i < extra else 0)
                parts.append(" " * spaces)
            parts.append(line[-1])
            return "".join(parts)

        for w in words:
            # if we add w, we need at least (len(line)) spaces between words
            if line_len + len(w) + len(line) <= maxWidth:
                line.append(w)
                line_len += len(w)
            else:
                res.append(justify(line, line_len, is_last=False))
                line = [w]
                line_len = len(w)

        # last line
        res.append(justify(line, line_len, is_last=True))
        return res
