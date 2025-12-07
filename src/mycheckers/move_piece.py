"""Move Piece."""

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
from mycheckers.valid_moves import valid_moves, valid_captures


def move_piece(
    board: list[dict[int, str]],
    start_row: int,
    start_col: int,
    end_row: int,
    end_col: int,
) -> bool:
    """Return if able to move or capture pieces from start position to end position successfully."""
    possible_moves = valid_moves(board, start_row, start_col)
    possible_captures = valid_captures(board, start_row, start_col)

    # Get current piece and any possible locations
    piece = board[start_row - 1][start_col]
    mid_row = (start_row + end_row) // 2
    mid_col = (start_col + end_col) // 2


    # If it's a capture, add possible_captures to possible_moves
    if board[mid_row - 1][mid_col] != "":

        # Append movesets from valid_captures into possible_moves
        possible_moves += possible_captures
        print("Added moves: ", possible_moves)

    # If move is not in the list of valid moves, return false.
    if (end_row, end_col) not in possible_moves:
        return False

    if board[mid_row - 1][mid_col] != "":
        # Remove the captured piece
        board[mid_row - 1][mid_col] = ""

    # Move & place the piece at the destination
    board[end_row - 1][end_col] = piece
    # Erase original location
    board[start_row - 1][start_col] = ""

    # If red and in enemy's territory, promote to king
    if piece == "R" and end_row == 8:
        print("Promoting to king..")
        board[end_row - 1][end_col] = "RR"

    # If black and in enemy's territory, promote to king
    if piece == "B" and end_row == 1:
        print("Promoting to king..")
        board[end_row - 1][end_col] = "BB"

    return True


def print_board(board: list[dict[int, str]]) -> None:
    """Print board data."""
    board_string = ""
    for row in board:
        for _column, value in row.items():
            if value:
                if len(value) == 1:
                    display = value.upper() + " "
                elif len(value) == 2:
                    display = value.upper()
                else:
                    display = "  "
            else:
                display = "  "  # empty square

            board_string += f"[ {display} ]"
        board_string += "\n"

    print(board_string)
