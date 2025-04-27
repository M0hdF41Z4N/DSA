def Z_Function(s):
    n = len(s)
    Z = [0]*n # Initialize Z array
    L , R = 0 , 0  # Initialize window [L, R]

    for i in range(1,n):
        # i is inside the current [L, R] window
        if i<=R:
            Z[i] = min(R-i+1,Z[i-L])
        # Try to extend Z[i] beyond the window
        while i + Z[i] < n and s[Z[i]] == s[i+Z[i]]:
            Z[i] += 1
        # Update [L, R] if we expanded past R
        if i+Z[i]-1 > R:
            L , R = i , i+Z[i]-1
    return Z

# Create new string after concanating pattern 
# with text seprating them with deliminator
new_str = pattern+"$"+text
Z = Z_Function(new_str)

pattern_len = len(pattern)
for i in range(len(new_str)):
    if pattern_len == Z[i]:
        return i-pattern_len-1
