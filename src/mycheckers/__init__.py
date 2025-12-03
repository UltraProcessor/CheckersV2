"""MyCheckers -  Alternative solution for checkers game."""

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

__title__ = "MyCheckers"
__author__ = "UltraProcessor"
__version__ = "0.1.0"
__license__ = "GNU General Public License Version 3"


from mycheckers.game import main as main

if __name__ == "__main__":
    print(f"{__title__} v{__version__}\nProgrammed by {__author__}.\n")
    main()
