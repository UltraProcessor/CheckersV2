"""Draw Pieces."""

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

# Draw the pieces, if any

import pygame

# Constants
BLACK = (10, 10, 10)
RED = (255, 0, 0)
LIGHT_BLACK = (50, 50, 50)
DARK_RED = (220, 30, 30)

def draw_pieces(
    surface: pygame.surface.Surface,
    board: list[dict[int, str]],
    square_size: int,
    location: tuple[int, int] = (0, 0),
) -> None:
    """Return rendered pieces."""

    board_x, board_y = location

    for row in range(8):
        for col in range(8):

            # Draw pieces
            piece = board[row][col + 1]
            radius = square_size // 2 - 5
            center_x = col * square_size + square_size // 2
            center_y = row * square_size + square_size // 2

            # If piece is red
            if piece == "R":
                pygame.draw.circle(
                    surface,
                    RED,
                    (center_x + board_x, center_y + board_y),
                    radius,
                )

            # If piece is black
            elif piece == "B":
                pygame.draw.circle(
                    surface,
                    BLACK,
                    (center_x + board_x, center_y + board_y),
                    radius,
                )
                pygame.draw.circle(
                    surface,
                    BLACK,
                    (center_x + board_x, center_y + 1 + board_y),
                    radius,
                )

            # If black piece becomes a "king"
            elif piece == "RR":
                pygame.draw.circle(
                    surface,
                    DARK_RED,
                    (center_x + board_x, center_y + board_y),
                    radius,
                )
                pygame.draw.circle(
                    surface,
                    RED,
                    (center_x + 5 + board_x, center_y + 5 + board_y),
                    radius,
                )

            # If red piece becomes a "king"
            elif piece == "BB":
                pygame.draw.circle(
                    surface,
                    BLACK,
                    (center_x + board_x, center_y + board_y),
                    radius,
                )
                pygame.draw.circle(
                    surface,
                    LIGHT_BLACK,
                    (center_x + 5 + board_x, center_y + 5 + board_y),
                    radius,
                )