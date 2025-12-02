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

from mycheckers.draw_board import draw_board


def configure_size(screen, board):
    if not hasattr(configure_size, "previous_square_size"):
        configure_size.previous_square_size = -1

    width, height = pygame.display.get_surface().get_size()
    square_size = min(width, height) // 8

    board_size_pixels = square_size * 8
    margin_x = (width - board_size_pixels) // 2
    margin_y = (height - board_size_pixels) // 2

    board_surface = None
    if square_size != configure_size.previous_square_size:
        board_surface = draw_board(board, square_size)
        configure_size.previous_square_size = square_size

    return board_surface, margin_x, margin_y, square_size


def get_square_size():
    window_width, window_height = 640, 640

    window_width, window_height = pygame.display.get_surface().get_size()
    square_size = min(window_width, window_height) // 8

    return square_size


def get_window_dimensions():
    window_width, window_height = pygame.display.get_surface().get_size()

    return window_width, window_height
