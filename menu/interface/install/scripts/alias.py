#!/usr/bin/env python3
#
# GitHub:   https://github.com/Admin9705/PlexGuide.com-The-Awesome-Plex-Server
# Author:   Admin9705
# URL:      https://plexguide.com
#
# PlexGuide Copyright (C) 2018 PlexGuide.com
# Licensed under GNU General Public License v3.0 GPL-3 (in short)
#
#   You may copy, distribute and modify the software as long as you track
#   changes/dates in source files. Any modifications to our software
#   including (via compiler) GPL-licensed code must also be made available
#   under the GPL along with build & install instructions.
#
#################################################################################
import time
# Import for Bash Ending
from subprocess import call

# Import for Menu Interface
from consolemenu import *
from consolemenu.format import *
from consolemenu.items import *

# If a Variable is Missing, this will ensure it's there
rc = call("touch /var/plexguide/pg.alias.stored", shell=True)

# Call Variables
with open('/var/plexguide/pg.alias', 'r') as myfile:
    starter=myfile.read().replace('\n', '')

with open('/var/plexguide/pg.alias.stored', 'r') as myfile:
    stored=myfile.read().replace('\n', '')

# If True, then Continue; not, do nothing else
if starter == stored:

# Menu Start

    # Change some menu formatting
menu_format = MenuFormatBuilder().set_border_style_type(MenuBorderStyleType.HEAVY_BORDER)\
    .set_prompt("")\
    .set_title_align('center')\
    .set_subtitle_align('left')\
    .set_left_margin(2)\
    .set_right_margin(2)\
    .show_header_bottom_border(True)

menu = ConsoleMenu("INSTALLING: PG Alias",
                   prologue_text=("Alias are custom commands such as plexguide, pgfork, pgedge that install on your box! PLEASE STANDBY!"))
menu.formatter = menu_format
item1 = MenuItem("Item 1", menu)
# Finally, we call show to show the menu and allow the user to interact
menu.start()

# Sleep 5 Seconds
time.sleep(5)
