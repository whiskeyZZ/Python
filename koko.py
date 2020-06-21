coco=0
while True:
    i=0
    temp=coco
    while i<4:
        if temp%3==1:
            temp-=1
            temp=int(temp*2/3)
            i+=1
        else:
            break
    if i==4:
        print(coco)
        break
    else:
        coco+=1