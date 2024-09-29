def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]

        for s in strs[1:]:
        # shortening the prefix until it matches the start of the current string
            while s[:len(prefix)] != prefix:
            # trimming the last character from the prefix
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix
