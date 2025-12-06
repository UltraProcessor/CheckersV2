"""Checkers Game."""

# Programmed by UltraProcessor

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
import traceback
from typing import Final

import pygame
import trio
from checkers.client import GameClient
from libcomponent.async_clock import Clock
from libcomponent.component import ExternalRaiseManager

from mycheckers.configure_screen import (
    color_screen_black,
    configure_screen,
    configure_size,
    get_window_dimensions,
)

from mycheckers.draw_board import draw_board
from mycheckers.draw_pieces import draw_pieces
from mycheckers.initial_board import initial_board
from mycheckers.move_piece import move_piece, print_board
from mycheckers.valid_moves import valid_moves

FPS: Final = 48

# Commit: Delete configure_size.py and put functions into configure_screen.py, add main_menu

def draw_menu_button(screen: pygame.surface.Surface,
                    text: str,
                     x: int,
                     y: int,
                     width: int,
                     height: int
) -> pygame.Rect:

    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, (180, 0, 0), rect, border_radius=8)
    pygame.draw.rect(screen, (0, 0, 0), rect, 3, border_radius=8)

    FONT = pygame.font.SysFont("arial", 30)

    label = FONT.render(text, True, (255, 255, 255))

    screen.blit(label, (x + (width - label.get_width())//2,
                     y + (height - label.get_height())//2))
    return rect


def main_menu(screen: pygame.surface.Surface) -> int:
    response = -1

    window_width, window_height = get_window_dimensions()

    run = True
    while run:
        color_screen_black(screen)

        FONT = pygame.font.SysFont("arial", 40)

        title = FONT.render("CHEKURS™️", True, (255, 255, 255))

        screen.blit(title, (window_width // 2 - title.get_width() // 2, 50))

        solo_btn = draw_menu_button(screen, "Solo", 200, 170, 200, 60)
        pvsai_btn = draw_menu_button(screen, "Player vs. AI", 200, 260, 200, 60)
        multi_btn = draw_menu_button(screen,"Multiplayer", 200, 350, 200, 60)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if solo_btn.collidepoint(event.pos):
                    return 0
                if pvsai_btn.collidepoint(event.pos):
                    return 1
                if multi_btn.collidepoint(event.pos):
                    return 2

    return response



def redraw_board(
    screen: pygame.surface.Surface,
    board: list[dict[int, str]],
    square_size: int,
    location: tuple[int, int] = (0, 0),
) -> None:
    """Render game board."""
    color_screen_black(screen)

    draw_board(screen, board, square_size, location)
    draw_pieces(screen, board, square_size, location)

def handle_left_click_event(
    event: pygame.event.Event,
    screen: pygame.surface.Surface,
    board: list[dict[int, str]],
    selected_piece: tuple[int, int] | None = None,
) -> tuple[int, int] | None:
    """Return selected piece."""
    margin_x, margin_y, square_size = configure_size(screen.get_size())

    mx, my = event.pos

    col = (mx - margin_x) // square_size
    row = (my - margin_y) // square_size

    if row < 0 or row >= 8:
        return selected_piece
    if col < 0 or col >= 8:
        return selected_piece

    key = col + 1
    piece = board[row][key]

    # Get a valid piece
    if piece != "":
        selected_piece = (row, col)
        selected_moves = valid_moves(
            board,
            row + 1,
            col + 1,
        )
        print(f"Selected {piece} at {(row, col)}")
        print("Moves:", selected_moves)

        return selected_piece

    # If already selected, continue
    if selected_piece:
        selected_row, selected_col = selected_piece
        # sc is 0-based, but dict uses 1-based
        piece = board[selected_row][selected_col + 1]

        # Try to move, convert to 1-based coordinates
        moved = move_piece(
            board,
            selected_row + 1,
            selected_col + 1,
            row + 1,
            col + 1,
        )

        if moved:
            print(
                f"{piece} piece moved from ({selected_row + 1}, {selected_col + 1}) to ({row + 1}, {col + 1})",
            )
            print_board(board)

            redraw_board(screen, board, square_size, (margin_x, margin_y))

            return None

        print(
            f"Invalid move from ({selected_row + 1}, {selected_col + 1}) to ({row + 1}, {col + 1})",
        )
    return selected_piece


async def run() -> None:
    """Event loop."""
    running = True

    # Initial draw
    screen = configure_screen()

    print("Initializing starter board..")
    board = initial_board()

    print_board(board)

    margin_x, margin_y, square_size = configure_size(screen.get_size())
    redraw_board(screen, board, square_size, (margin_x, margin_y))

    selected_piece: tuple[int, int] | None = None  # (row, col)

    clock = Clock()

    async with trio.open_nursery() as main_nursery:
        event_manager = ExternalRaiseManager(
            "checkers",
            main_nursery,  # "client"
        )

        async with GameClient("game_client") as client:
            with event_manager.temporary_component(client):
                while running:
                    # Event handling
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False

                        elif (
                            event.type == pygame.KEYUP
                            and event.key == pygame.K_ESCAPE
                        ):
                            # Trigger quit if presses the escape key
                            pygame.event.post(pygame.event.Event(pygame.QUIT))

                        elif (
                            event.type == pygame.MOUSEBUTTONDOWN
                            and event.button == 1
                        ):
                            selected_piece = handle_left_click_event(
                                event,
                                screen,
                                board,
                                selected_piece,
                            )
                        elif event.type == pygame.WINDOWRESIZED:
                            margin_x, margin_y, square_size = configure_size(screen.get_size())
                            redraw_board(screen, board, square_size, (margin_x, margin_y))

                    # --- CLOCK ---
                    _time_passed_ns = await clock.tick(FPS)

                    # --- DRAWING ---
                    pygame.display.update()


def main() -> None:
    """Run game."""
    # Initialize pygame
    pygame.init()
    try:
        screen = configure_screen()
        response = main_menu(screen)

        if response == 0:
            print("Launching solo game..")
            trio.run(run)

        elif response == 1:
            print("Launching player vs. AI..")
            trio.run(run)

        elif response == 2:
            print("Launching multiplayer..")
            trio.run(run)

        else:
            print("Something went wrong")

    except BaseException as exc:
        traceback.print_exception(exc)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
