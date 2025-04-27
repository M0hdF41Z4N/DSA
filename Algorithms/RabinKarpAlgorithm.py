def rabin_karp(pattern, text):
    base = 256  # Base for ASCII characters
    modulus = 10**9 + 7  # Large prime to minimize collisions
    m = len(pattern)
    n = len(text)
    
    if m == 0 or m > n:
        return []
    
    # Precompute base^(m-1) mod modulus
    power = pow(base, m-1, modulus)
    
    # Compute hash for pattern and first window of text
    pattern_hash = 0
    text_hash = 0
    for i in range(m):
        pattern_hash = (pattern_hash * base + ord(pattern[i])) % modulus
        text_hash = (text_hash * base + ord(text[i])) % modulus
    
    result = []
    
    # Slide the window over the text
    for i in range(n - m + 1):
        # Check hash match
        if pattern_hash == text_hash:
            # Verify character-by-character to avoid collisions
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                result.append(i)
        
        # Update hash for next window (if not the last iteration)
        if i < n - m:
            # Remove leftmost character's contribution
            text_hash = (text_hash - ord(text[i]) * power) % modulus
            # Shift left and add new rightmost character
            text_hash = (text_hash * base + ord(text[i + m])) % modulus
            # Ensure non-negative hash
            if text_hash < 0:
                text_hash += modulus
    
    return result
