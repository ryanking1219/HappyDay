def dfs(u):
    #return nodes number
    num1, num2 = 0,0
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

def findLargest():
    #lst[0] ((a,b),c)
    maxResult = -1;
    edge[a].remove(b)
    edge[b].remove(a)
    maxResult = max(maxResult, dfs(a) * dfs(b) * 2)

t=input()
for case in xrange(t):
    n=input()
    dic = {}
    for i in xrange(1,n+1):
        edge[i]=[]
    for i in xrange(n-1):
        a,b,c=map(int,raw_input().split())
        edge[a].append(b)
        edge[b].append(a)
        dic.setdefault((a,b),c)
        #dic.setdefault(c,(a,b))
        #lst = dic.values().sort().reverse();
    lst = sorted(dic.iteritems(), lambda x,y:cmp(x[1], y[1]), reverse=True)
    print splitTwoTrees()