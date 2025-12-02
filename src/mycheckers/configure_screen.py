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

def configure_screen():
    window_width, window_height = 640, 640

    pygame.display.set_caption("Checkers Game")
    screen = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)

    return screen


def color_screen_black(screen):
    screen.fill(BLACK)

    return screen

