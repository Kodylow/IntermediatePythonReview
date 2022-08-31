# Given 2 strings s1 and s2, check if they're anagrams.
# Two strings are anagrams if they're made of the same characters with the same frequencies.
from collections import Counter

def valid_anagram(s1, s2):
    if len(s1) != len(s2):
        return False

    # One line with Counter
    # O(n) time and space complexity
    # return Counter(s1) == Counter(s2)

    # One line with sorted
    # O(nlogn) time complexity, O(n) space complexity
    # return sorted(s1) == sorted(s2)

    # Multiple lines building Hash Table
    # O(n) time and space complexity
    freq1 = {}
    freq2 = {}
    for ch in s1:
        try:
            freq1[ch] += 1
        except:
            freq1[ch] = 1
    for ch in s2:
        try:
            freq2[ch] += 1
        except:
            freq2[ch] = 1
    return freq1 == freq2

print(valid_anagram('danger', 'garden'))