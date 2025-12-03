"""Draw (render) Board."""

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
import pygame

# Light brown color for squares
LIGHT_BROWN = (238, 180, 125)
# Dark brown color for squares
DARK_BROWN = (123, 63, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)


def draw_board(
    board: list[dict[int, str]],
    square_size: int,
) -> pygame.surface.Surface:
    """Return rendered board surface."""
    surface = pygame.Surface((square_size * 8, square_size * 8))

    for row in range(8):
        for col in range(8):
            if (row + col + 1) & 1 == 0:
                square_color = DARK_BROWN
                rect = pygame.Rect(
                    col * square_size,
                    row * square_size,
                    square_size,
                    square_size,
                )

                pygame.draw.rect(surface, square_color, rect)

            else:
                square_color = LIGHT_BROWN
                rect = pygame.Rect(
                    col * square_size,
                    row * square_size,
                    square_size,
                    square_size,
                )

                pygame.draw.rect(surface, square_color, rect)

            # Draw the pieces, if any
            piece = board[row][col + 1]
            radius = square_size // 2 - 5
            center_x = col * square_size + square_size // 2
            center_y = row * square_size + square_size // 2

            if piece == "R":
                pygame.draw.circle(surface, RED, (center_x, center_y), radius)
            elif piece == "B":
                pygame.draw.circle(
                    surface,
                    BLACK,
                    (center_x, center_y),
                    radius,
                )

    return surface
