from .spells_by_type import spells_by_type
from .enchants_by_type import enchants_by_type 

def all_by_type(type_of):
    spells_dict = spells_by_type(type_of)
    enchants_dict = enchants_by_type(type_of)
    all_return = {**spells_dict, **enchants_dict}
    return all_return
