"""
  DESCRIPTION

    Minesweeper is a popular video game. From Wikipedia, "The game features a grid of
    clickable squares, with hidden "mines" scattered throughout the board. The
    objective is to clear the board without detonating any mines, with help from
    clues about the number of neighboring mines in each field." Specifically,
    when a player clicks on a square (also called a cell) that doesn't contain a
    mine, the square reveals a number representing the number of immediately
    adjacent mines (including diagonally adjacent mines).


    You're given a two-dimensional array of strings that represents a
    Minesweeper board for a game in progress. You're also given a row and a
    column representing the indices of the next square that the player clicks on
    the board. Write a function that returns an updated board after the click
    (your function can mutate the input board).


    The board will always contain only strings, and each string will be one of
    the following:
        "M": A mine that has not been clicked on.
        "X": A mine that has been clicked on, indicating a lost game.
        "H": A cell with no mine, but whose content is still hidden to the player.
        "0-8": A cell with no mine, with an integer from 0 to 8
          representing the number of adjacent mines. Note that this is a
          single-digit integer represented as a string. For example
          "2" would mean there are 2 adjacent cells with mines.
          Numbered cells are not clickable as they have already been revealed.


    If the player clicks on a mine, replace the "M" with
    "X", indicating the game was lost.

    If the player clicks on a cell adjacent to a mine, replace the
    "H" with a string representing the number of adjacent mines.

    If the player clicks on a cell with no adjacent mines, replace the
    "H" with "0". Additionally, reveal all of the
    adjacent hidden cells as if the player had clicked on those cells as well.

    You can assume the given row and column will always represent a legal move.
    The board can be of any size and have any number of mines in it.


  Time complexity O(w*h)
  Space complexity O(1)
"""
import pytest
from icecream import ic



def revealMineSweeper(board, row, column, click=True):
    if board[row][column] == 'M':
        if click:
            board[row][column] = 'X'
        return board

    revealed_cell = str(reveal(board,row,column))
    if revealed_cell == '0':
        board[row][column] = '0'
        
        for cell in get_adjacent(board,row,column):
            if board[cell[0]][cell[1]]=='H':
                revealMineSweeper(board, cell[0], cell[1], False)
    else:
        board[row][column] = revealed_cell

    return board


def reveal(board, row, column):
    return sum([1 for cell in get_adjacent(board, row, column) if board[cell[0]][cell[1]] == 'M'])
        

def get_adjacent(board, row, column):
    adjacents = [
        [row-1,column-1],
        [row-1,column],
        [row-1,column+1],
        [row,column-1],
        [row,column+1],
        [row+1, column-1],
        [row+1, column],
        [row+1, column+1]
    ]
    return [[r, c] for r,c in adjacents if 0<=r<len(board) and 0<=c<len(board[0])]



