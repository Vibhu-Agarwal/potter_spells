# Harry Potter Spells (potter_spells)

The package lists all the Harry Potter spells.\
Specifically, the scripts scrape the data from the website harrypotter.wikia.com and and provides all the spells.\
The various python scripts provides various filters to list out the spells and enchantments (magic enchantments which are not specifically spells).

## Installing the package
```
pip install potter_spells
```

## Using the package
```
>>> import potter_spells as potter
>>> potter.all_data()
>>> potter.find('Avada Kedavra')
```

### List out all Spells or Enchantments
```
>>> potter.all_spell_names()
>>> potter.all_enchantment_names()
```

### Filter by Type of Magic
```
>>> potter.all_by_type('Charm')
>>> potter.spells_by_type('Hex')
>>> potter.enchants_by_type('Charm')
```
