import gtts
from playsound import playsound
import os

LANGUAGE = 'de'

def german_file_name(german: str):
    """cant save special chars to os"""
    output = german.lower().replace('ü', 'ue').replace('ä', 'ae').replace('ö', 'öe').replace('ß', 'ss')
    return output


def play_sound(file, german, article=None):
    base_directory = file.replace('Wörter', 'Sound')
    base_directory = base_directory.replace('.csv', '')
    sound_file = base_directory + f'/{german_file_name(german)}.mp3'
    if not os.path.exists(sound_file):
        if not os.path.exists(base_directory):
            os.makedirs(base_directory)
        if article:
            input_text = f'{article} {german}'
        else:
            input_text = german

        sound_obj = gtts.gTTS(text=input_text, lang=LANGUAGE)
        sound_obj.save(sound_file)

    sound_file = os.path.abspath(sound_file)
    playsound(sound_file)


if __name__ == '__main__':
    file_name = './../Datenbank/Wörter/Nouns/Home.csv'
    text = 'Küche'
    art = 'Die'

    play_sound(file_name, text, art)
