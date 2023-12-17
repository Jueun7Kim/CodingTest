def solution(s):
    s = list(s)
    s[0] = s[0].upper()
    for i in range(len(s)):
        if s[i-1] == " " or i == 0:
            s[i] = s[i].upper()
        else:
            s[i] = s[i].lower()
            
    return ''.join(s)