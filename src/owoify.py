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


def owoify(text):
    text = re.sub(r'@!', r'@¡', text)  # Escape Discord tags
    text = re.sub(r'o',
                  lambda _: r'owo' if random.random() < OWO_CHANCE else 'o', text)
    text = re.sub(r'u',
                  lambda _: r'uwu' if random.random() < OWO_CHANCE else 'u', text)
    text = re.sub(r'([eo][r](s?))\b',
                  lambda match: random.choice(['ah' + match[2], 'uh' + match[2], match[1]]), text)
    text = re.sub(r'\blmao\b', r'lmeow', text)
    text = re.sub(r'l|r', r'w', text)
    text = re.sub(r'L|R', r'W', text)
    text = re.sub(r'ttl', r'ddl', text)
    text = re.sub(r'\bthe\b', r'da', text)
    text = re.sub(r'\bThe\b', r'Da', text)
    text = re.sub(r'\bTHE\b', r'DA', text)
    text = re.sub(r'\bwith\b', r'wif', text)
    text = re.sub(r'ome', r'um', text)
    text = re.sub(r'\bone(s?)\b', r'wun\1', text)
    text = re.sub(r'tion', r'shun', text)
    text = re.sub(r'([Nn])([aou])', r'\1y\2', text)
    text = re.sub(r'N([AOU])', r'NY\1', text)
    text = re.sub(r'ove', r'uv', text)
    text = re.sub(r'!+|(?<!\w):\)(?!\w)', kaomoji('happy'), text)
    text = re.sub(r"\bD:(?!\w)|:'?\(", kaomoji('sad'), text)
    text = re.sub(r'@¡', r"@!", text)  # Unescape Discord tags

    return text
