list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

outlist=[]
for num in list1:
    if num>0:
        outlist.append(str(num))
newtuple= tuple(outlist)
print(",".join(newtuple))
        
list=[]
for number in list2:
    if number>0:
        list.append(number)
print(list)
