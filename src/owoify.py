import re
import random

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
        return random.choice(KAOMOJI[mood])

    return inner


def matchcase(replacement):
    def inner(match):
        word = match.group(0)

        if word.istitle():
            return replacement.title()

        chance = len([c for c in word if c.isupper()]) / len(word)
        return ''.join(c.upper() if random.random() < chance else c for c in replacement)
    return inner


def owoify(text):
    text = re.sub(r'o',
                  lambda _: r'owo' if random.random() < OWO_CHANCE else 'o', text)
    text = re.sub(r'u',
                  lambda _: r'uwu' if random.random() < OWO_CHANCE else 'u', text)
    text = re.sub(r'([eo][r](s?))\b',
                  lambda match: random.choice(['ah' + match.group(2), 'uh' + match.group(2), match.group(1)]), text)
    text = re.sub(r'\blmao\b', r'lmeow', text)
    text = re.sub(r'l|r', r'w', text, flags=re.IGNORECASE)
    text = re.sub(r'L|R', r'W', text, flags=re.IGNORECASE)    
    text = re.sub(r'\bcum\b', matchcase(r'cummies'), text, flags=re.IGNORECASE)
    text = re.sub(r'\bthe\b', matchcase(r'da'), text, flags=re.IGNORECASE)
    text = re.sub(r'\bwith\b', matchcase(r'wif'), text, flags=re.IGNORECASE)    
    text = re.sub(r'\bone\b', matchcase(r'wun'), text, flags=re.IGNORECASE)
    text = re.sub(r'\bones\b', matchcase(r'wuns'), text, flags=re.IGNORECASE)
    text = re.sub(r'\bgive\b', matchcase(r'gib'), text, flags=re.IGNORECASE)
    text = re.sub(r'ttl', matchcase(r'ddl'), text, flags=re.IGNORECASE)
    text = re.sub(r'tion', matchcase(r'shun'), text, flags=re.IGNORECASE)
    text = re.sub(r'ome', matchcase(r'um'), text, flags=re.IGNORECASE)
    text = re.sub(r'([Nn])([aou])', r'\1y\2', text)
    text = re.sub(r'N([AOU])', r'NY\1', text)
    text = re.sub(r'ove', r'uv', text)
    # Negative lookbehind to avoid matching @! for Discord tags
    text = re.sub(r'(?<!@)!+|(?<!\w):\)(?!\w)', kaomoji('happy'), text)
    text = re.sub(r"\bD:(?!\w)|:'?\(", kaomoji('sad'), text)

    return text
