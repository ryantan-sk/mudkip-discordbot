def ColourCode(colour):
    code = {
        "teal": 0x1abc9c,
        "dark_teal": 0x11806a,
        "green": 0x2ecc71,
        "dark_green": 0x1f8b4c,
        "blue":0x3498db,
        "dark_blue": 0x206694,
        "purple": 0x9b59b6,
        "dark_purple": 0x71368a,
        "magneta": 0xe91e63,
        "dark_magneta": 0xad1457,
        "gold": 0xf1c40f,
        "dark_gold": 0xc27c0e,
        "orange": 0xe67e22,
        "dark_orange": 0xa84300,
        "red": 0xe74c3c,
        "dark_red": 0x992d22,
        "lighter_grey":0x95a5a6,
        "dark_grey": 0x607d8b,
        "blurple": 0x7289da,
        "greyple": 0x99aab5
    }
    return code[f'{colour}']
