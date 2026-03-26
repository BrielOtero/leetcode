from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """
        time: O(n * k log k)
        space: O(1)
        approach: sorting with hash map
        """
        grouped: defaultdict[str, list[str]] = defaultdict(list)

        for string in strs:
            key = "".join(sorted(string))

            grouped[key].append(string)

        return list(grouped.values())
