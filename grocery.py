lit=[]
lit1=[]
while True:
    try:
        e=input().lower()
    except EOFError:
        break
    if e in lit :
        a=lit.index(e)
        lit1[a]+=1
    else:
        lit+=[e]
        lit1+=[1]
lit.sort()
for i in range(len(lit)):
    print(lit1[i],lit[i])





