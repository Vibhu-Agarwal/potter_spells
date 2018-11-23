from .scrape import get_spells

def all_enchantment_names():
    enchants = get_spells()[1]
    return list(enchants.keys())
