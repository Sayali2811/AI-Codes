data=[11,5,2,88,9,10]
n=len(data)
for i in range(0,n):
    min=data[i]
    index=i
    for j in range(i+1,n):
        if(min>data[j]):
            min=data[j]
            index=j
    data[i],data[index]=data[index],data[i]
print(data)