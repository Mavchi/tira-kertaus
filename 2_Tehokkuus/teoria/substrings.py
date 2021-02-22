# monessako osajonossa vierekkäiset merkit peräkkäin aakkosissa?

# O(n^2)
def calc(s):
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i,n):
            if i != j and abs(ord(s[j-1])-ord(s[j])) != 1:
                break
            print(s[i:j+1])
            count += 1
    return count

# O(n)
def calc2(s):
    n = len(s)
    count = 0
    length = 0
    for i in range(n):
        if i != 0 and abs(ord(s[i-1])-ord(s[i])) == 1:
            length += 1
        else:
            length = 1
        count += length
        print('kohtaan', i, 'päättyy', length, 'osajonoa')
        # aabaca
        #    ^ 3 osajonoa päättyy tähän kohtaan
        # aabaca
        #     ^ 1 osajonoa päättyy tähän kohtaan
    return count


#print(calc('aabaca'))
print(calc2('aabaca'))

test_string = "ab"*50000
#print(calc(test_string))
#print(calc2(test_string))
