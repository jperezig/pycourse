#!/usr/bin/python
#-*- coding: utf-8 -*-
u'''
Exercises MOD 04: Strings
'''
from checkbox.lib.text import split
import unittest
import string


def sum_chars_text(text):
    '''given a text str, add all chars by its code
        tip:
            >>> c = 'c'
            >>> ord(c)
            99
    '''
    result = 0
    for letter in text:
        result += ord(letter)
    return result


def reverse_text_by_word(text):
    '''given a text, reverse it by words

        >>> reverse_text_by_word('Sparse is better than dense.')
        'dense. than better is Sparse'
    '''
    split_text = string.split(text, " ")
    split_text.reverse()
    return " ".join(split_text)


def remove_identation_multiline_string(text):
    '''given a multiline text, removes identation

        >>> remove_identation_multiline_string("""Complex is better than complicated.
                                                  Flat is better than nested.""")
        "Complex is better than complicated. Flat is better than nested."
    '''

    return " ".join(text.split())


def join_str_unicode(*items):
    '''given some items joins them with a space as a separator. return a str type (utf-8)

        >>> print join_str_unicode(u'el señor', 'de los anillos')
        'el señor de los anillos'
    '''
    result = " ".join(items)
    return result.decode("utf-8")


class ModStringTestCase(unittest.TestCase):

    def test_sum_chars_text(self):
        '''implement sum_chars_text'''
        text = 'In the face of ambiguity, refuse the temptation to guess.'
        assert sum_chars_text(text) == 5307

    def test_reverse_text_by_word(self):
        '''implement reverse_text_by_word'''
        text = "rules. the break to enough special aren't cases Special"
        assert reverse_text_by_word(text) == "Special cases aren't special enough to break the rules."

    def test_remove_identation_multiline_string(self):
        '''implement remove_identation_multiline_string'''
        text = """ Complex is better than complicated.
                    Flat is better than nested."""
        assert remove_identation_multiline_string(text) == 'Complex is better than complicated. '\
                                                           'Flat is better than nested.'

    def test_join_str_and_unicode(self):
        items = ('el señor', u'de los anillos')
        assert join_str_unicode(items) == 'el se\xc3\xb1or de los anillos'


if __name__ == '__main__':
    unittest.main()
