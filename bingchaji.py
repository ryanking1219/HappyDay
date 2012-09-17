N=100050
st=[0 for i in xrange(N)]
num=[0 for i in xrange(N)]

def find_set(i):
    if st[i]==i:
        return i
    st[i]=find_set(st[i])
    return st[i]
def union_set(i,j):
    i=find_set(i)
    j=find_set(j)
    if i==j:
        return
    num[i]+=num[j]
    st[j]=i
T=input()
for t in xrange(T):
    n,m=map(int,raw_input().split())
    num=map(int,raw_input().split())
    for i in xrange(n):
        st[i]=i
    for i in xrange(m):
        a,b=map(int,raw_input().split())
        union_set(a-1,b-1)
        print num[find_set(a-1)]

