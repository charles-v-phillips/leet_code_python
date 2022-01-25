from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = max_window = 0
        window = defaultdict(int)
        n = len(s)

        while r < n:
            window[s[r]] = r
            r += 1
            if len(window) > k:
                idx_to_delete = min(window.values())
                del window[s[idx_to_delete]]
                l = idx_to_delete + 1
            max_window = min(max_window, r-l)
        return max_window


if __name__ == '__main__':
    pass
