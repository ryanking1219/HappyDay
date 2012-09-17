N=100005
edge=[[] for i in xrange(N)]
def dfs(u,p):
    ans1,ans2=1,0
    for v in edge[u]:
        if v==p:
            continue
        tmp=dfs(v,u)
        ans1+=min(tmp[0],tmp[1])
        ans2+=tmp[0]
    return ans1,ans2

t=input()
for case in xrange(t):
    n=input()
    for i in xrange(1,n+1):
        edge[i]=[]
    for i in xrange(n-1):
        a,b=map(int,raw_input().split())
        edge[a].append(b)
        edge[b].append(a)
    if n==1:
        print n
        continue
    ans=dfs(1,1)
    print min(ans[0],ans[1])
