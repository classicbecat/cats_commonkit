Cats_Commonkit

Version: 1.0 Alpha
Author: classicbecat
License: GNU AGPL v3.0

About

Cats_Commonkit is a simple Python utility library containing basic functions for clearing the terminal, adding delays, and displaying menu text.

Functions
clear() — Clears the terminal screen.
wait(wt) — Pauses the program for a specified number of seconds.
menu_one(menu_text) — Displays a simple menu with a title.
menu_two(menu_text, menu_text_sub) — Displays a menu with a title and subtitle.
Usage

Import the file into your Python project and call its functions.

import Cats_Commonkit

Cats_Commonkit.clear()
Cats_Commonkit.wait(1)
Cats_Commonkit.menu_one("Main Menu")
Cats_Commonkit.menu_two("Main Menu", "Settings")

Requirements
Python 3
No external dependencies
License

This project is licensed under the GNU Affero General Public License v3.0 (AGPL-3.0).
