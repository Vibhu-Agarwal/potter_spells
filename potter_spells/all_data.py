from .scrape import get_spells

def all_data():
    spells, enchants = get_spells()
    if None in (spells,enchants):
    	data = {}
    else:
    	data = {'spells':spells,'enchantments':enchants}
    return data
