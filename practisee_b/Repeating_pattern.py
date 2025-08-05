def find_repeating_pattern(s):
    n = len(s)
    for i in range(1, n):
        pattern = s[:i]
        if n % i == 0 and pattern * (n // i) == s:
            return pattern
    return s 

print(find_repeating_pattern("abcabcabc"))      
