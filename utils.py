import json

def create_ranks(array):

    arrayint = [int(''.join(map(str, sorted(i, reverse=True)))) for i in array]
    ranking_dict = {}
    for tuple_value in array:

        counter = 0
        integer = int(''.join(map(str, sorted(tuple_value, reverse=True))))
        for number in arrayint:
            if integer > number:
                counter+=1
        ranking_dict[tuple_value] = counter

    return ranking_dict

def ranks_1_dice():

    possible_throws = []
    for i in range(1, 7):
        possible_throws.append((i,))

    remaining_possibble_throws_with_rankings  = create_ranks(possible_throws)

    return remaining_possibble_throws_with_rankings

def ranks_2_dice(hastoinclude_value=()):

    possible_throws = []
    for i in range(1, 7):
        for j in range(1,7):
                possible_throws.append((i,j))

    if hastoinclude_value is not ():

        remaining_possibble_throws = [tup for tup in possible_throws if all(num in tup for num in hastoinclude_value)]
        remaining_possibble_throws_with_rankings  = create_ranks(remaining_possibble_throws)
    else:
        remaining_possibble_throws_with_rankings  = create_ranks(possible_throws)


    return remaining_possibble_throws_with_rankings
    
def ranks_3_dice(hastoinclude_value=()):

    #we create an array with all possibilities
    possible_throws = []
    for i in range(1, 7):
        for j in range(1,7):
            for k in range(1,7):
                possible_throws.append((i,j,k))

    if hastoinclude_value is not ():

        #our throw has to have some dice, so we can throw out all possibilities without these dice,
        #we also 
        remaining_possibble_throws = [tup for tup in possible_throws if all(num in tup for num in hastoinclude_value)]
        remaining_possibble_throws_with_rankings  = create_ranks(remaining_possibble_throws)
    else:

        #our throw does not need to include any dice, so we just use to total array
        remaining_possibble_throws_with_rankings  = create_ranks(possible_throws)

    return remaining_possibble_throws_with_rankings
    
if __name__ == "__main__":

    x=5