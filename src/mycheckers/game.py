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
#from libcomponent import async_clock
#import trio

# Functions from the other files

from mycheckers.configure_screen import configure_screen, color_screen_black
from mycheckers.configure_size import configure_size, get_square_size, get_window_dimensions
from mycheckers.draw_board import draw_board
from mycheckers.initial_board import initial_board
from mycheckers.move_piece import move_piece
from mycheckers.valid_moves import valid_moves


def run():
    """Main game loop."""
    running = True

    # Initial draw
    screen = configure_screen()
    board = initial_board()
    square_size = get_square_size()
    board_surface = draw_board(board, square_size)
    margin_x, margin_y = 0, 0

    current_player = "R"
    selected_piece = None  # (row, col)
    selected_moves = []

    while running:

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = pygame.mouse.get_pos()

                col = (mx - margin_x) // square_size
                row = (my - margin_y) // square_size

                if 0 <= row < 8 and 0 <= col < 8:
                    key = col + 1
                    piece = board[row][key]

                    # Get a valid piece
                    if piece != "":
                        selected_piece = (row, col)
                        selected_moves = valid_moves(board, piece, row + 1, col + 1)
                        print(f"Selected {piece} at {(row, col)}")
                        print("Moves:", selected_moves)

                    # If already selected, continue
                    elif selected_piece:
                        selected_row, selected_col = selected_piece
                        piece = board[selected_row][selected_col + 1]  # sc is 0-based, but dict uses 1-based

                        # Try to move, convert to 1-based coordinates
                        moved = move_piece(board, piece, selected_row + 1, selected_col + 1, row + 1, col + 1)

                        if moved:
                            # switch players
                            current_player = "r" if current_player == "b" else "b"
                            selected_piece = None
                            selected_moves = []
                            board_surface = draw_board(board, square_size)

                        else:
                            print("Invalid move")

        # --- SCREEN COLOR ---
        color_screen_black(screen)

        # --- RESIZE HANDLING ---
        new_board_surface, margin_x, margin_y, new_size = configure_size(screen, board)

        if new_board_surface is not None:
            board_surface = new_board_surface
            square_size = new_size

        # --- DRAWING ---
        screen.blit(board_surface, (margin_x, margin_y))
        pygame.display.update()


def main() -> None:
    """Run game."""
    # Initialize pygame
    pygame.init()
    try:
        run()
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
