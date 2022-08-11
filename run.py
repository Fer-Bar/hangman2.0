import sys

from game.hangman import Hangman
from game.utility_classes import LanguageIdentifier, SelectWord, Validators

if __name__ == "__main__":
    arg_value = Validators.validate_argv(sys.argv)
    lang_dict = LanguageIdentifier.setup_language(arg_value)
    word = SelectWord.select_random_word(lang_dict['words'])
    hangman = Hangman(word=word, lang_dict=lang_dict)
    results = hangman.run_game()
    print(results)
