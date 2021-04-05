data = [4,5,104,105,110,120,130,130,150,
        160,170,183,185,187,188,191,350,360]

# del data[0:2]
# print(data)
# del data [14:]
# print(data)

min_valid = 100
max_valid = 200

#  process the low values in the list
stop = 0
for index, value in enumerate(data):
        if value >= min_valid:
                stop = index
                break
        """what is impotant here is that; we do not 
        delete the indexs inside the iteration, instead we do
        it out side the for-loop"""
print(stop) # for debugging 
del data[:stop] # slice it upto the value that we are gonna delete
print(data)

# process the high value in the list
start = 0
for index in range(len(data)-1,-1,-1):
        if data[index] <= max_valid:
                # We have the index of the last item to keep
                # Set "start" to the position of the first 
                # item to delete, which is 1 after "index".
                start = index + 1
                break
print(start) # for debugging purpose
del data[start:]
print(data)