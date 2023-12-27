from core_scripts import read_file, write_file, create_logger
from random import shuffle, choice
from typing import Dict, List, Optional, Tuple
from text_to_speech import play_sound

TEST_MODE = False
article_redundant_nouns = ['Countries', 'DaysOfWeek', 'Months']
MAX_WORDS = 20

logger = create_logger(__name__)

# TODO have better system for non gender important words or double spellings based on gender


class WordData:
    def __init__(self, line: str, file: str):
        self.file_name: str = file
        self.category: str = file.split('/')[-1].replace('.csv', '')

        self.german = None
        self.english = None
        self.gender = None
        self.article = None
        self.box = None
        self.passes = None
        self.fails = None

        self.read_line(line)

        self.fails_this_session: int = 0
        self.next_prompt: List[str] = ['g', 'e']
        self.current_prompt: Optional[str] = None

    def read_line(self, line):
        """
        LINE FORMAT: German,English,Gender,Box,Passes,Fails\n
        German and English:
            PrimaryWord|AlternativeWord(FeminineVersion)
        Gender:
            M/F/N -> Masculine, Feminine, Neuter
            V -> Variable Word
            None -> Not Applicable
        Box
            Current Word Level
        Passes
            Recorded Successes
        Failed
            Recorded Failures
        """
        data = line.replace('\n', '').split(',')
        german = data[0].split('|')
        english = data[1].split('|')

        gender = data[2]
        if gender in ['M', 'F',  'N', 'V']:
            if self.category in article_redundant_nouns:
                article = None
            else:
                if gender == 'M':
                    article = 'Der'
                elif gender == 'F':
                    article = 'Die'
                elif gender == 'N':
                    article = 'Das'
                else:
                    print("idk what to do here!")
                    raise
        else:
            gender = None
            article = None

        self.german = german
        self.english = english
        self.gender = gender
        self.article = article
        self.box = int(data[3])
        self.passes = int(data[4])
        self.fails = int(data[5])

    def get_next_prompt(self) -> str:
        """
        Picks a side of the card and prompts the user for an answer
        :return: users answer, side_of_card
        """
        self.current_prompt = choice(self.next_prompt)
        if self.article:
            if self.current_prompt == 'g':
                return f"{self.article} {self.german[0]}? "
            else:
                return f"The {self.english[0]}? "
        if self.current_prompt == 'g':
            return f"{self.german[0]}? "
        else:
            return f"{self.english[0]}? "

    def as_german(self):
        if self.gender:
            return f"{self.article} {self.german[0]}"
        return self.german[0]

    def word_to_line(self) -> str:
        """
        Converts the object to a CSV line
        :return: csv line str
        """
        return f"{'|'.join(self.german)},{'|'.join(self.english)},{self.gender},{self.box},{self.passes},{self.fails}\n"

    def is_answer_correct(self, answer: str) -> bool:
        """
        Assess if the answer given is correct
        :param answer: User answer
        :return: correct or fail
        """

        answer = answer.lower()

        # if the prompt was in english (expect answer to be german)
        if self.current_prompt == 'e':
            correct_answers = [x.lower() for x in self.german]
            if self.article:
                article = answer.split(' ')[0]
                german = answer.replace(f'{article} ', '')
                if article == self.article.lower() and german in correct_answers:
                    return True
            else:
                if answer in [x.lower() for x in self.german]:
                    return True
        # prompt is german and expecting english
        else:
            answer = answer.replace('the ', '')
            correct_answers = [x.lower() for x in self.english]
            if answer in correct_answers:
                return True
        return False

    def assess_answer(self, answer: str) -> bool:
        result = self.is_answer_correct(answer)
        if result:
            logger.debug('Correct!')
            self.passes += 1
            self.next_prompt.remove(self.current_prompt)
            if not self.next_prompt:
                self.box += 1
                self.next_prompt = ['g', 'e']
        else:
            logger.debug("That's not quite right")
            self.fails += 1
            self.fails_this_session += 1
            self.next_prompt.append(self.current_prompt)

            logger.debug(self)
        return result

    def __str__(self):
        if self.article:
            return f"{self.article} {self.german[0]}: The {self.english[0]}"
        return f"{self.german[0]}: {self.english[0]}"


