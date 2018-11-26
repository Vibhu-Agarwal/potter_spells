from .scrape import get_spells

def enchants_by_type(type_of_enchantment):
    enchants = get_spells()[1]
    enchants_dict = {}
    if enchants is None:
    	return enchants_dict
    for key in enchants:
        enchant = enchants[key]
        if enchant.type == None:
            continue
        if type_of_enchantment.lower() in enchant.type.lower():
            enchants_dict[key] = enchant
    return enchants_dict
