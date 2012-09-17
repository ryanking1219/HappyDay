def dfs(u,p):
    res,mx1,mx2=0,0,0
    for v in edge[u]:
        if v==p:
            continue
        tmp=dfs(v,u)
        res=max(res,tmp[0])
        if tmp[1]+1>mx1:
            mx1,mx2=tmp[1]+1,mx1
        elif tmp[1]+1>mx2:
            mx2=tmp[1]+1
    res=max(res,mx1+mx2)
    return res,mx1

N=10
edge=[[] for i in xrange(N)]

def splitTwoTrees():
    MaxProduct = -1;
    for i in xrange(1,n+1):
        for j in edge[i]:
            if (j>=i):
                edge[i].remove(j)
                edge[j].remove(i)
                result1 = dfs(i,i)
                #print "i=%s, j=%s, result1=%s"%(i,j,result1)
                #ans1 = (result1[0], result1[1])
                ans1 = result1[0]
                result2 = dfs(j,j)
                #print "i=%s, j=%s, result2=%s"%(i,j,result2)
                #ans2 = max(result2[0], result2[1])
                ans2 = result2[0]
                #print edge
                MaxProduct = max(MaxProduct, ans1 * ans2)
                edge[i].append(j)
                edge[j].append(i)
                edge[i].sort()
                edge[j].sort()
    return MaxProduct

t=input()
for case in xrange(t):
    n=input()
    for i in xrange(1,n+1):
        edge[i]=[]
    for i in xrange(n-1):
        a,b=map(int,raw_input().split())
        edge[a].append(b)
        edge[b].append(a)
    for i in xrange(1, n+1):
        edge[i].sort()
    if n<=3:
        print 0
        continue
    #ans=dfs(1,1)
    print splitTwoTrees()
