# montako halkaisukohtaa joissa vasen ja oikea summa on sama
def count(t):
    n = len(t)
    count = 0
    for i in range(n-1):
        if sum(t[0:i+1]) == sum(t[i+1:]):
            count += 1
    return count


def count2(t):
    n = len(t)
    left_sum = [0]*n
    left_sum[0] = t[0]
    for i in range(1,n):
        left_sum[i] = left_sum[i-1]+t[i]

    right_sum = [0]*n
    right_sum[-1] = t[-1]
    for i in range(n-2, -1, -1):
        right_sum[i] = right_sum[i+1]+t[i]

    count = 0
    for i in range(n-1):
        if left_sum[i] == right_sum[i+1]:
            count += 1
    return count
print(count2([1,-1,1,-1,1,-1])) # 2
print(count2([1,-1]*50000)) # 49999
