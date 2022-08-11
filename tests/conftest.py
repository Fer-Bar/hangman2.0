import pytest

from game.hangman import Hangman

@pytest.fixture(scope='module')
def new_hangman():
    lang_dict = {
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
    hangman = Hangman(word='python',
                   lang_dict=lang_dict)   
    return hangman