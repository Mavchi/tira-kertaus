# mikä on pisin kahden saman merkin etäisyys?

# O(n^2)
def calc(s):
    n = len(s)
    distance = 0
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j]:
                #print('kohdat', i ,'ja', j, 'etäisyys', j-i)
                distance = max(distance, j-i)
    return distance

def calc2(s):
    n = len(s)
    distance = 0
    first = {}
    for i in range(n):
        if s[i] in first:
            distance = max(distance, i-first[s[i]])
        else:
            first[s[i]] = i
    print(first)
    return distance

print(calc2('abccacdb'))

s = 'ab'*50000
print(calc2(s))
