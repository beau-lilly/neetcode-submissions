class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        def str_encoder(word):
            enc = [0] * 26
            for ch in word:
                enc[ord(ch) - ord("a")] += 1
            return tuple(enc)

        for word in strs:
            key = str_encoder(word)
            if key not in hashmap:
                hashmap[key] = []
            hashmap[key].append(word)

        return list(hashmap.values())