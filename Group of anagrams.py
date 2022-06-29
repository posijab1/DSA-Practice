from collections import defaultdict

def group_of_anagrams(anagrams_seq):

    ans = defaultdict(list)

    for i in anagrams_seq:
        abc = [0] * 26
        for n in i:
            abc[ord(n) - ord('a')] += 1
        ans[tuple(abc)].append(i)

    return ans.values()


print(group_of_anagrams(["eat","tea","tan","ate","nat","bat"]))