# case [board, row, column, expected]
cases = [
    [[['H']], 0, 0, [['0']]],
    [[['M']], 0, 0, [['X']]],
    [[['H', 'M']], 0, 0, [['1', 'M']]],
    [[['H', 'H']], 0, 0, [['0', '0']]],
    [[['H', 'H'], ['H', 'H']], 0, 0, [['0', '0'], ['0', '0']]],
    [[['H', 'H'], ['H', 'H']], 1, 0, [['0', '0'], ['0', '0']]],
    [[['H', 'H'], ['H', 'H']], 1, 1, [['0', '0'], ['0', '0']]],
    [[['H', 'H'], ['H', 'H']], 0, 1, [['0', '0'], ['0', '0']]],
    [[['H', 'M'], ['H', 'H']], 0, 1, [['H', 'X'], ['H', 'H']]],
    [[['H', 'M'], ['H', 'H']], 1, 1, [['H', 'M'], ['H', '1']]],
    [[['H', 'M'], ['H', 'H']], 1, 0, [['H', 'M'], ['1', 'H']]],
    [[['H', 'M'], ['H', 'H']], 0, 0, [['1', 'M'], ['H', 'H']]],
    [[['M', 'M'], ['M', 'M']], 0, 0, [['X', 'M'], ['M', 'M']]],
    [[['M', 'M'], ['M', 'M']], 1, 0, [['M', 'M'], ['X', 'M']]],
    [[['M', 'M'], ['H', 'H'], ['H', 'H']], 0, 0, [['X', 'M'], ['H', 'H'], ['H', 'H']]],
    [[['M', 'M'], ['H', 'H'], ['H', 'H']], 1, 0, [['M', 'M'], ['2', 'H'], ['H', 'H']]],
    [[['M', 'M'], ['H', 'H'], ['H', 'H']], 2, 0, [['M', 'M'], ['2', '2'], ['0', '0']]],
    [[['M', 'M', 'M'], ['M', 'H', 'M'], ['M', 'M', 'M']], 1, 1, [['M', 'M', 'M'], ['M', '8', 'M'], ['M', 'M', 'M']]],
    [[['M', 'M', 'M', 'M'], ['M', 'H', 'H', 'M'], ['M', 'M', 'M', 'M']], 1, 1, [['M', 'M', 'M', 'M'], ['M', '7', 'H', 'M'], ['M', 'M', 'M', 'M']]],
    [[['H', 'H', 'H', 'H', 'M'], ['H', 'H', 'M', 'H', 'H'], ['H', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'H']], 3, 0, [['0', '1', 'H', 'H', 'M'], ['0', '1', 'M', '2', '1'], ['0', '1', '1', '1', '0'], ['0', '0', '0', '0', '0']]],
    [[['H', 'H', 'H', 'H', 'M'], ['H', 'H', 'M', 'H', 'H'], ['H', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'H']], 3, 4, [['0', '1', 'H', 'H', 'M'], ['0', '1', 'M', '2', '1'], ['0', '1', '1', '1', '0'], ['0', '0', '0', '0', '0']]],
    [[['H', 'H', 'H', 'H', 'M'], ['H', 'H', 'M', 'H', 'H'], ['H', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'H']], 0, 2, [['H', 'H', '1', 'H', 'M'], ['H', 'H', 'M', 'H', 'H'], ['H', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'H']]],
    [[['H', 'H', 'H', 'H', 'M'], ['H', '1', 'M', 'H', '1'], ['H', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'H']], 3, 4, [['0', '1', 'H', 'H', 'M'], ['0', '1', 'M', '2', '1'], ['0', '1', '1', '1', '0'], ['0', '0', '0', '0', '0']]],
    [[['H', 'H', 'M', 'H', 'H', 'M', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'M', 'H', 'H', 'M', 'H'], ['H', 'M', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'M', 'H', 'M', 'H', 'H', 'M'], ['M', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'M', 'H', 'M', 'H', 'H'], ['H', 'H', 'M', 'H', 'H', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'H', 'H', 'M', 'H', 'H'], ['H', 'M', 'H', 'H', 'H', 'H', 'H', 'H', 'H']], 0, 0, [['0', '1', 'M', 'H', 'H', 'M', 'H', 'H', 'H'], ['1', '2', 'H', 'H', 'M', 'H', 'H', 'M', 'H'], ['H', 'M', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'M', 'H', 'M', 'H', 'H', 'M'], ['M', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'M', 'H', 'M', 'H', 'H'], ['H', 'H', 'M', 'H', 'H', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'H', 'H', 'M', 'H', 'H'], ['H', 'M', 'H', 'H', 'H', 'H', 'H', 'H', 'H']]],
    [[['H', 'H', 'M', 'H', 'H', 'M', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'M', 'H', 'H', 'M', 'H'], ['H', 'M', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'M', 'H', 'M', 'H', 'H', 'M'], ['M', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'M', 'H', 'M', 'H', 'H'], ['H', 'H', 'M', 'H', 'H', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'H', 'H', 'M', 'H', 'H'], ['H', 'M', 'H', 'H', 'H', 'H', 'H', 'H', 'H']], 3, 6, [['H', 'H', 'M', 'H', 'H', 'M', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'M', 'H', 'H', 'M', 'H'], ['H', 'M', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'M', 'H', 'M', '1', 'H', 'M'], ['M', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'M', 'H', 'M', 'H', 'H'], ['H', 'H', 'M', 'H', 'H', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'H', 'H', 'M', 'H', 'H'], ['H', 'M', 'H', 'H', 'H', 'H', 'H', 'H', 'H']]],
    [[['H', 'H', 'M', 'H', 'H', 'M', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'M', 'H', 'H', 'M', 'H'], ['H', 'M', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'M', 'H', 'M', 'H', 'H', 'M'], ['M', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'M', 'H', 'M', 'H', 'H'], ['H', 'H', 'M', 'H', 'H', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'H', 'H', 'M', 'H', 'H'], ['H', 'M', 'H', 'H', 'H', 'H', 'H', 'H', 'H']], 7, 4, [['H', 'H', 'M', 'H', 'H', 'M', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'M', 'H', 'H', 'M', 'H'], ['H', 'M', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'M', 'H', 'M', 'H', 'H', 'M'], ['M', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'M', 'H', 'M', 'H', 'H'], ['H', 'H', 'M', '2', '1', '3', 'H', 'H', 'H'], ['H', 'H', '2', '1', '0', '1', 'M', 'H', 'H'], ['H', 'M', '1', '0', '0', '1', 'H', 'H', 'H']]],
    [[['H', 'M', 'H', 'H', 'H', 'H', 'M', 'H'], ['H', 'H', 'H', 'H', 'M', 'H', 'H', 'H'], ['M', 'H', 'H', 'M', 'H', 'M', 'H', 'H'], ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], ['H', 'M', 'H', 'H', 'H', 'H', 'M', 'H'], ['H', 'H', 'H', 'H', 'M', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'M']], 6, 0, [['H', 'M', 'H', 'H', 'H', 'H', 'M', 'H'], ['H', 'H', 'H', 'H', 'M', 'H', 'H', 'H'], ['M', 'H', 'H', 'M', 'H', 'M', 'H', 'H'], ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], ['H', 'M', 'H', 'H', 'H', 'H', 'M', 'H'], ['1', '1', '1', '1', 'M', 'H', 'H', 'H'], ['0', '0', '0', '1', 'H', 'H', 'H', 'M']]],
    [[['H', 'M', '1', 'H', '1', 'H', 'M', '1'], ['H', 'H', 'H', 'H', 'M', 'H', '2', 'H'], ['M', 'H', 'H', 'M', 'H', 'M', 'H', 'H'], ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], ['1', 'M', 'H', 'H', 'H', 'H', 'M', 'H'], ['H', 'H', 'H', 'H', 'M', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'M']], 6, 0, [['H', 'M', '1', 'H', '1', 'H', 'M', '1'], ['H', 'H', 'H', 'H', 'M', 'H', '2', 'H'], ['M', 'H', 'H', 'M', 'H', 'M', 'H', 'H'], ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], ['1', 'M', 'H', 'H', 'H', 'H', 'M', 'H'], ['1', '1', '1', '1', 'M', 'H', 'H', 'H'], ['0', '0', '0', '1', 'H', 'H', 'H', 'M']]],
    [[['H', 'M', '1', 'H', '1', 'H', 'M', '1'], ['H', 'H', 'H', 'H', 'M', 'H', '2', 'H'], ['M', 'H', 'H', 'M', 'H', 'M', 'H', 'H'], ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], ['1', 'M', 'H', 'H', 'H', 'H', 'M' , 'H'], ['1', '1', 'H', 'H', 'M', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'M']], 6, 0, [['H', 'M', '1', 'H', '1', 'H', 'M', '1'], ['H', 'H', 'H', 'H', 'M', 'H', '2', 'H'], ['M', 'H', 'H', 'M', 'H', 'M', 'H', 'H'], ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], ['1', 'M', 'H', 'H', 'H', 'H', 'M', 'H'], ['1', '1', '1', '1', 'M', 'H', 'H', 'H'], ['0', '0', '0', '1', 'H', 'H', 'H', 'M']]],
    [[['H', 'M', 'H', 'H', 'H', 'H', 'M', 'H'], ['H', 'H', 'H', 'H', 'M', 'H', 'H', 'H'], ['M', 'H', 'H', 'M', 'H', 'M', 'H', 'H'], ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], ['H', 'M', 'H', 'H', 'H', 'H', 'M', 'H'], ['H', 'H', 'H', 'H', 'M', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'M']], 6, 7, [['H', 'M', 'H', 'H', 'H', 'H', 'M', 'H'], ['H', 'H', 'H', 'H', 'M', 'H', 'H', 'H'], ['M', 'H', 'H', 'M', 'H', 'M', 'H', 'H'], ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], ['H', 'M', 'H', 'H', 'H', 'H', 'M', 'H'], ['H', 'H', 'H', 'H', 'M', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'X']]],
    [[['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'M', 'H'], ['H', 'H', 'H', 'H', 'M', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'H', 'H', 'M', 'H', 'H', 'H', 'H', 'H'], ['H', 'H', 'M', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'M', 'H'], ['H', 'H', 'H', 'H', 'M', 'H', 'H', 'H', 'H', 'M', 'H', 'H'], ['M', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'M', 'H', 'H', 'H', 'H']], 6, 2, [['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'M', 'H'], ['H', 'H', 'H', 'H', 'M', 'H', 'H', 'H', 'H', 'H', 'H', 'H'], ['H', 'H', 'H', 'H', 'H', 'H', 'M', 'H', 'H', 'H', 'H', 'H'], ['H', 'H', 'M', 'H', 'H', 'H', 'H', 'H', 'H', 'H', 'M', 'H'], ['H', '2', '1', '2', 'M', 'H', 'H', 'H', 'H', 'M', 'H', 'H'], ['M', '1', '0', '1', '1', '1', '1', 'H', 'H', 'H', 'H', 'H'], ['H', '1', '0', '0', '0', '0', '1', 'M', 'H', 'H', 'H', 'H']]],
    [[['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'H', 'H', 'H', 'H', 'M', 'M', 'M'], ['M', 'M', 'M', 'H', 'H', 'H', 'H', 'M', 'M', 'M'], ['M', 'M', 'M', 'H', 'H', 'H', 'H', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M']], 4, 3, [['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', '5', 'H', 'H', 'H', 'M', 'M', 'M'], ['M', 'M', 'M', 'H', 'H', 'H', 'H', 'M', 'M', 'M'], ['M', 'M', 'M', 'H', 'H', 'H', 'H', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M']]],
    [[['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'H', 'H', 'H', 'H', 'M', 'M', 'M'], ['M', 'M', 'M', 'H', 'H', 'H', 'H', 'M', 'M', 'M'], ['M', 'M', 'M', 'H', 'H', 'H', 'H', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M']], 5, 5, [['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', '5', '3', '3', '5', 'M', 'M', 'M'], ['M', 'M', 'M', '3', '0', '0', '3', 'M', 'M', 'M'], ['M', 'M', 'M', '5', '3', '3', '5', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M']]],
    [[['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', '5', '3', '3', '5', 'M', 'M', 'M'], ['M', 'M', 'M', 'H', 'H', 'H', 'H', 'M', 'M', 'M'], ['M', 'M', 'M', 'H', 'H', 'H', 'H', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M']], 5, 5, [['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', '5', '3', '3', '5', 'M', 'M', 'M'], ['M', 'M', 'M', '3', '0', '0', '3', 'M', 'M', 'M'], ['M', 'M', 'M', '5', '3', '3', '5', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M'], ['M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M']]]
]

@pytest.mark.parametrize("board, row, column, expected", cases)
def test_revealMineSweeper(board, row, column, expected):
    assert revealMineSweeper(board, row, column)==expected

