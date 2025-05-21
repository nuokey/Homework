def string_to_ascii(s):
    l = len(s)
    if l <= 2:
        if l > 0:
            return ord(s[0])
    elif 2 < l < 10:
        fc = s[0]
        lc = s[-1]

        mi = (l - 1) // 2
        mc = s[mi]
        return ord(fc) + ord(mc) + ord(lc)
    else:
        if l > 0:
            return ord(s[-1])
    
print(string_to_ascii(input()))