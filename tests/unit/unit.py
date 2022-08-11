import pytest
from game.utility_classes import SelectWord, LanguageIdentifier


def test_select_random_word_with_one_word():
    list_of_words = ['bunny']
    word_to_guess = SelectWord.select_random_word(list_of_words)
    assert word_to_guess == 'bunny'
    
def test_select_random_word_with_multiple_words():
    list_of_words = ['bunny', 'duck', 'rat', 'cat']
    word_to_guess = SelectWord.select_random_word(list_of_words)
    assert word_to_guess in list_of_words
    
def test_start_new_hangman_game_in_initial_state(new_hangman):
    assert new_hangman._tries == 7
    assert new_hangman._word == 'python'
    assert new_hangman._guessed_letters == []
    assert isinstance(new_hangman._lang_dict, dict)
    
def test_tries_will_be_more_than_zero(new_hangman):
    assert new_hangman._tries != 0
    
def test_setup_language_function_return_a_dict():
    lang_dict = LanguageIdentifier.setup_language("1")
    assert isinstance(lang_dict, dict)
    
def test_setup_language_function_return_a_dict_even_without_an_arg():
    lang_dict = LanguageIdentifier.setup_language()
    assert isinstance(lang_dict, dict)

def test_setup_language_function_return_a_english_dict():
    lang_dict = LanguageIdentifier.setup_language("1")
    assert lang_dict['messages']['GUESS_QUESTION'] == 'Guess a letter: '

def test_setup_language_function_return_a_spanish_dict():
    lang_dict = LanguageIdentifier.setup_language("2")
    assert lang_dict['messages']['GUESS_QUESTION'] == 'Introduce una letra: '
    