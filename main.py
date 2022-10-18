def calc_x(V,M,a,t):
    x=[1]*(V+1)
    for n in range(1,V+1):
        sum=0
        for i in range(0,M):
            if n>=t[i]:
                sum+=a[i]*t[i]*x[n-t[i]]
        x[n]=sum/n
    #print("calc_x: x=",x)
    return x
def calc_p0(x):
    sum = 0
    for item in x:
        sum += item
    return 1 / sum
def calc_pn(x,V,M,a,t):
    #print("calc_pn start...")
    P=[1]*(V+1)
    P[0]=calc_p0(x)
    #print("P(0)=",P[0])
    for n in range(1,V+1):
        sum=0
        for i in range(0,M):
            if n>=t[i]:
                sum+=a[i]*t[i]*P[n-t[i]]
        P[n]=sum/n
    #print("P: ",P)
    #print("calc_pn end...")
    return P
def calc_bn(P,V,t,i=1):
    sum=0
    for i in range(V-t[i-1]+1, V+1):
        sum+=P[i]
    return sum
def calc_all(M,V,a,t):
    x = calc_x(V, M, a, t)
    P = calc_pn(x, V, M, a, t)
    print("x: ",x)
    print("P: ",P)
    #b1=calc_bn(P,V,t,1)
    #b2=calc_bn(P,V,t,2)
    b=[1]*M
    iterator = 0
    while iterator < M:
        iterator += 1
        #print(calc_bn(P,V,t, iterator))
        b[iterator-1] = calc_bn(P,V,t, iterator)
    
    print("b: ",b)

M=2
V=3
t=[1,2]
a=[[0.4,1], [1, 2]]

for item in a:
    print("#### M:", M)
    print("#### V:", V)
    print("#### a:", item)
    print("#### t:", t)
    calc_all(M,V,item,t)
