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
from mycheckers.valid_moves import valid_moves


def move_piece(
    board: list[dict[int, str]],
    start_row: int,
    start_col: int,
    end_row: int,
    end_col: int,
) -> bool:
    """Return if able to move piece from start position to end position successfully."""
    possible_moves = valid_moves(board, start_row, start_col)

    piece = board[start_row - 1][start_col]

    # If move is not in the list of valid moves, return false.
    if (end_row, end_col) not in possible_moves:
        return False

    # If it's a capture, remove the piece that is jumped over
    if abs(end_row - start_row) == 2 and abs(end_col - start_col) == 2:
        mid_row = (start_row + end_row) // 2
        mid_col = (start_col + end_col) // 2
        # Remove the captured piece
        board[mid_row - 1][mid_col] = ""

    # Move the piece
    # Place the piece at the destination
    board[end_row - 1][end_col] = piece
    # Erase original location
    board[start_row - 1][start_col] = ""

    return True


def print_board(board: list[dict[int, str]]) -> None:
    """Print board data."""
    print("\n".join(map(repr, board)))
