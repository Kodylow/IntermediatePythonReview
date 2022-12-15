# Given two strings s and t, find the shortest substring of s that contains all characters of t

def contains_all(freq1, freq2):
    for ch in freq2:
        if freq1[ch] < freq2[ch]:
            return False
    return True

# Brute Force
# O(n^3) Time Complexity
# O(n+m) Space Complexity
def min_window_brute_force(s, t):
    n, m = len(s), len(t)
    if m > n or m == 0:
        return ""
    freqt = Counter(t)
    shortest = " "*(n+1)
    for length in range(1, n+1):
        for i in range(n-length+1):
            sub = s[i:i+length]
            freqs = Counter(sub)
            if contains_all(freqs, freqt) and length < len(shortest):
                shortest = sub
    return shortest if len(shortest) <= n else ""

# Optimization 1: Instead of extracting and storing the substring itself, we just work with its start and end indexes
# Optimization 2: Don't rebuild Counter every time, use a Sliding Window
# Optimizating 3: Check if substring is valid. Don't recheck everything: eep track of how many conditions are satisfied, and if for a specific substring all of them become satisfied, then it's valid

freqs[went_in] += 1
if went_in in freqt and freqs[went_in] == freqt[went_in]:
    satisfied += 1
if went_out in freqt and freqs[went_out] == freqt[went_out]:
    satisfied -= 1
freqs[went_out] -= 1

# O(n^2) Time Complexity
# O(n+m) Time Complexity
def min_window_sliding(s,t):
    n, m = len(s), len(t)
    if m > n or t =="":
        return ""
    freqt = Counter(t)
    start, end = 0, n+1
    for length in range(1, n+1):
        freqs = Counter()
        satisfied = 0
        for ch in s[:length]:
            freqs[ch] += 1
            if ch in freqt and freqs[ch] == freqt[ch]:
                satisfied += 1
        if satisfied == len(freqt) and length < end-start:
            start, end = 0, length
        for i in range(1, n-length+1):
            freqs[s[i+length-1]] += 1
            if s[i+length-1] in freqt and freqs[s[i+length-1]] == freqt[s[i+length-1]]:
                satisfied += 1
            if s[i-1] in freqt and freqs[s[i-1]] == freqt[s[i-1]]:
                satisfied -= 1
            freqs[s[i-1]] -= 1
            if satisfied == len(freqt) and length < end-start:
                start, end = i, i+length
    return s[start:end] if end-start <= n else ""

# Optimization 4: Manipulate sliding window differently. ID chars we can remove to shorten the valid substring, after right shift try removing left chars until you can't
# O(n + m) Time Complexity
def min_window_left_slide_optimized(s,t):
    n, m = len(s), len(t)
    if m > n or t == "":
        return ""
    freqt = Counter(t)
    start, end = 0, n
    satisfied = 0
    freqs = Counter()
    left = 0
    for right in range(n):
        freqs[s[right]] += 1
        if s[right] in freqt and freqs[s[right]] == freqt[s[right]]:
            satisfied += 1
        if satisfied == len(freqt):
                while s[left] not in freqt or freqs[s[left]] > freqt[s[left]]:
                    freqs[s[left]] -= 1
                    left += 1
                if right-left+1 < end-start+1:
                    start, end = left, right
    return s[start:end+1] if end-start+1 <= n else ""