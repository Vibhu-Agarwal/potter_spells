from .scrape import get_spells

def all_spell_names():
    spells = get_spells()[0]
    return list(spells.keys())