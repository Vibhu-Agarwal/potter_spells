# -----------------------------------------------------------------------------
# Author: Vibhu Agarwal
# -----------------------------------------------------------------------------

from dataclasses import dataclass
from dataclasses import asdict
from dataclasses import field
from bs4 import BeautifulSoup
from pprint import pprint
import requests
import sys


@dataclass
class Spell:
    name: str
    type: str = field(init=False, repr=True, default=None)
    pronunciation: str
    description: str


@dataclass
class Enchantment:
    name: str
    type: str = field(init=False, repr=True, default=None)
    description: str


def adjust(text):
    ind = text.find('(')
    return text[:ind - 1] if ind > 0 else text


def fix(text):
    text = text.replace('\n', '')
    text = text.strip()
    return text


def fill_obj(detail, spells, enchantments):
    if 'pron' in detail:
        new_spell = Spell(detail['full_name'],
                          detail['pron'],
                          detail['desc'])
        if 'type' in detail:
            new_spell.type = detail['type']
        spells[detail['name']] = new_spell
    else:
        new_enchantment = Enchantment(detail['full_name'],
                                      detail['desc'])
        if 'type' in detail:
            new_enchantment.type = detail['type']
        enchantments[detail['name']] = new_enchantment


def get_spells():
    url = 'https://harrypotter.wikia.com/wiki/List_of_spells'

    try:
        # print('Creating response ...')
        response_search_page = requests.get(url)
    except:
        print('Failed to create response of search page')
        return None, None

    try:
        # print('Creating response ...')
        soup = BeautifulSoup(response_search_page.text, 'lxml')
    except:
        print('Could not make soup from response')
        return None, None

    try:
        tabbertabs = soup.find_all('div', {'class': 'tabbertab'})
    except:
        print('Failed to load tabbertabs')
        return None, None

    if len(tabbertabs) == 0:
        print('Failed to load tabbertabs')
        return None, None

    spells = {}
    enchantments = {}

    detail = {
        'name': 'Legilimens',
        'full_name': 'Legilimens (Legilimency Spell)',
        'type': 'Type: Charm ',
        'pron': 'Pronunciation: Le-JIL-ih-mens',
        'desc': 'Description: Allows the caster to delve into the mind of the victim, allowing the '
                'caster to see the memories, thoughts, and emotions of the victim.'
    }
    for tabbertab in tabbertabs:
        for tag in tabbertab:
            if tag.name == 'h3':
                spell_name = tag.text
                if detail['name'] not in spells and detail['name'] not in enchantments:
                    if 'desc' in detail:
                        fill_obj(detail, spells, enchantments)
                    else:
                        # print('Not enough information about', detail['name'])
                        pass
                detail = {'name': adjust(spell_name),
                          'full_name': spell_name}
                dl_not_defined = True
            elif tag.name == 'dl' and dl_not_defined:
                dds = tag.find_all('dd')
                for dd in dds:
                    property_text = fix(dd.text)
                    if 'Pronunciation' in property_text and 'Unknown' not in property_text:
                        detail['pron'] = property_text
                    elif 'Type' in property_text:
                        detail['type'] = property_text
                    elif 'Description' in property_text:
                        detail['desc'] = property_text
                if 'pron' in detail or 'type' in detail or 'desc' in detail:
                    dl_not_defined = False

    fill_obj(detail, spells, enchantments)

    return spells, enchantments


if __name__ == '__main__':
    spells, enchantments = get_spells()
    for key in spells:
        print(key)
        print(asdict(spells[key]), '\n')
    for key in enchantments:
        print(key)
        print(asdict(enchantments[key]), '\n')
