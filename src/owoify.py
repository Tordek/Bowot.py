import re
from random import random, choice

OWO_CHANCE = 0.03
KAOMOJI = {
    'happy': [
        '(\\*^ω^)',
        '(◕‿◕✿)',
        '(◕ᴥ◕)',
        'ʕ•ᴥ•ʔ',
        'ʕ￫ᴥ￩ʔ',
        '(\\*^.^\\*)',
        '(｡♥‿♥｡)',
        '(\\*￣з￣)',
        '>w<',
        '^w^',
        '(つ✧ω✧)つ',
        '(/ =ω=)/',
    ],
    'sad': [
        '(/ω＼)',
        '~(>_<~)',
        '｡･ﾟﾟ\\*(>д<)\\*ﾟﾟ･｡',
        '(╥_╥)',
        '(╬ Ò﹏Ó)',
        '( \\` ω ´ )',
        '(；⌣̀_⌣́)',
        '(︶︹︺)',
        '(ᗒᗣᗕ)՞',
    ],
}


def kaomoji(mood):
    def inner(_):
        return choice(KAOMOJI[mood])

    return inner


def matchcase(replacement):
    def inner(match):
        word = match.group(0)

        if word.istitle():
            return replacement.title()

        chance = len([c for c in word if c.isupper()]) / len(word)
        return ''.join(c.upper() if random() < chance else c for c in replacement)
    return inner


def chance(p, option1, option2):
    def inner(_):
        if random() < p:
            return option1
        return option2
    return inner


def fchance(p, option1, option2):
    def inner(match):
        if random() < p:
            return option1(match)
        return option2(match)
    return inner


def owoify(text):
    text = re.sub(r'o', chance(OWO_CHANCE, 'owo', 'o'), text)
    text = re.sub(r'u', chance(OWO_CHANCE, 'uwu', 'u'), text)
    text = re.sub(r'([eo][r](s?))\b',
                  lambda match: choice(['ah' + match.group(2), 'uh' + match.group(2), match.group(1)]), text)
    text = re.sub(r'\blmao\b', r'lmeow', text)
    text = re.sub(r'l|r', r'w', text)
    text = re.sub(r'L|R', r'W', text)
    text = re.sub(r'\bcum\b', matchcase(r'cummies'), text, flags=re.IGNORECASE)
    text = re.sub(r'\bthe\b', matchcase(r'da'), text, flags=re.IGNORECASE)
    text = re.sub(r'\bwith\b', matchcase(r'wif'), text, flags=re.IGNORECASE)
    text = re.sub(r'\bone\b', matchcase(r'wun'), text, flags=re.IGNORECASE)
    text = re.sub(r'\bones\b', matchcase(r'wuns'), text, flags=re.IGNORECASE)
    text = re.sub(r'\bgive\b', matchcase(r'gib'), text, flags=re.IGNORECASE)
    text = re.sub(r'\bnot\b', fchance(0.5, matchcase(r'knot'),
                  matchcase(r'not')), text, flags=re.IGNORECASE)
    text = re.sub(r'ttl', matchcase(r'ddl'), text, flags=re.IGNORECASE)
    text = re.sub(r'tion', matchcase(r'shun'), text, flags=re.IGNORECASE)
    text = re.sub(r'ome', matchcase(r'um'), text, flags=re.IGNORECASE)
    text = re.sub(r'ove', matchcase(r'uv'), text, flags=re.IGNORECASE)
    text = re.sub(r'N([AOU])', lambda match: chance(
        0.1, r'NY' + match.group(1), match.group(0))(None), text)
    text = re.sub(r'([Nn])([aou])', lambda match: chance(
        0.1, match.group(1) + r'y' + match.group(2), match.group(0))(None), text)
    # Negative lookbehind to avoid matching @! for Discord tags
    text = re.sub(r'(?<!@)!+|(?<!\w):\)(?!\w)', kaomoji('happy'), text)
    text = re.sub(r"\bD:(?!\w)|:'?\(", kaomoji('sad'), text)

    return text
