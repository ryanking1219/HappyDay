N=100050
edge=[[] for _ in xrange(N)]
dep=[0 for _ in xrange(N)]
fa=[[0]*20 for _ in xrange(N)]
def dfs(u,p,d):
    dep[u]=d
    for v in edge[u]:
        if v==p:
            continue
        fa[v][0]=u
        for i in xrange(19):
            fa[v][i+1]=fa[fa[v][i]][i]
        dfs(v,u,d+1)

def lca(x,y):
    if dep[x]<dep[y]:
        x,y=y,x
    d=dep[x]-dep[y]
    i=0
    while d>0:
        if d&1==1:
            x=fa[x][i]
        i+=1
        d>>=1
    i=0
    while x!=y:
        if fa[x][i]!=fa[y][i] or (fa[x][i]==fa[y][i] and i==0):
            x=fa[x][i]
            y=fa[y][i]
            i+=1
        else:
            i-=1
    return x
t=input()
for case in xrange(t):
    n=input()
    for i in xrange(1,n+1):
        edge[i]=[]
    for i in xrange(n-1):
        a,b=map(int,raw_input().split())
        edge[a].append(b)
        edge[b].append(a)
    dfs(1,1,0)
    m=input()
    for i in xrange(m):
        a,b=map(int,raw_input().split())
        print dep[a]+dep[b]-2*dep[lca(a,b)]