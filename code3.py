"""Take 2 strings s1 and s2 including only letters from a to z.
Return a new sorted string, the longest possible, containing distinct letters,
each taken only once - coming from s1 or s2."""

def longest(s1, s2):
    s_super = "abcdefghijklmnopqrstuvwxyz"
    s_total = ''
    for el in s_super:
        if s1.find(el) != -1:
            s_total = s_total + el
        elif s2.find(el) != -1:
            s_total = s_total + el
    return s_total


print(longest("aretheyhere", "yestheyarehere"))
    # , "aehrsty")