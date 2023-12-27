import unittest
from Skripte import leitner_system


class TestMain(unittest.TestCase):
    def test_word_data(self):
        line: str = 'Maus,Mouse,F,1,2,3\n'
        file: str = './../Datenbank/Wörter/Nouns/Animal.csv'
        word = leitner_system.WordData(line, file)
        comparisons_list = [
            (word.file_name, './../Datenbank/Wörter/Nouns/Animal.csv'),
            (word.category, 'Animal'),
            (word.german, ['Maus']),
            (word.english, ['Mouse']),
            (word.gender, 'F'),
            (word.article, 'Die'),
            (word.box, 1),
            (word.passes, 2),
            (word.fails, 3),
            (word.fails_this_session, 0),
            (word.next_prompt, ['g', 'e']),
            (word.current_prompt, None),
        ]
        for word_attrib, expected in comparisons_list:
            self.assertEqual(word_attrib, expected)

    def test_multi_word_data(self):
        line: str = 'Stadt,City|Town,F,3,2,1\n'
        file: str = './../Datenbank/Wörter/Nouns/Location.csv'
        word = leitner_system.WordData(line, file)
        comparisons_list = [
            (word.file_name, file),
            (word.category, 'Location'),
            (word.german, ['Stadt']),
            (word.english, ['City', 'Town']),
            (word.gender, 'F'),
            (word.article, 'Die'),
            (word.box, 3),
            (word.passes, 2),
            (word.fails, 1),
            (word.fails_this_session, 0),
            (word.next_prompt, ['g', 'e']),
            (word.current_prompt, None),
        ]
        for word_attrib, expected in comparisons_list:
            self.assertEqual(word_attrib, expected)

    def test_adj_word_data(self):
        line: str = 'Alt,Old,,0,0,0\n'
        file: str = './../Datenbank/Wörter/Other/Adjectives.csv'
        word = leitner_system.WordData(line, file)
        comparisons_list = [
            (word.file_name, file),
            (word.category, 'Adjectives'),
            (word.german, ['Alt']),
            (word.english, ['Old']),
            (word.gender, None),
            (word.article, None),
            (word.box, 0),
            (word.passes, 0),
            (word.fails, 0),
            (word.fails_this_session, 0),
            (word.next_prompt, ['g', 'e']),
            (word.current_prompt, None),
        ]
        for word_attrib, expected in comparisons_list:
            self.assertEqual(word_attrib, expected)

    def test_noun_word_data(self):
        line: str = 'Neuseeland,New Zealand,M,1,2,0\n'
        file: str = './../Datenbank/Wörter/Nouns/Countries.csv'
        word = leitner_system.WordData(line, file)
        comparisons_list = [
            (word.file_name, file),
            (word.category, 'Countries'),
            (word.german, ['Neuseeland']),
            (word.english, ['New Zealand']),
            (word.gender, 'M'),
            (word.article, None),
            (word.box, 1),
            (word.passes, 2),
            (word.fails, 0),
            (word.fails_this_session, 0),
            (word.next_prompt, ['g', 'e']),
            (word.current_prompt, None),
        ]
        for word_attrib, expected in comparisons_list:
            self.assertEqual(word_attrib, expected)
