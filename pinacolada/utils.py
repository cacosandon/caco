import requests
from xmljson import parker
from xml.etree.ElementTree import fromstring
from functools import reduce
from typing import List


def deep_get(dictionary: dict(), *keys: List[str]):
    """
        Performs deep get on a dictionary. If any key is not found, returns None.
    """

    return reduce(lambda hash, key: hash.get(key) if hash else None, keys, dictionary)

def get_location_data(latitude: str, longitude: str) -> dict[str, str]:
    data_url = f"https://nominatim.openstreetmap.org/reverse?lat={latitude}&lon={longitude}"

    location_xml_data = fromstring(requests.get(data_url).text)

    return parker.data(location_xml_data)['addressparts']
