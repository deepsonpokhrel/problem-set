lit=[]
lit1=[]
while True:
    try:
        e=input().upper()
    except EOFError:
        break
    if e in lit :
        a=lit.index(e)
        lit1[a]+=1
    else:
        lit+=[e]
        lit1+=[1]
m_lit=list(zip(lit,lit1))
m_lit.sort()
for el,c in m_lit:
    print(f"{c} {el}")
