# Lists Of list
data = [
    ["Shoe","Shirt","Jeans"],    #0 index
    [1000,800,1200]             #1 Index
]
print(len(data))
print(data[0])                  # List at 0
print(data[1][2])               # 1st List 2nd Index -> 1200

print("Data[1][0:2] : ",data[1][0:2])
#add more list in data
print("Data[0:1][0:2] : ",data[0:1][0:2])