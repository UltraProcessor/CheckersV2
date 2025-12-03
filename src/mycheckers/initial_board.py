"""Initial Board."""

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
import math


def initial_board(
    width: int = 8,
    height: int = 8,
) -> list[dict[int, str]]:
    """Return initial board."""
    board = [dict.fromkeys(range(1, width + 1), "") for _ in range(height)]

    player_row_count = math.ceil(height / 3)

    # Place red pieces ('W') on rows 1, 2, 3
    for row in range(player_row_count):
        for col in range(width):
            # Check if the square is dark (for white pieces)
            if (row + col) & 1:
                # Place red piece
                board[row][col + 1] = "R"

    # Place black pieces ('W') on rows 6, 7, 8
    for row in range(height - player_row_count, height):
        for col in range(width):
            # Check if the square is dark (for white pieces)
            if (row + col) & 1:
                # Place red piece
                board[row][col + 1] = "B"

    return board
