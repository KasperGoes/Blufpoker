import json
from collections import Counter
from itertools import permutations
from utils import ranks_1_dice
from utils import ranks_2_dice
from utils import ranks_3_dice


def find_entry(dict, entry):

    for perm in permutations(entry):
        if perm in dict:
                rank_of_claim = dict[perm]
                return rank_of_claim

def roll_strategy(dict):
    return

    
def calculate_winning_probability(correct_dice_ranks, claim):

    rank_of_claim = find_entry(correct_dice_ranks,claim)

    total_possible_ranks = len(correct_dice_ranks)
    how_often_does_claim_draw = Counter(correct_dice_ranks.values())[rank_of_claim]

    win = rank_of_claim/total_possible_ranks
    draw = how_often_does_claim_draw/total_possible_ranks
    lose = (total_possible_ranks-rank_of_claim-how_often_does_claim_draw)/total_possible_ranks
    outcome_array = {'win':win,'draw':draw,'lose':lose}

    print(f"The rank of the claim {claim} is {rank_of_claim}.")
    print(f"the claim {claim} strictly beats {rank_of_claim} roll(s), draws {how_often_does_claim_draw} roll(s) and strictly loses from {total_possible_ranks-rank_of_claim-how_often_does_claim_draw} roll(s)")
    print(f"The percentage of rolls that you beat is {win:.2f}")

    return outcome_array

def possible_throws_with_ranks(dict):

    visible_dice_at_end_of_turn = dict['visible_dice_at_end_of_turn']
    not_included_in_roll = dict['not_included_in_roll']
    
    #we do not cound the dice that are not includeda as visible dice at end of turn.
    visible_dice_at_end_of_turn = tuple(item for item in visible_dice_at_end_of_turn if item not in not_included_in_roll)

    #we take the following steps. Depending on how many dice are not included in roll we will throw with the remaining amount of dice
    if len(not_included_in_roll) == 2:

        #if we only throw with one dice. there are only six possibilities and it is impossible to show any dice after turn
        remaining_possibble_throws_with_rankings = ranks_1_dice()
    elif len(not_included_in_roll) == 1:
        remaining_possibble_throws_with_rankings = ranks_2_dice(visible_dice_at_end_of_turn)
    elif len(not_included_in_roll) == 0:
        remaining_possibble_throws_with_rankings = ranks_3_dice(visible_dice_at_end_of_turn)

    remaining_possibble_throws_with_rankings = {(key + not_included_in_roll): value for key, value in remaining_possibble_throws_with_rankings.items()}
    
    return remaining_possibble_throws_with_rankings

def ev_of_throwing(dict):

    #ev of throwing is chance that we throw higher than roll
    return 


def belief_not_belief(dict):

    claim_sender = dict['claim_sender']

    #we first calculate all the possible throws with rankings
    remaining_possibble_throws_with_rankings = possible_throws_with_ranks(dict)
    
    #based on these rankings we calculate the winning, drawing and losing percentages.
    percentile_of_claim = calculate_winning_probability(remaining_possibble_throws_with_rankings, claim_sender)

    ev_of_calling_claim = percentile_of_claim['win']


    ev = ev_of_throwing()
    #based on these percentages we decide whether or not we want to catch their possible bluff


    return
    

if __name__ == "__main__":

    turn_dict = {
        'sender': 'Olav',
        'receiver': 'Kasper',
        'roll': (1,1,1),
        'claim_sender': (5,5,5),
        'not_included_in_roll': (),  # 0 to 3 integers #Not included in roll zijn dobbelstenen die je niet meerolt, visible dice at end of turn zijn dobbelstenen die je na het rollen zichtbaar maakt
        'visible_dice_at_end_of_turn': (),  # 0 to 3 integersvDie 
        'number_of_dice_rolled': 3,
        'turn_action_order': ()  # exact 1 'claim', max 1 'roll', 0 to ∞ 'look' but max 1x in a row
    }

    #load in rank_dict

    belief_not_belief(turn_dict)
