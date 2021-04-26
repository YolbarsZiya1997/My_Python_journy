def sum_eo(n,t):
    if t == 'e':
        summ = 0
        for i in range(2,n,2):
            summ += i
        return summ
    elif t == 'o':
        total = 0
        for j in range(1,n,2):
            total += j
        return total
    else:
        return -1
answer = sum_eo(7,'spam')
print(answer)