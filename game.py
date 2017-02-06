# -*- coding: utf-8 -*-

# `random` module is used to shuffle field, see§:
# https://docs.python.org/3/library/random.html#random.shuffle
import random


# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Dictionary of possible moves if a form of: 
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -4,
    's': 4,
    'a': -1,
    'd': 1,
}


def shuffle_field():
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    """
    field = list(range(1, 17))
    field[-1] = EMPTY_MARK
    random.shuffle(field)
        
    count = 0
    for i in range(0, 16):
        if field[i] != EMPTY_MARK:
            element = field[i]
            for j in range(i + 1, 16):
                if field[j] != EMPTY_MARK and element > field[j]:
                    count += 1
                   
    if (count + 1) % 2 != 0:
        print('Комбинацию невозможно собрать. Меняю расклад.')
        shuffle_field()
    

    return field    
    


def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    
    """
    for i in range(0, 16, 4):
        print(field[i: i + 4])
    


def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    
    list1 = list(range(1, 17))
    list1[-1] = EMPTY_MARK
    return field == list1


def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """
    if EMPTY_MARK in field:
        empty_index = field.index(EMPTY_MARK)


    if key == 'w' and empty_index < 4:
        raise IndexError('Недопустимый ход!')
    if key == 'a' and empty_index % 4 == 0:
        raise IndexError('Недопустимый ход!')
    if key == 's' and empty_index > 11:
        raise IndexError('Недопустимый ход!')
    if key == 'd' and (empty_index + 1) % 4 == 0:
        raise IndexError('Недопустимый ход!')

    difference = empty_index + MOVES[key]
    field[empty_index], field[difference] = field[difference], field[empty_index]
    
    return field

def handle_user_input():
    """
    Handles user input. List of accepted moves:
        'w' - up, 
        's' - down,
        'a' - left, 
        'd' - right
    :return: <str> current move.
    """
    while True:
        move = input('Введите ваш ход:  ')

        if move not in MOVES.keys():
            print('Недопустимое значение. Попробуйте ещё раз.')
        else:
            return move        


def main():
    """
    The main method. It starts when the program is called.
    It also calls other methods.
    :return: None
    """

    steps = 0
    field = shuffle_field()
    while not is_game_finished(field):
        try:
            print_field(field)
            move = handle_user_input()
            field = perform_move(field, move)
            steps += 1
        except IndexError as mistake:
            print(mistake)
        except KeyboardInterrupt:
            print('The programm is shutting down.')
            print('Количество ваших шагов - {}'.format(steps)) 
            quit()
    else:
        print('Задача решена')              

if __name__ == '__main__':

    # See what this means:
    # http://stackoverflow.com/questions/419163/what-does-if-name-main-do

    main()