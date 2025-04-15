
tc=0
while True :
    try:
        print('Item: ', end='')
        i=input().lower()
    except EOFError :
        print()
        break

    if i=='baja taco':
        m=4.25
    elif i=='burrito':
        m=7.50
    elif i=='bowl':
        m=8.50
    elif i=='nachos':
        m=11.00
    elif i=='quesadilla':
        m=8.50
    elif i=='super burrito':
        m=8.50
    elif i=='super quesadilla':
        m=9.50
    elif i=='taco':
        m=3.00
    elif i=='tortilla salad':
        m=8.00
    else :
        continue
    tc+=m
print(f"total: ${tc:.2f}")

