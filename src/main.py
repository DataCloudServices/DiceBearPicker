"""
Main script
===========

Just the main.

AUTHOR
    rafidini@GitHub

CREATED AT
    Sat. 23 Apr. 2022 00:28
"""
# External packages
import ui
from dicebear.styles import micah 

# User interface
ui.main_page(
    styles=[micah],
    api_endpoint="https://avatars.dicebear.com/api"
)
