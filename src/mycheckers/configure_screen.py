"""Configure Screen."""

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

# Constants
BLACK = (0, 0, 0)


def configure_screen() -> pygame.surface.Surface:
    """Configure display."""
    window_width, window_height = 640, 640

    pygame.display.set_caption("Checkers Game")
    return pygame.display.set_mode(
        (window_width, window_height),
        pygame.RESIZABLE,
    )


def color_screen_black(screen: pygame.surface.Surface) -> None:
    """Fill screen black."""
    screen.fill(BLACK)


def configure_size(
    screen_size: tuple[int, int],
) -> tuple[int, int, int]:
    """Return (x margin, y margin, square size)."""
    width, height = screen_size
    square_size = get_square_size(screen_size)

    board_size_pixels = square_size * 8
    margin_x = (width - board_size_pixels) // 2
    margin_y = (height - board_size_pixels) // 2

    return margin_x, margin_y, square_size


def get_square_size(
    screen_size: tuple[int, int],
) -> int:
    """Return square size."""
    window_width, window_height = screen_size
    return min(window_width, window_height) // 8


def get_window_dimensions() -> tuple[int, int]:
    """Return window dimensions."""
    return pygame.display.get_surface().get_size()