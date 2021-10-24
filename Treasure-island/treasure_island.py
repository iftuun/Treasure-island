row1=[" "," "," "]
row2=[" "," "," "]
row3=[" "," "," "]

map=[row1,row2,row3]

print(map)
print("where do you want to put your treasure? ")
print(f"{row1}\n{row2}\n{row3}")

po=input("mention column and row without space: ")

var=int(po[0])
hor=int(po[1])

map1=map[hor-1]
map1[var-1]="X"

#print(va)
#print(ho)


print(f"{row1}\n{row2}\n{row3}")