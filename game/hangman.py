# pylint: disable=C0303
import os
import time

from game.images import IMAGES 
from game.utility_classes import Validators

class Hangman:
    """
    The hangman game.
    """

    def __init__(self, word: str, lang_dict: dict, tries: int = 7) -> None:
        """
        Constructs all the necessary attributes for the hangman object.

        Parameters
        ----------
        word : str
            The word to be guessed.
        tries : int, optional
            The number of tries the player has, by default 7.

        Attributes
        ----------
        _word : str
            The word to be guessed.
        _tries : int
            The number of tries the player has.
        _guessed_letters : list
            The list of letters the player has guessed.
        _hidden_word : list
            The list of asterisks representing the length of the word to be guessed.
        _formatter : object
            The formatter object 
        _lang_option : str
            This set up the language. 
        _message_dict : dict[str:str]
            The game messages to be displayed to the player.
        """
        self._formatter = Validators()
        self._word: str = self._formatter.validate_word(word)
        self._lang_dict: dict = self._formatter.validate_lang_dict(lang_dict)
        self._tries: int = self._formatter.validate_tries(tries) 
        self._guessed_letters: list = []
        self._hidden_word: list = ["*"] * len(word)

    def set_gameboard(self, word_to_display: str, tries: int) -> None:
        """
        This function sets the gameboard for the game.

        Parameters
        ----------
        word_to_display : str
            The word to display on the gameboard.
        tries : int
            The number of tries the player has left.

        Returns
        -------
        None
        """
        print(IMAGES[tries])
        print(word_to_display)
        print(f'❤️ : {tries}')

    def check_if_letter_was_used(self, guess_letter: str) -> bool:
        """
        This function checks if the player has used the same letter more than once.
        If it was, it prints an alert message.

        Parameters
        ----------
        guess_letter: str
            The letter to be checked.

        Returns:
        -------
        None
        """
        return guess_letter in self._guessed_letters
            

    def check_and_replace(self, letter: str) -> None:
        """
        This function replaces letters in the hidden word with the letter that the player guessed.

        Parameters
        ----------
        letter : str
            The letter that the player guessed.

        Returns
        -------
        None
        """
        if letter in self._word:
            for idx, char in enumerate(self._word):
                if letter == char:
                    self._hidden_word[idx] = letter
                    self._guessed_letters.extend(letter)
        else:
            self._tries -= 1

    def game_is_finished(self, tries_to_check:int, word_to_check: list) -> bool:
        """
        This function checks the status of the game. \n
        Takes a word and tries as an input and checks if it contains any asterisks or 
        tries is equal to 0.
        Return True if the player has guessed all the letters correctly or their number
        of tries is equal to 0.
        Return False if the player has not guessed all the letters correctly and
        have tries to keep playing.

        Parameters
        ----------
        word_to_check: str
            The word to check.
        tries: int
            The tries to check.
        Returns
        -------
        bool
            Returns True if the player has won the game and
            False if the player has not won the game."""
        return tries_to_check == 0 or "*" not in word_to_check
        
    def results(self, word_to_guess) -> str:
        if "*" not in word_to_guess: 
            return f"{self._lang_dict['messages']['WIN_MSG']} The word was {self._word}"
        return f"{self._lang_dict['messages']['LOSE_MSG']} The word was {self._word}"
    
    def guess_letter(self) -> str:
        letter: str = input(self._lang_dict['messages']['GUESS_QUESTION']).strip().lower()
        return self._formatter.validate_letter(letter)
    
    @staticmethod
    def _clean_screen():
        os.system("cls")

    @staticmethod
    def _timer():
        seconds_until_next_guess = 2
        time.sleep(seconds_until_next_guess)
    
    def run_game(self) -> str:
        """
        This function runs the game.

        Parameters
        ----------
        self : Self@Hangman
            The Hangman object.

        Returns
        -------
        str
            A message indicating whether the player won or lost."""
        game_over = False
        while not game_over:
            Hangman._clean_screen()
            self.set_gameboard(word_to_display=self._hidden_word, tries=self._tries)
            letter = self.guess_letter()
            if self.check_if_letter_was_used(letter):
                print(self._lang_dict['messages']["SAME_LETTER_MSG"])
                Hangman._timer()
            else:
                self.check_and_replace(letter)
            game_over = self.game_is_finished(tries_to_check=self._tries, 
                              word_to_check=self._hidden_word)
                
        return self.results(self._hidden_word)


