from __future__ import annotations

# MyCheckers -  Alternative solution for checkers game.
# Copyright (C) 2025  UltraProcessor
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


def initial_board():
    board = [
        {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''},
        {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''},
        {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''},
        {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''},
        {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''},
        {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''},
        {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''},
        {1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: ''},

    ]

    # Place red pieces ('W') on rows 1, 2, 3
    row = 0
    while row < 3:
        col = 1
        while col < 9:
            if (row + col) % 2 == 1:  # Check if the square is dark (for white pieces)
                board[row][col] = 'R'  # Place red piece

            col = col + 1
        row = row + 1

    # Place black pieces ('W') on rows 6, 7, 8
    row = 5
    while row < 8:
        col = 1
        while col < 9:
            if (row + col) % 2 == 1:  # Check if the square is dark (for white pieces)
                board[row][col] = 'B'  # Place red piece

            col = col + 1
        row = row + 1


    print("Initializing starter board..")
    for row in board:
        print(row)

    return board
