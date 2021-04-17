a = b = c = d = e = f = 42
print(c)

x,y,z = 1,2,76
print(x,y,z)

print("Unpacking a tuple")

data = 1, 2, 76 # Data represents a tupple
x, y, z = data
print(x,y,z)

print("Unpacking List")

data_list = [12, 13, 14]
# data_list.append(15) # causes the unpack crash

p,q,r = data_list
print(p)
print(q)
print(r)