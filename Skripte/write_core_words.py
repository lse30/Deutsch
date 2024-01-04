import os
from core_scripts import read_file, write_file, compare_datasets
from meta_data import noun_bank, misc_bank

"""
Nature: sea*, ocean*, river, mountain, rain, snow, tree, sun, moon, world, Earth, forest, sky, plant, wind, soil/earth, 
flower, valley, root, lake, star, grass, leaf, air, sand, beach, wave, fire, ice, island, hill, heat, natureC

Math/Measurements: meter, centimeter, kilogram, inch, foot, pound, half, circle, square, temperature, date, weight, 
edge,corner
"""

CSV_HEADER = 'German,English,Gender,Box,Passes,Fails\n'
NOUN_PATH = './../Datenbank/Wörter/Nouns/'
MISC_PATH = './../Datenbank/Wörter/Other/'
LETTERS = 'üäßö'

number_cache_ger = {
    '0': 'Null',
    '1': 'Ein',
    '2': 'Zwei',
    '3': 'Drei',
    '4': 'Vier',
    '5': 'Fünf',
    '6': 'Sechs',
    '7': 'Sieben',
    '8': 'Acht',
    '9': 'Neun',
    '10': 'Zehn',
    '11': 'Elf',
    '12': 'Zwölf',
    '13': 'Dreizehn',
    '14': 'Vierzehn',
    '15': 'Fünfzehn',
    '16': 'Sechzehn',
    '17': 'Siebzehn',
    '18': 'Achtzehn',
    '19': 'Neunzehn',
    '20': 'Zwanzig',
    '30': 'Dreißig',
    '40': 'Vierzig',
    '50': 'Fünfzig',
    '60': 'Sechzig',
    '70': 'Siebzig',
    '80': 'Achtzig',
    '90': 'Neunzig',
    '100': 'Hundert'
}


def write_words_to_file(word_category):
    if word_category == 'Noun':
        path = NOUN_PATH
        word_bank = noun_bank.items()
    elif word_category == 'Misc':
        path = MISC_PATH
        word_bank = misc_bank.items()
    else:
        raise NotImplementedError(f'Not Implemented: {word_category}')

    existing_files = os.listdir(path)

    for category, words_list in word_bank:
        if category + '.csv' in existing_files:
            print("File already exists")
            file_data = read_file(f"{path}{category}.csv")
            existing_words = [x.split(',')[0] for x in file_data[1:]]
        else:
            file_data = [CSV_HEADER]
            existing_words = []

        for word_data in words_list:
            line_data = word_data.split('.')
            if len(line_data) == 3:
                german = line_data[0]
                english = line_data[1]
                gender = line_data[2]
            elif len(line_data) == 2:
                german = line_data[0]
                english = line_data[1]
                gender = ''
            else:
                raise Exception(f"Invalid Line {word_data}")

            if gender not in ['M', 'F', 'N', '']:
                raise Exception(f"Invalid Line {word_data}")

            if german not in existing_words:
                new_line = f"{german},{english},{gender},0,0,0\n"
                file_data.append(new_line)

        write_file(file_data, f"{path}{category}.csv")


def write_numbers():
    file_data = [CSV_HEADER]
    i = 0
    bonus_lines = [
        'Eintausend,1000,F,0,0,0\n',
        'Erst,1st,F,0,0,0\n',
        'Zweite,2nd,F,0,0,0\n',
        'Dritte,3rd,F,0,0,0\n',
        'Vierte,4th,F,0,0,0\n',
        'Fünfte,5th,F,0,0,0\n',
        'Sechste,6th,F,0,0,0\n',
        'Siebte,7th,F,0,0,0\n',
        'Achte,8th,F,0,0,0\n',
        'Neunte,9th,F,0,0,0\n',
        'Zehnte,10th,F,0,0,0\n',
    ]
    while i < 115:
        # german words
        if str(i) in number_cache_ger:
            g_out = number_cache_ger[str(i)]
            if i == 1:
                g_out += 's'
        elif i >= 100:
            new = str(i - 100)
            g_out = f"einhundertund{number_cache_ger[new]}"
        else:
            tens = f"{i // 10}0"
            ones = i % 10
            g_out = f'{number_cache_ger[str(ones)]}und{number_cache_ger[tens]}'
        line = f"{g_out.capitalize()},{i},F,0,0,0\n"
        file_data.append(line)
        i += 1
    file_data += bonus_lines
    write_file(file_data, f"{MISC_PATH}Numbers.csv")


def write_words():
    write_words_to_file('Noun')
    write_words_to_file('Misc')
    # write_numbers()


write_words()

if __name__ == '__main__':
    base_dir = './../Datenbank/Wörter/Nouns/'
    other_files = [
        './../Datenbank/Wörter/Other/Adjectives.csv',
        './../Datenbank/Wörter/Other/Colour.csv',
        './../Datenbank/Wörter/Other/Pronouns.csv',
        './../Datenbank/Wörter/Other/CommonSayings.csv',
        './../Datenbank/Wörter/Other/Conjunctions.csv',
        './../Datenbank/Wörter/Other/Prepositions.csv',
        './../Datenbank/Wörter/Other/Adverbs.csv',
        './../Datenbank/Wörter/Other/MISC.csv',
    ]

    new_files = [base_dir + x for x in os.listdir(base_dir)] + other_files
    # old_files = ['./../Datenbank/master_word_bank.csv']
    old_files = ['./../Datenbank/Wörter/other.csv']
    compare_datasets(old_files, new_files)
