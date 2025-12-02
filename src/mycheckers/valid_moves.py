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


def valid_moves(board, piece, row, col):
    valid_moves = []

    # Red pieces move downwards (towards lower rows)
    if piece == 'R':
        # down-left: (row+1, col-1), down-right: (row+1, col+1)
        directions = [(1, -1), (1, 1)]

    # Black pieces move upwards (towards higher rows)
    elif piece == 'B':
        # up-left: (row-1, col-1), up-right: (row-1, col+1)
        directions = [(-1, -1), (-1, 1)]

    else:
        return valid_moves  # If no valid piece, return empty list

    # Loop through each direction and check if the move is within bounds
    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        # Check if the move is within bounds (1 <= row <= 8 and 1 <= col <= 8)
        if 1 <= new_row <= 8 and 1 <= new_col <= 8:
            # Ensure the destination square is empty (no other pieces present)
            if board[new_row - 1][new_col] == '':
                valid_moves.append((new_row, new_col))

    return valid_moves
