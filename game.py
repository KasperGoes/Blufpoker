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

    def dice(self):
        #sort them
        #self.values = tuple(sorted(random.randint(1, 6) for _ in range(3), reverse=True))
        return random.randint(1, 6)
        # return (random.randint(1, 6), random.randint(1, 6), random.randint(1, 6))

    def get_current_player(self):
        return self.players[self.current_player_index]
    
    def get_next_player_info(self):
        index = (self.current_player_index + 1) % len(self.players)
        return self.players[index]
    
    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play_turn(self):
        player = self.get_current_player()
        print(f"{player.name}'s turn!")

        # Roll the dice
        rolled_value = int(self.dice())
        print(f"{player.name} rolled {rolled_value}.")

        # Player decides to pass or bluff
        # bluff_score = int(input(f"{player}, what score do you announce?: "))
        bluff_score = 6
        print(f'{player.name} announces score 6')
        return bluff_score, rolled_value

    def start_game(self):
        #initialization
        last_rolled_score = None

        while not self.Isgameover:
            bluff_score, actual_score = self.play_turn()

            # Next player decides if they believe the score
            # belief = input("Do you believe the announced score? (yes/no): ").strip().lower()
            belief = random.choice(['yes','no'])
            if belief =='yes':
                print(f'player {self.get_next_player_info().name} does belief')
            else:
                print(f'player {self.get_next_player_info().name} does not belief')

            if belief == 'no':
                if bluff_score > actual_score:
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



