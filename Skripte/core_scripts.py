import os


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
    base_dir = './../Datenbank/Wörter'
    y = os.listdir(base_dir)
    output = []
    for file in y:
        words_list = open(f"{base_dir}/{file}", 'r', encoding='utf-8').readlines()
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


def compare_datasets(set_a, set_b):
    set_a_data = set([x.split(',')[0] for file in set_a for x in read_file(file)[1:]])
    set_b_data = set([x.split(',')[0] for file in set_b for x in read_file(file)[1:]])
    numbers = set([x.split(',')[0] for x in read_file('./../Datenbank/Wörter/Other/Numbers.csv')[1:]])
    set_a_data -= numbers

    missing_words = set_a_data - set_b_data
    added_words = set_b_data - set_a_data
    print(f"{len(set_a_data)} Total words in the bank")
    print(f"{len(missing_words)} left to add")
    print(missing_words)
    print(f"Added {len(added_words)} new words")
