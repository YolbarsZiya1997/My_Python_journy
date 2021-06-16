vehicles = {
    "dream" : "Hnda 250T",
    "roadster" : "BMW R1100",
    "er5" : "Kawasaki ER5",
    "can_am" : "Bombardier Can_Am 250",
    "virgo" : "Yamaha XV250",
    "tenere" : "Yamaha XT650",
    "jimny" : "Suzuki Jimny 1.5",
    "fiesta" : "Ford Fiesta Ghiza 1.4",
    "roadster" : "Triumph Stree Triple"
}

# my_car = vehicles["fiesta"]
# print(my_car)

# commuter = vehicles["virgo"]
# print(commuter)

# learner = vehicles.get("er5")
# print(learner)

vehicles["starfighter"] = "Lockheed F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "glider"

# Upgrade the Virgo
vehicles["virgo"] = "Yamaha XV535"

del vehicles["starfighter"]
# del vehicles["f1"]
result = vehicles.pop("f1","You wish! Sell the Lear jet and you might afford a racing car.")
print(result)
plane = vehicles.pop("learjet")
print(plane)

bike = vehicles.pop("tenere", "not present")
print(bike)
print()

# for key in vehicles:
#     print(key,vehicles[key], sep=", ")

for key, value in vehicles.items():
    print(key,value, sep=", ")
    

    



