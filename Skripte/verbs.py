from core_scripts import write_file, read_file
from random import shuffle
from text_to_speech import play_sound

filename = './../Datenbank/Wörter/Verbs/present.csv'
next_filename = './../Datenbank/Wörter/Verbs/present2.csv'
data = [x.replace('\n', '') for x in read_file(filename)[1:]]
data = data[1:4]
header_order = 'english,german,ich,du,er/sie/es,wir,ihr,Sie'.split(',')


def retrieve_list_item(data_list, previous):
    shuffle(data_list)
    if len(data_list) == 1 or data_list[0] != previous:
        return data_list.pop(0)
    return data_list.pop(1)


def serve_verb(verb):
    word_list = verb.split(',')
    word_pairs = [(header_order[i], word_list[i]) for i in range(len(header_order))]
    # print(word_pairs)
    english = word_pairs.pop(0)
    _ = word_pairs.pop(0)
    current = None
    print(f"To {english[1]}")
    while word_pairs:

        current = retrieve_list_item(word_pairs, current)
        pronoun, answer = current
        alternate_answer = answer.replace('ä', 'ae').replace('ü', 'ue').replace('ö', 'oe').replace('ß', 'ss')
        pronoun = pronoun if pronoun != 'er/sie/es' else 'es'
        user_answer = input(f"{pronoun} ")
        if user_answer == answer or user_answer == alternate_answer:
            print('Correct!')
        else:
            word_pairs.append(current)
            print(f"{pronoun} {answer}")
            play_sound(filename, answer, pronoun)


def verbs_controller(verbs):
    current = None
    i = 0
    while verbs and i < 5:
        current = retrieve_list_item(verbs, current)
        serve_verb(current)
        i += 1


verbs_controller(data)
