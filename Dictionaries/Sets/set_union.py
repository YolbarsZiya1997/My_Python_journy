# farm_animals = {
#     "sheep",
#     "hen",
#     "cow",
#     "horse",
#     "goat"
# }

# wild_animals = {
#     "lion",
#     "elephant",
#     "tiger",
#     "goat", 
#     "panther",
#     "horse"
# }

# all_animals_1 = farm_animals.union(wild_animals)
# print(all_animals_1)

# all_animals_2 = wild_animals.union(farm_animals)
# print(all_animals_2)

# all_animals_3 = farm_animals | wild_animals

# if all_animals_1 == all_animals_2 == all_animals_3:
#     print("True")
    
from prescription_data import adverse_interactions

meds_to_watch = set()

for interactions in adverse_interactions:
    # meds_to_watch = meds_to_watch | interactions
    # meds_to_watch.update(interactions)
    meds_to_watch |= interactions
    
# print(sorted(meds_to_watch))

scorpions = {"emperor", "red claw", "arizona", "forest", "far tail"}
snakes = {"python", "cobra", "viper", "anaconda", "mamba"}
spiders = {"tarantula", "black widow", "wolf spider", "crab spider"}
vespas = {"yellowjacket", "hornet", "paper wasp"}

stinging_buggers = snakes | vespas
arachnids = spiders | scorpions

print(stinging_buggers),
print(arachnids)