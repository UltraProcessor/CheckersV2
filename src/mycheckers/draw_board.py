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
BLACK = (10, 10, 10)
RED = (255, 0, 0)


def draw_board(
    surface: pygame.surface.Surface,
    board: list[dict[int, str]],
    square_size: int,
    location: tuple[int, int] = (0, 0),
) -> None:
    """Return rendered board surface."""
    board_x, board_y = location

    for row in range(8):
        for col in range(8):
            if (row + col + 1) & 1 == 0:
                square_color = DARK_BROWN
                rect = pygame.Rect(
                    col * square_size + board_x,
                    row * square_size + board_y,
                    square_size,
                    square_size,
                )

                pygame.draw.rect(surface, square_color, rect)

            else:
                square_color = LIGHT_BROWN
                rect = pygame.Rect(
                    col * square_size + board_x,
                    row * square_size + board_y,
                    square_size,
                    square_size,
                )

                pygame.draw.rect(surface, square_color, rect)