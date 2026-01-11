import numpy as np


field = np.array([[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]])
prods_array = []
def check_field():
    """ prods_array contains the products of rows, columns, and diagonals """
    prods_array.append(field[0, :].prod())
    prods_array.append(field[1, :].prod())
    prods_array.append(field[2, :].prod())
    prods_array.append(field[:, 0].prod())
    prods_array.append(field[:, 1].prod())
    prods_array.append(field[:, 2].prod())
    prods_array.append(field.diagonal().prod())
    prods_array.append(np.fliplr(field).diagonal().prod())

    """ 
    Check if 1 or 1000 is present in the prods_array
    If product of any of the 3 combinations is 1, then player 1 is the winner
    If the product is 1000, then player 2 is the winner
    """
    if 1 in prods_array:
        return "Player 1 won"
    elif 1000 in prods_array:
        return "Player 2 won"
    else:
        return "Game goes on"

""" print_field displays the classical view of the field as X and O """

tic_tac_toe = {
    0: "?", 1: "X", 10: "O"
}
def print_field():
    field_string = ""
    for row in field:
        for elem in row:
            field_string += tic_tac_toe[elem]
            field_string += " "
        field_string += "\n"
    print(field_string)

"""
While game is on the turn increases alternating in turns for Player 1 and Player 2
Player decides where to put X or O by inputting the coordinates i and j representing 
                                     row and column of the field matrix respectively
"""

turn = 1
winner_text = "Game goes on"
while winner_text == "Game goes on":
    print_field()
    print("\n")
    if turn % 2 == 1:
        i, j = [int(x) for x in input(" Player 1: Enter coordinates separated by a space: ").split()]
        field[(i, j)] = 1
    else:
        i, j = [int(x) for x in input(" Player 2: Enter coordinates separated by a space: ").split()]
        field[(i, j)] = 10
    winner_text = check_field()
    turn += 1
print_field()
print(winner_text)