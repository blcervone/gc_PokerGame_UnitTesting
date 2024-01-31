# Create cards tuple
# Create an associated values tuple with corresponding card values
# Define check_straight function with card1, 2, 3 parameters which will be string values from the cards tuple
    # Get each card's index number
    # Get corresponding card value based on index
    # Create a sortable iterable (ie list) with the resulting card values
    # Sort that list
    # Create an if/else statement that checks if the sorted values are neighboring sequential values
        # If yes: return largest card's value
        # If no: return 0
# Define check_3ofa_kind function with card 1, 2, 3 parameters which will be string values from the cards tuple
    # Get each card's index number
    # Get corresponding card value based on index
    # Create a sortable iterable (ie list) with the resulting card values
    # Sort that list
    # Create an if/else statement that checks if all the card values are equal:
        # If yes: return largest card's value
        # If no: return 0
# Define a check_royalflush function with card 1, 2, 3 parameters which will be string values from the cards tuple
    # Call check_straight passing in the parameter cards
    # If check_straight returns a value equal to 14,
        # return 14
    # Else:
        # return 0
# Define a play_cards function that takes 6 parameters: 3 cards for left, 3 cards for right: all will be string values from the card tuple
    # Determine left and right values for: straight, 3 of a kind, and royal flush
    # Write an if/else statement to code win conditions based on the above values
        # If left straight value > right straight value or left 3ofakind value > right 3ofakind value or left royalflush > right royal flush
            # AND right straight value is 0:
                # Left wins; return -1
        #  If right straight value > left straight value or right 3ofakind value > left 3ofakind value or right royalflush > left royal flush
             # AND left straight value is 0:
              # Right wins; return 1
        # else:
            # its a draw: return 0

# ============================================================================================================= #

cards = ('S2','S3','S4','S5','S6','S7','S8','S9','S10','SJ','SQ','SK','SA')
cards_values = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)


def check_straight(card1, card2, card3):

    card1_index = cards.index(card1)
    card2_index = cards.index(card2)
    card3_index = cards.index(card3)

    card1_value = cards_values[card1_index]
    card2_value = cards_values[card2_index]
    card3_value = cards_values[card3_index]

    card_value_list = [card1_value, card2_value, card3_value]
    card_value_list.sort()

    if card_value_list[1] == card_value_list[0] + 1 and card_value_list[2] == card_value_list[0] + 2:
        return card3_value
    else:
        return 0


def check_3ofa_kind(card1, card2, card3):

    card1_index = cards.index(card1)
    card2_index = cards.index(card2)
    card3_index = cards.index(card3)

    card1_value = cards_values[card1_index]
    card2_value = cards_values[card2_index]
    card3_value = cards_values[card3_index]

    card_value_list = [card1_value, card2_value, card3_value]
    card_value_list.sort()

    if card_value_list[0] == card_value_list[1] and card_value_list[1] == card_value_list[2]:
        return card3_value
    else:
        return 0


def check_royal_flush(card1, card2, card3):
    if check_straight(card1, card2, card3) == 14:
        return 14
    else:
        return 0


def play_cards(left1, left2, left3, right1, right2, right3):

    left_straight_value = check_straight(left1, left2, left3)
    right_straight_value = check_straight(right1, right2, right3)

    left_3ofakind_value = check_3ofa_kind(left1, left2, left3)
    right_3ofakind_value = check_3ofa_kind(right1, right2, right3)

    left_royalflush_value = check_royal_flush(left1, left2, left3)
    right_royalflush_value = check_royal_flush(right1, right2, right3)

    if left_royalflush_value > right_royalflush_value or left_straight_value > right_straight_value or left_3ofakind_value > right_3ofakind_value and right_straight_value == 0:
        return -1
    elif right_royalflush_value > left_royalflush_value or right_straight_value > left_straight_value or right_3ofakind_value > left_3ofakind_value and left_straight_value == 0:
        return 1
    else:
        return 0
