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

from mycheckers.valid_moves import valid_moves


def move_piece(board, piece, start_row, start_col, end_row, end_col):

    possible_moves = valid_moves(board, piece, start_row, start_col)

    # If move is not in the list of valid moves, return false.
    if (end_row, end_col) not in possible_moves:
        print(f"Invalid move from ({start_row}, {start_col}) to ({end_row}, {end_col}).")
        return False

    # If it's a capture, remove the piece that is jumped over
    if abs(end_row - start_row) == 2 and abs(end_col - start_col) == 2:
        mid_row = (start_row + end_row) // 2
        mid_col = (start_col + end_col) // 2
        board[mid_row - 1][mid_col] = ''  # Remove the captured piece

    # Move the piece
    board[end_row - 1][end_col] = piece  # Place the piece at the destination
    board[start_row - 1][start_col] = ''


    print(f"{piece} piece moved from ({start_row}, {start_col}) to ({end_row}, {end_col})")
    print_board(board)
    return True


def print_board(board):
    for row in board:
        print(row)
