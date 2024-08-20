import random

class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def add_point(self):
        self.points += 1

class Game:
    def __init__(self, player_names):
        self.players = [Player(name) for name in player_names]
        self.current_player_index = 0
        self.turn_dict = {
            'sender': None,
            'receiver': None,
            'roll': (0, 0, 0),
            'cla im_sender': (0, 0, 0),
            'not_included_in_roll': (),  # 0 to 3 integers
            'visible_dice_at_end_of_turn': (),  # 0 to 3 integers
            'number_of_dice_rolled': 0,
            'turn_action_order': ()  # exact 1 'claim', max 1 'roll', 0 to ∞ 'look' but max 1x in a row
        }
        self.Isgameover = False

    def roll_strategy(self, last_rolled_score):

        #only happens in first turn
        if last_rolled_score is not None:

            #we call strategy file to decide what to keep and what to roll again
            #keep, dices_to_throw = strategy.py
            #as an example lets say we keep the highest number
            tuple_value = self.turn_dict['roll']

            #new strategie nu
            keep =  (tuple_value[0],)
            throw = self.dice(2)
            rolled_tuple = keep + throw
            rolled_tuple = tuple(sorted(rolled_tuple, reverse=True))
            return rolled_tuple

        else:

            #if last_rolled_score is none we are in the first throw
            rolled_tuple = self.dice(3)
            return rolled_tuple
        return

    def dice(self, amount_of_dice_to_throw):
        # Roll the specified number of dice and store the results in a list
        throw = tuple(random.randint(1, 6) for _ in range(amount_of_dice_to_throw))
        throw = tuple(sorted(throw, reverse=True))

        self.turn_dict['roll'] = throw
        return throw
    
    def from_tuple_to_int(self,tuple_value):

        resulting_integer = int(''.join(map(str, sorted(tuple_value, reverse=True))))

        return resulting_integer

    
    def isMoveLegal(self, bluff_score, rolled_int):

        if (bluff_score <= rolled_int):
             raise ValueError("The bluffed_score must be greater or equal to the rolled_values")
        return

    def get_current_player(self):
        return self.players[self.current_player_index]
    
    def get_next_player_info(self):
        index = (self.current_player_index + 1) % len(self.players)
        return self.players[index]
    
    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play_turn(self, last_rolled_score):

        player = self.get_current_player()
        print(f"{player.name}'s turn!")

        # Roll the dice
        throw = self.roll_strategy(last_rolled_score)

        print(f"{player.name} rolled {throw}.")

        #update roll
        self.turn_dict['roll'] = throw

        # Player decides to pass or bluff
        # bluff_score = int(input(f"{player}, what score do you announce?: "))
        # we call the strategy file again here
        #said_score = strategy.py.whattosay()
        said_score = 654
        print(f'{player.name} announces score {said_score}')
        return said_score, throw

    def start_game(self):
        #initialization
        last_rolled_score = None

        while not self.Isgameover:

            said_score, actual_score = self.play_turn(last_rolled_score)
            # Next player decides if they believe the score
            # belief = input("Do you believe the announced score? (yes/no): ").strip().lower()
            #belief_yes_no = strategy.py.believe(dict)
            belief = random.choice(['yes','no'])

            if belief =='yes':
                print(f'player {self.get_next_player_info().name} does belief')
            else:
                print(f'player {self.get_next_player_info().name} does not belief')

            if belief == 'no':
                if said_score > self.from_tuple_to_int(actual_score):
                    # Current player loses a point if caught lying
                    self.get_next_player_info().add_point()
                    print(f"{self.get_current_player().name} was caught lying!")
                else:
                    # Next player loses a point if they falsely accuse
                    self.next_player()
                    self.get_next_player_info().add_point()
                    print(f"{self.get_current_player().name} falsely accused and loses a point!")
                
                #score was called so game is over
                self.Isgameover = True
        
            last_rolled_score = actual_score
            self.next_player()
            print()


player_names = ["Alice", "Bob"]
game = Game(player_names)

game.start_game()


for player in game.players:
    print(f'{player.name} has {player.points} points ')



