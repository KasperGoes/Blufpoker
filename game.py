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
        self.is_game_over = False

    def roll_strategy(self, last_rolled_score, claim_sender):

        #only happens in first turn
        if last_rolled_score is not None:

            #we call strategy file to decide what to keep and what to roll again
            #as an example lets say we keep the highest number
            tuple_value = self.turn_dict['roll']

            #new strategie nu
            #keep, dices_to_throw = strategy.py
            keep =  (tuple_value[0],)
            throw = self.dice(2)

            self.turn_dict['number_of_dice_rolled'] = len(keep)
            self.turn_dict['not_included_in_roll'] = keep
            rolled_tuple = keep + throw
            rolled_tuple = tuple(sorted(rolled_tuple, reverse=True))
            return rolled_tuple

        else:

            #if last_rolled_score is none we are in the first throw
            rolled_tuple = self.dice(3)
            self.turn_dict['number_of_dice_rolled'] = 3
            return rolled_tuple
        

    def whattosay_and_show(self, throw):

        #show = strategy.py.show_strategy(throw)
        visible_dice_at_end_of_turn = throw[0]
        return (6,5,4), visible_dice_at_end_of_turn
    

    def dice(self, amount_of_dice_to_throw):
        # Roll the specified number of dice and store the results in a list
        throw = tuple(random.randint(1, 6) for _ in range(amount_of_dice_to_throw))
        throw = tuple(sorted(throw, reverse=True))

        self.turn_dict['roll'] = throw
        return throw
    
    def from_tuple_to_int(self, tuple_value):

        if tuple_value is not None:
            resulting_integer = int(''.join(map(str, sorted(tuple_value, reverse=True))))

            return resulting_integer

    
    def isMoveLegal(self, claim_sender, my_claim):

        if claim_sender is not None:
            if my_claim <= claim_sender:
                raise ValueError("The claim must be greater than previous claim")
            return
        return

    def get_current_player(self):
        return self.players[self.current_player_index]
    
    def get_next_player_info(self):
        index = (self.current_player_index + 1) % len(self.players)
        return self.players[index]
    
    def next_player(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play_turn(self, last_rolled_score, claim_sender):

        player = self.get_current_player()
        print(f"{player.name}'s turn!")

        # Roll the dice
        throw = self.roll_strategy(last_rolled_score, claim_sender)
        print(f"{player.name} rolled {throw}.")

        #update roll

        # Player decides to pass or bluff
        # bluff_score = int(input(f"{player}, what score do you announce?: "))
        # we call the strategy file again here
        #said_score = strategy.py.whattosay_and_show(throw)
        my_claim, visible_dice_at_end_of_turn = self.whattosay_and_show(throw)
        self.isMoveLegal(claim_sender, self.from_tuple_to_int(my_claim))
        said_score = 654
        print(f'{player.name} announces score {said_score} and shows {visible_dice_at_end_of_turn}')

        return said_score, throw, visible_dice_at_end_of_turn

    def start_game(self):
        
        #initialization
        last_rolled_score = None
        claim_sender =  None

        while not self.is_game_over:

            said_score, actual_score, visible_dice_at_end_of_turn = self.play_turn(last_rolled_score, claim_sender)
            self.turn_dict['sender'] =  self.get_current_player().name
            self.turn_dict['receiver'] = self.get_next_player_info().name
            self.turn_dict['roll'] = actual_score
            self.turn_dict['cla im_sender'] = said_score
            self.turn_dict['visible_dice_at_end_of_turn'] = visible_dice_at_end_of_turn
            self.turn_dict['turn_action_order'] = None

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
                self.is_game_over = True
        
            claim_sender = said_score
            last_rolled_score = actual_score
            self.next_player()
            print()


player_names = ["Alice", "Bob"]
game = Game(player_names)

game.start_game()


for player in game.players:
    print(f'{player.name} has {player.points} points ')

print('round is finished')


