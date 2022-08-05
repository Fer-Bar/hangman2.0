# pylint: disable=C0303
from images import IMAGES


class Hangman:
    """
    The hangman game.
    """

    def __init__(self, word: str, tries: int = 7) -> None:
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
        _messages : dict[str:str]
            The game messages to be displayed to the player.
        """
        self._word: str = word
        self._tries: int = tries
        self._guessed_letters: list = []
        self._hidden_word: list = ["*"] * len(word)
        self._messages: dict[str:str] = {
            "VICTORY": "You won the game",
            "NO_VICTORY": "You lose the game",
            "TRY_AGAIN_ALERT": "You have already used this letter, try with another",
        }

    def check_letter_format(self, letter_to_inspect: str) -> None:
        """
        This function checks that the letter isn't a number or contains more than one character

        Parameters
        ----------
        letter_to_inspect : str
            The letter to be inspected.

        Returns
        -------
        None

        Raises
        ------
        Exception
            If the value entered is invalid."""
        if len(letter_to_inspect) != 1 or letter_to_inspect.isdigit():
            raise Exception("The value entered is invalid.")

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

    def check_if_letter_was_used(self, guess_letter: str) -> None:
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
        if guess_letter in self._guessed_letters:
            print(self._messages["TRY_AGAIN_ALERT"])

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

    def check_status(self, word_to_check: str) -> bool:
        """
        This function checks the status of the game. \n
        Takes a word as an input and checks if it contains any asterisks.
        If it doesn't contain any asterisks, it means the player has guessed all
        the letters correctly and has won the game.
        If it does contain asterisks, it means the player has not guessed all the
        letters correctly and has to keep playing.

        Parameters
        ----------
        word_to_check: str
            The word to check.

        Returns
        -------
        bool
            Returns True if the player has won the game and
            False if the player has not won the game."""
        return "*" not in word_to_check

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
        while self._tries >= 0:
            self.set_gameboard(word_to_display=self._hidden_word, tries=self._tries)
            letter: str = input("Guess a letter: ").strip().lower()
            self.check_letter_format(letter)
            if self.check_if_letter_was_used(letter):
                continue
            self.check_and_replace(letter)
            if self.check_status(self._hidden_word):
                return f"{self._messages['VICTORY']}. The word was {self._word}"
        return f"{self._messages['NO_VICTORY']}. The word was {self._word}"


if __name__ == "__main__":
    hangman = Hangman(word="hangman")
    results = hangman.run_game()
    print(results)