class LeitnerSystem:
    def __init__(self, *filepaths: str):
        self.filepaths: Tuple[str] = filepaths
        self.boxes: Dict[str, List[WordData]] = self.prepare_words()
        self.current_box: int = min([int(x) for x in self.boxes.keys()])

        self.words_to_test_user: List[WordData] = self.get_test_words()
        self.total_words = len(self.words_to_test_user)
        self.completed_words: List[WordData] = []
        self.current_word: Optional[WordData] = None

    def get_test_words(self):
        print(f"{len(self.boxes[str(self.current_box)])} possible words in word set")
        word_set = self.boxes[str(self.current_box)][:MAX_WORDS]
        if len(word_set) < MAX_WORDS:
            if str(self.current_box + 1) in self.boxes:
                word_set = word_set + self.boxes[str(self.current_box + 1)]
                word_set = word_set[:MAX_WORDS]
        return word_set

    def prepare_words(self) -> Dict[str, List[WordData]]:
        """
        Categorizes all the words in the given files into the appropriate boxes
        """
        file_data: List[WordData] = [WordData(x, file) for file in self.filepaths for x in read_file(file)[1:]]
        boxes: Dict[str, List[WordData]] = {}
        for word in file_data:
            boxes.setdefault(str(word.box), []).append(word)

        for key in boxes.keys():
            shuffle(boxes[key])
        return boxes

    def update_words(self):
        if TEST_MODE:
            print('Test Mode is [True]: not editing files')
            return
        sorted_words = {}
        promoted_words = 0
        for word in self.completed_words:
            if word.fails_this_session != 0:
                word.box -= 1
            else:
                promoted_words += 1
            sorted_words.setdefault(word.file_name, []).append(word)

        for word in self.words_to_test_user:
            sorted_words.setdefault(word.file_name, []).append(word)
        print(f"{promoted_words} words were promoted!")
        for file, updated_words in sorted_words.items():
            updated_words_list = [x.german[0] for x in updated_words]
            file_data = [x for x in read_file(file) if x.split(',')[0].split('|')[0] not in updated_words_list]
            file_data += [x.word_to_line() for x in updated_words]
            write_file(file_data, file)
            print(f'Updated file {file}')
        return promoted_words

    def test(self):
        while self.words_to_test_user:
            shuffle(self.words_to_test_user)
            self.current_word = self.words_to_test_user.pop(0)
            answer = input(self.current_word.get_next_prompt())
            self.submit_answer(answer)
        self.update_words()

    def serve_word(self):
        if len(self.words_to_test_user) > 0:
            shuffle(self.words_to_test_user)
            self.current_word = self.words_to_test_user.pop(0)
            return self.current_word
        return None

    def submit_answer(self, answer: str) -> bool:
        result = self.current_word.assess_answer(answer)
        if self.current_box == self.current_word.box:
            self.words_to_test_user.append(self.current_word)
        else:
            self.completed_words.append(self.current_word)
        return result

    def get_answer(self):
        return self.current_word

    def get_category(self):
        return self.current_word.category

    def is_answer_correct(self, answer):
        return self.current_word.is_answer_correct(answer)

    def get_counter(self):
        return f'{len(self.completed_words)}/{self.total_words}'

    def play_word(self):
        cw = self.current_word
        play_sound(cw.file_name, cw.german[0], cw.article)


if __name__ == '__main__':
    # file_path_1 = './../Datenbank/Wörter/Other/Colour.csv'
    file_path_1 = './../Datenbank/Wörter/Nouns/Months.csv'

    system = LeitnerSystem(file_path_1)

    # first_word = system.words_to_test_user[0]
    # system.serve_word()

    system.test()
