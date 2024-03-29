import os
import logging

BASE_DIR = './../Datenbank/Wörter'


def create_logger(name, log_level=logging.INFO):
    logging.basicConfig()
    logging.root.setLevel(log_level)

    return logging.getLogger(name)


def read_file(file_path):
    f = open(file_path, 'r', encoding='utf-8')
    data = f.readlines()
    f.close()
    return data


def write_file(lines, file_path):
    f = open(file_path, 'w', encoding='utf-8')
    for line in lines:
        if '\n' not in line:
            f.write(line + '\n')
        else:
            f.write(line)
    f.close()


def write_words(unique_words, file_path):
    f = open(file_path, 'w', encoding='utf-8')
    for word in unique_words:
        if '\n' not in word:
            f.write(word + '\n')
        else:
            f.write(word)
    f.close()


def open_all_words(use_master=False):
    if use_master:
        master_words = open("./../Datenbank/master_word_bank.csv", 'r', encoding='utf-8').readlines()
        all_words = [x.split(',')[0] for x in master_words[1:]]
        return all_words
    base_dir = './../Datenbank/Wörter'
    y = [x for x in os.listdir(base_dir) if 'Noun' not in x]
    output = []
    for file in y:
        words_list = open(f"{base_dir}/{file}", 'r', encoding='utf-8').readlines()
        if len(words_list) > 1:
            existing_words = [x.split(',')[0].lower() for x in words_list[1:]]
            output += existing_words
    return output


def write_to_master_word_bank():
    y = os.listdir(BASE_DIR)
    output = []
    for file in y:
        words_list = open(f"{BASE_DIR}/{file}", 'r', encoding='utf-8').readlines()
        category = file.replace('.csv', '')
        if len(words_list) > 1:
            words_meta_data = [x.split(',') for x in words_list[1:]]
            for words_line in words_meta_data:
                new_line = ','.join(words_line[:3]) + ',' + category + ',' + ','.join(words_line[3:])
                output.append(new_line)
    master_words = open("./../Datenbank/master_word_bank.csv", 'r', encoding='utf-8').readlines()
    all_words = [x.split(',')[0] for x in master_words[1:]]
    output = [x for x in output if x.split(',')[0] not in all_words]
    master_words += output
    write_words(master_words, "./../Datenbank/master_word_bank.csv")
    return output


def open_phrase_book():
    phrase_book = './../Datenbank/Phrasen/phrase_book.csv'
    pre_phrase_book = './../Datenbank/Phrasen/pre_phrase_book.csv'

    phrases = open(phrase_book, 'r', encoding='utf-8').readlines()
    new_phrases = open(pre_phrase_book, 'r', encoding='utf-8').readlines()
    output = []
    for phrase in new_phrases[1:]:
        data = phrase.replace('\n', '').split(',')
        german = data[0].lstrip()
        english = data[1].lstrip()
        new_line = f"{german},{english},0,0,0\n"
        output.append(new_line)
    current_phrases = [x.split(',')[0] for x in phrases[1:]]
    output = [x for x in output if x.split(',')[0] not in current_phrases]
    phrases += output
    write_words(phrases, './../Datenbank/Phrasen/phrase_book.csv')


def analyse_phrase_book():
    phrase_book = './../Datenbank/Phrasen/phrase_book.csv'
    phrases = open(phrase_book, 'r', encoding='utf-8').readlines()
    current_phrases = [x.split(',')[0] for x in phrases[1:]]
    all_words = [x.lower() for x in open_all_words(True)]
    phrase_words = []
    for phrase in current_phrases:
        words = phrase.split(' ')
        for word in words:
            base_word = word.capitalize().replace('.', '').replace('?', '').replace('!', '')
            if base_word not in phrase_words:
                phrase_words.append(base_word)
    unique_words = [x for x in phrase_words if x.lower() not in all_words]
    print(unique_words)


def compare_datasets():
    duolingo_word_file = './../Datenbank/vocabulary_2.csv'
    duolingo_words = set([x.replace('\n', '').lower() for x in read_file(duolingo_word_file)])

    nouns = [f"{BASE_DIR}/Nouns/{x}" for x in os.listdir(f"{BASE_DIR}/Nouns")]
    script_nouns = set([x.split(',')[0].lower() for y in nouns for x in read_file(y)[1:]])

    verbs = [f"{BASE_DIR}/Verbs/{x}" for x in os.listdir(f"{BASE_DIR}/Verbs")]
    script_verbs = set([word.replace('\n', '') for file in verbs for line in read_file(file)[1:]
                        for word in line.split(',')[1:]])

    others = [f"{BASE_DIR}/Other/{x}" for x in os.listdir(f"{BASE_DIR}/Other") if 'Numbers' not in x]
    script_other = set([x.split(',')[0].lower() for y in others for x in read_file(y)[1:]])

    scripted_total = script_nouns.union(script_verbs, script_other)
    unaccounted_duo_words = duolingo_words - scripted_total
    new_words = scripted_total - duolingo_words
    print(f"There are {len(duolingo_words)} duolingo words")
    print(f"There are {len(scripted_total)} scripted words")
    print(f"There are {len(new_words)} new words")
    print(f"There are {len(unaccounted_duo_words)} unaccounted words")
    for word in unaccounted_duo_words:
        print(word)


if __name__ == '__main__':
    compare_datasets()
