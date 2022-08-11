# pylint: disable=C0303
import sys
import random

from game.exceptions import TooManyArgsException, InvalidLetterException, InvalidWordException,InvalidLangDictException


class Validators:
    """Class Validators"""
    @staticmethod
    def validate_tries(tries):
        default_tries = 7
        try:
            if tries <= 0 or tries > default_tries:
                raise ValueError("Tries must be a positive number, between 1 and 7")
            return tries
        except ValueError:
            return default_tries
        
    @staticmethod
    def validate_word(word):
        if word == '':
            raise InvalidWordException("The game can't start with a empty word")
        return word.strip().lower()
    
    @staticmethod
    def validate_lang_dict(dictionary):
        if dictionary == {}:
            raise InvalidLangDictException("The game can't start without the messages to display")
        return dictionary
        
    @staticmethod
    def validate_argv(argv:list[str]):
        valid_options = ['1','2']
        default_argv_value = '1'
        try:
            if len(argv) > 2:
                raise TooManyArgsException
            return argv[1] if argv[1] in valid_options else default_argv_value
        except (IndexError, TooManyArgsException):
            return default_argv_value
        
    @staticmethod    
    def validate_letter(letter_to_inspect: str) -> str:
        """
        This function checks that the letter isn't a number or contains more than one character

        Parameters
        ----------
        letter_to_inspect : str
            The letter to be inspected.

        Returns
        -------
        letter_to_inspect : str
            The letter to be inspected.

        Raises
        ------
        Exception
            If the value entered is invalid."""
        if len(letter_to_inspect) != 1 or letter_to_inspect.isdigit():
            raise InvalidLetterException
        return letter_to_inspect

class LanguageIdentifier:
    
    @staticmethod
    def setup_language(option: str = "1") -> dict:
        msg_by_lang: dict = {
            "1": {
                'messages': {
                    'GUESS_QUESTION': 'Guess a letter: ',
                    'WIN_MSG': 'You won the game. Congratulations!',
                    'LOSE_MSG': 'You lose the game. Good luck in the next one.',
                    'SAME_LETTER_MSG': 'You have already used this letter, try with another'
                    },
                
                'words': [
                    'python', 'anaconda', 'banana', 'umbrella', 'couchbase', 'fantastic',
                    'cheese', 'keyboard', 'backseat', 'pyramids'
                    ]
                },
            "2": {
                'messages': {
                    'GUESS_QUESTION': 'Introduce una letra: ',
                    'WIN_MSG': 'Ganaste el juego. Felicitaciones!',
                    'LOSE_MSG': 'Perdiste el juego. Suerte en la próxima.',
                    'SAME_LETTER_MSG': 'Ya has utilizado esta letra, prueba con otra'
                    },
                'words': ['perro', 'anaconda', 'manzana', 'sombrero', 'silla', 'pera', 
                          'queso', 'teclado', 'asientos', 'escuela']                
                }
        }
        try:
            return msg_by_lang[option]
        except KeyError:
            print(f'Key Error: Your choice: {option} does not exist. Be sure to introduce one of the choices.') 


class SelectWord:
    @staticmethod
    def select_random_word(list_of_words:list):
        return random.choice(list_of_words)
