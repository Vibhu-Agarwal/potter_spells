from .scrape import get_spells

def all_spell_names():
    spells = get_spells()[0]
    if spells is None:
    	data = []
    else:
    	data = list(spells.keys())
    return data