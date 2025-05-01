def longest_common_substr(s1: str, s2: str) -> int:
    """
    Computes the length of the longest common substring between two strings s1 and s2

    Example:
        Given s1 = "abcdefg" and s2 = "abcfgh", the longest common substring is "abc"
        and the function will return 3
    """
    # m = len(s1)
    # n = len(s2)

    # res = 0
    # for i in range(m):
    #     for j in range(n):
    #         curr = 0
    #         while (i + curr) < m and (j + curr) < n and s1[i + curr] == s2[j + curr]:
    #             curr += 1
    #         res = max(res, curr)

    # return res

    # Dynamic Programming Approach
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    max_length = 0
    
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
                if dp[i+1][j+1] > max_length:
                    max_length = dp[i+1][j+1]
            else:
                dp[i+1][j+1] = 0
                
    return max_length


def longest_common_prefix(s1: str, s2: str) -> int:
    """
    Computes the length of the longest common prefix between two strings s1 and s2.
    """
    min_length = min(len(s1), len(s2))
    for i in range(min_length):
        if s1[i] != s2[i]:
            return i
    return min_length


def longest_common_suffix(s1: str, s2: str) -> int:
    """
    Computes the length of the longest common suffix between two strings s1 and s2.
    """
    min_length = min(len(s1), len(s2))
    for i in range(1, min_length + 1):
        if s1[-i] != s2[-i]:
            return i - 1
    return min_length


class StringAnalysis:
    """
    A class to analyze relationships between two strings, including their
    longest common substring, prefix, and suffix.
    """

    def __init__(self, s1: str, s2: str):
        self.s1 = s1
        self.s2 = s2

    def analyze(self):
        lcs_length = longest_common_substr(self.s1, self.s2)
        lcpre_length = longest_common_prefix(self.s1, self.s2)
        lcsuf_length = longest_common_suffix(self.s1, self.s2)

        return {
            "String 1": self.s1,
            "String 2": self.s2,
            "Longest Common Substring Length": lcs_length,
            "Longest Common Prefix Length": lcpre_length,
            "Longest Common Suffix Length": lcsuf_length,
        }
