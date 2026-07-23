class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # nlogn basically sort the string at the position i and add it to the dictionary. 
        # sort it to the size first meaning 1 size is e.g. in a bucket in on ofitself than do a search in this bucket in the groups
        # create like dict of dict, key = freq list with a dictionary and then value is the fitting elements in the list
        # e.g {c=1, a=1, t=1} = [cat, act]  a c t -> hash  nlogm m is the size of the string itself

        res = defaultdict(list)

        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            res[tuple(count)].append(s)
        return list(res.values())