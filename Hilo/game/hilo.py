import random


class Hilo:
    """A class who chosee two cards.

    The responsibility of Hilo is to chosee two cards and show a value for each card.
   
    Attributes:
        value1 (int): The number the firts card.
        value2 (int): The number the second card.
    """

    def __init__(self):
        """Constructs a new instance of Hilo.

        Args:
            self (Hilo): An instance of Hilo.
        """
        self.value1 = 0
        self.value2 = 0

    def roll(self):
        """Generates a new aleatory random value to the card.
        
        Args:
            self (Hilo): An instance of Hilo.
        """
        self.value1 = random.randint(1, 13)
        self.value2 = random.randint(1, 13)
