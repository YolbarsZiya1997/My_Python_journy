from contents import recipes

def my_deepcopy(d: dict) -> dict:
    """Deepcopies the dictionary you input

    Args:
        d (dict): the dictionary that is going to be copied

    Returns:
        dict: copied dictionary
    """
    copied_dict = {}
    for keys, values in d.items():
        new_values = values.copy() # this is the line that makes the difference
        # when you don't use the copy() method the data is not stored separately
        # when copy() is used, memory opens a new storing place for it
        copied_dict[keys] = new_values
    return copied_dict


recipes_copy = my_deepcopy(recipes)
recipes_copy["Butter chicken"]["ginger"] = 300
print(recipes_copy["Butter chicken"]["ginger"])
print(recipes["Butter chicken"]["ginger"])
        