def ManachersAlgo(string):
  t = '#' + '#'.join(string) + '#'
  n = len(t)
  p = [0] * n  # Array to hold radius of palindrome around each center
  center = 0
  right = 0
  max_len = 0
  max_center = 0

  for i in range(n):
      mirror = 2 * center - i  # Mirror position of i around center

      if i < right:
          p[i] = min(right - i, p[mirror])

      # Expand palindrome centered at i
      a = i + p[i] + 1
      b = i - p[i] - 1
      while a < n and b >= 0 and t[a] == t[b]:
          p[i] += 1
          a += 1
          b -= 1

      # Update center and right boundary if palindrome expanded past right
      if i + p[i] > right:
          center = i
          right = i + p[i]

      # Track max palindrome length and center
      if p[i] > max_len:
          max_len = p[i]
          max_center = i

  # Extract the longest palindrome from the original string
  start = (max_center - max_len) // 2  # Map back to original string indices
  return s[start:start + max_len]
