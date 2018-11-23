from .scrape import get_spells

def all_data():
    spells, enchants = get_spells()
    return {'spells':spells,
            'enchantments':enchants}
