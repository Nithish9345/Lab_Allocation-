def lab_alloction(l,n):
    m = l[0]-n
    f = "L1"
    if(l[1]-n>=0 and l[1]-n<m):
        m = l[1]-n
        f = "L2"
    elif(m>l[2]-n and l[2]-n>=0):
        f = "L3"
    return f

l = list(map(int, input().split()))
n = int(input())
print(lab_alloction(l,n))







