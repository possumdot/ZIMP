import json

from models.devcard import DevCard
from models.item import Item


def load_item_details_from_file():
    """
    Loads a file that contains a JSON representation of an item, then rebuilds that item
    :return:
    """
    file = open("Test.file", "r")
    file_contents = json.load(file)
    new_item = Item()
    for key, value in file_contents.items():
        setattr(new_item, key, value)

def load_dev_card_from_file():
    """
    Loads a file that contains a JSON representation of a dev card, then rebuilds that dev card
    dev cards have an object inside them so this proves that it inherits it correctly
    :return:
    """
    file = open("testdev.file", "r")
    file_contents = json.load(file)
    new_dev_card = DevCard()
    for key, value in file_contents.items():
        setattr(new_dev_card, key, value)
