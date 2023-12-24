import random

from core_scripts import open_all_words, write_words


def give_vocab_a_home():
    word_homes = {}
    existing_words = open_all_words()
    vocab_file = "./../Datenbank/vocabulary.csv"
    data = [x.strip('\n') for x in open(vocab_file, 'r', encoding='utf-8').readlines()]
    unique_words = list(set(data) - set(existing_words))
    write_words(unique_words, vocab_file)
    random.shuffle(data)
    print('ENTER [ENGLISH],[GENDER],[CATEGORY]')
    for word in unique_words:
        x = input(f"do you know this word? [{word}] ")
        if x.lower() == 's':
            continue
        elif x.lower() == 'b':
            break
        else:
            if ',' in x:
                english, gender, genre = x.split(',')
            else:
                english = x
                gender = '_'
                genre = 'other'
            english = english.capitalize()
            gender = gender.upper()
            german = word.capitalize()
            new_word_line = f"{german},{english},{gender},0,0,0"
            if genre in word_homes:
                word_homes[genre].append(new_word_line)
            else:
                word_homes[genre] = [new_word_line]

    for key, value in word_homes.items():
        print(key)
        for item in value:
            print(item)


class SimpleWord:
    def __init__(self, line_input):
        data = line_input.split(',')
        self.german = data[0]
        self.english = data[1]
        self.gender = data[2] if data[2] in ['M', 'F', 'N'] else None
        self.prefix = None
        if self.gender:
            if self.gender == 'F':
                self.prefix = 'Die'
            elif self.gender == 'M':
                self.prefix = 'Der'
            else:
                self.prefix = 'Das'
        self.category = data[3]
        self.box = data[4]
        self.passes = data[5]
        self.fails = data[6]

    def __str__(self):
        if self.gender:
            return f"{self.prefix} {self.german}: The {self.english}"
        return f"{self.german}: {self.english}"


def test_words():
    vocab_file = "./../Datenbank/master_word_bank.csv"
    data = [x.strip('\n') for x in open(vocab_file, 'r', encoding='utf-8').readlines()[1:]]
    test_data = [SimpleWord(x) for x in data]
    test_data = [x for x in test_data if x.gender]
    random.shuffle(test_data)
    for item in test_data:
        g_or_e = random.randint(1, 2)
        if g_or_e == 1:
            answer = input(f"What is {item.prefix} {item.german} in English? ")
            answer = answer.replace('the ', '').replace('The ', '')
            if answer.lower() == item.english.lower():
                print("Correct!")
        else:
            answer = input(f"What is the {item.english} in German? ")
            if " " in answer:
                prefix, word = answer.split(' ')

                if prefix.lower() == item.prefix.lower() and word.lower() == item.german.lower():
                    print("Correct!")
            else:
                print("Missing article!")
        print(item)


# test_words()
give_vocab_a_home()
