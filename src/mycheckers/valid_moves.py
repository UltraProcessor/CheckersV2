"""Valid Moves."""

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


def valid_moves(
    board: list[dict[int, str]],
    row: int,
    col: int,
) -> list[tuple[int, int]]:
    """Return list oc valid move locations for given piece."""
    valid_moves: list[tuple[int, int]] = []

    # sc is 0-based, but dict uses 1-based
    piece = board[row - 1][col]

    directions: list[tuple[int, int]] = []
    # Red pieces move downwards (towards lower rows)
    if piece == "R":
        # down-left: (row+1, col-1), down-right: (row+1, col+1)
        directions = [(1, -1), (1, 1), (2, -2), (2, 2)]

    # Black pieces move upwards (towards higher rows)
    elif piece == "B":
        # up-left: (row-1, col-1), up-right: (row-1, col+1)
        directions = [(-1, -1), (-1, 1), (-2, -2), (-2, 2)]

    # If a red or black king, can move in all directions. Combines "R" and "B" directions.
    elif piece == "RR" or piece == "BB":
        directions = [(1, -1), (1, 1), (2, -2), (2, 2), (-1, -1), (-1, 1), (-2, -2), (-2, 2)]

    # Loop through each direction and check if the move is within bounds
    for direction_row, direction_column in directions:
        new_row = row + direction_row
        new_col = col + direction_column

        # Check if the move is within bounds (1 <= row <= 8 and 1 <= col
        # <= 8) and ensure the destination square is empty (no other
        # pieces present)
        if (
            1 <= new_row <= 8
            and 1 <= new_col <= 8
            and board[new_row - 1][new_col] == ""
        ):
            valid_moves.append((new_row, new_col))

    return valid_moves
