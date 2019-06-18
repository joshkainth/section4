names = "John, Jennie, Jim, Jack, Joe"
print(names[0])

idx = names.index("Jennie")
print(idx)

names = names.replace("J", "K")
print(names)

data = names.split(",")
print(data)
print(type(data))

qoutes = "Search the candle rather than cursing the darkness"
data = qoutes.split(" ")
print(data)
print(len(data))