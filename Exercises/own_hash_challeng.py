data = [
    ("kawap", "tasty meat skewer grilled with chared coal, have a disticnt cumen flavor"),
    ("polo", "famous centarl asian rice dish, made with rice and carrots"),
    ("Qorulghan laghman", "famous Uyghur noodle dish"),
    ("chuchure", "a soup dish that has meat and dumpling in it"),
    ("Narin", "Another type of meaty noodly dish made with horse meat")
]

def simple_hash(s: str) -> int:
    """ A supper easy hash function

    Args:
        s (str): string or key that is gonna be hashed

    Returns:
        int: the hash value
    """
    hash_value = ord(s[0])
    return hash_value % 10

def get(k: str) -> str:
    """Gives us the value of the hash key, if it exist

    Args:
        k (str): [description]

    Returns:
        str: [description]
    """
    hash_number = simple_hash(k)
    if values[hash_number]:
        return values[hash_number]
    else:
        return None
    
keys = [""] * 10
values = keys.copy()

for key, value in data:
    hashes = simple_hash(key)
    print(key, hashes)
    keys[hashes] = key
    values[hashes] = value
    
print(keys)
print(values)
taam = get("Manta")
print(taam)