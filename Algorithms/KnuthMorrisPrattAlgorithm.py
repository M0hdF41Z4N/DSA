def Knuth–Morris–Pratt(needel,haystack)
    # Also known as : KMP Algo
    # Edge case: empty pattern
    if not needle:
        return 0

    pattern_length = len(needle)
    text_length = len(haystack)
    lps = [0] * pattern_length  # Longest Prefix Suffix array
    
    # shifting the patter by 1 indices for resetting
    pattern = " " + needle
    lps = [0] * (pattern_length+1) # Longest proper prefix

    # Compute LPS array
    # j : prefix index
    # i : suffix index
    j = 0
    for i in range(1, pattern_length):
        while j > 0 and needle[i] != needle[j]:
            j = lps[j-1]
        if needle[i] == needle[j]:
            j += 1
            lps[i] = j

    
    
    j = 0 # index for needle
    # i : text index
    for i in range(text_length):
        # Keep resetting to the existing prefix
        while j > 0 and haystack[i] != needle[j]:
            j = lps[j-1]
        # increasing pattern iterator in case of matching
        if haystack[i] == needle[j]:
            j += 1
        # pattern found
        if  j==pattern_length:
            return i-pattern_length+1
    return -1
