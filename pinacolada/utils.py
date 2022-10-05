from functools import reduce
from typing import List

def deep_get(dictionary: dict(), *keys: List[str]):
    """
        Performs deep get on a dictionary. If any key is not found, returns None.
    """

    return reduce(lambda hash, key: hash.get(key) if hash else None, keys, dictionary)
