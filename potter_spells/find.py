from .scrape import get_spells

def find(word):
    spells, enchants = get_spells()
    data = {}
    if len(word) < 1 or None in (spells,enchants):
    	return data
    for key in spells:
    	spell = spells[key]
    	if word.lower() in spell.name.lower():
    		data[key] = spell
    for key in enchants:
    	enchant = enchants[key]
    	if word.lower() in enchant.name.lower():
    		data[key] = enchant
    return data