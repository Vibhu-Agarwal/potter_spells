from .scrape import get_spells

def all_enchantment_names():
    enchants = get_spells()[1]
    if enchants is None:
    	data = []
    else:
    	data = list(enchants.keys())
    return data
