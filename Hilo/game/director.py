from game.hilo import Hilo


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card1: Is the value of the first card.
        card2: Is the value of the second card.
        roll_hilo: Constan of hight or lower.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The total score of the game.
        
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card_1 = 0
        self.card_2 = 0
        self.roll_hilo = ""
        self.is_playing = True
        self.score = 300

  
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Show the first card and ask if the next card is hight or lower.

        Args:
            self (Director): An instance of Director.
        """
        hilo = Hilo()
        hilo.roll()
        self.card_1 = hilo.value1
        self.card_2 = hilo.value2
        print(f"The card is {self.card_1}")

        self.roll_hilo = input("Hight ot lower? [h/l] ").lower()
        self.is_playing = (self.roll_hilo == "h" or "l")
       
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        if (self.card_1 > self.card_2) and (self.roll_hilo == "l"):
            self.score += 100
        elif self.card_1 < self.card_2 and (self.roll_hilo == "h"):
            self.score += 100
        else:
            self.score -= 75


    def do_outputs(self):
        """Displays second card. Also asks the player if they want to play again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        print(f"The next card was: {self.card_2}")
        print(f"Your score is: {self.score}\n")
        self.is_playing == (self.score > 0)
        close = input("play again? [y/n]: ").lower()
        if close == "n":
            self.is_playing = False
            print("Game is Over!!")
