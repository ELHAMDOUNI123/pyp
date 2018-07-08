def code(a,b,c,d):
    x=0
    while x<6 :
        if d=="0":
           d=c
           c=b
           b=a
           a="0"
        if b=="0":
            b=a
            a="0"
        elif c=="0":
            c=b
            b=a
            a="0"
        elif d=="0":
            d=c
            c=b
            b=a
            a="0"
        x+=1
    return a,b,c,d
def codee(a,b,c,d) :
    m=0
    while m<2: 
        if a==b:
            a="0"
            b=(int(a)+int(b))
            if d==c:
                d=(int(c)+int(d))
                
                c=b*2
                b="0"
                break
        if c==b:
            a="0"
            b="0"
            c= (int(c)+int(b))
            c=c*2
            break
        if d==c:
            a="0"
            b="0"
            d=(int(c)+int(d))
            d=d*2
            break
        m+=1
    return a,b,c,d
def codeee(a,b,c,d):
   a=(code(a[0],a[2],a[4],a[6]))
   b=(code(b[0],b[2],b[4],b[6]))
   c=(code(c[0],c[2],c[4],c[6]))
   d=(code(d[0],d[2],d[4],d[6]))
   print (codee(a[0],a[1],a[2],a[3]))
   print (codee(b[0],b[1],b[2],b[3]))
   print (codee(c[0],c[1],c[2],c[3]))
   print (codee(d[0],d[1],d[2],d[3]))
a=input()
b=input()
c=input()
d=input()
e=int(input())
if e==3:
    print(codeee(a,b,c,d))
if e==1 :
    a=a[::-1]
    b=b[::-1]
    c=c[::-1]
    d=d[::-1]
    x=codeee(a,b,c,d)
    x=x[::-1]
    print (x)
    
    
           
