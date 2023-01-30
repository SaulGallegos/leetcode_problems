# Solution 1: Hash Map
def isAnagramHasMap(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s = list(s)
    t = list(t)

    s_dict = {}
    t_dict = {}

    for i in range(len(s)):
        if s[i] in s_dict:
            s_dict[s[i]] += 1
        else:
            s_dict[s[i]] = 1

        if t[i] in t_dict:
            t_dict[t[i]] += 1
        else:
            t_dict[t[i]] = 1

    return s_dict == t_dict


# Solution 2: Remove same letters in both lists
def isAnagramOne(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s = list(s)
    t = list(t)

    for i in range(len(s)):
        if s[i] in t:
            t.remove(s[i])
        else:
            return False

    return True

# Solution 3: Sort both lists and compare


def isAnagramTwo(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


print(isAnagramHasMap("anagram", "nagaram"))
print(isAnagramOne("anagram", "nagaram"))
print(isAnagramTwo("anagram", "nagaram"))
