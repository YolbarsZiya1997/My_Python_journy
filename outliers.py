# data = [4,5,104,105,110,120,130,130,150,
#         160,170,183,185,187,188,191,350,360] 
         # outlying values at both the low and high ends
# data = [4,5,104,105,110,120,130,130,150,
#         160,170,183,185,187,188,191]
         # outlying values at the low end only
# data = [104,105,110,120,130,130,150,
#          160,170,183,185,187,188,191,350,360]
        # outlying values at the high end only
# data = [104,105,110,120,130,130,150,
#         160,170,183,185,187,188,191]
        # no outlying values
# data = [4546,5456,1504,6105,6110,1920,1230,1360,1550,
#         1690,1750,1283,1485,1287,1688,1391,2350,3260] 
        # Only outlying values       
data = []
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
                start = index + 1 # as you see if we don't add this 1, the del() below will also include index 13
                break
print(start) # for debugging purpose
del data[start:]
print(data)