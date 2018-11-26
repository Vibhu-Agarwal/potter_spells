from .scrape import get_spells

def spells_by_type(type_of_spell):
    spells = get_spells()[0]
    spells_dict = {}
    if spells is None:
    	return spells_dict
    for key in spells:
        spell = spells[key]
        if spell.type == None:
            continue
        if type_of_spell.lower() in spell.type.lower():
            spells_dict[key] = spell
    return spells_dict
