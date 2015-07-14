#!/bin/zsh

#--------------
# git stuff:
#--------------
source $SETTINGS_ROOT/aliases/_git
#-----------
# General:
#-----------
source $SETTINGS_ROOT/aliases/_general


#-----------
# Searching:
#-----------
source $SETTINGS_ROOT/aliases/_searching


#--------------
# Common typos:
#--------------
source $SETTINGS_ROOT/aliases/_typos

#-------------
# Private commands (not synced with git)
# ------------
if [[ -f $SETTINGS_ROOT/aliases/_private ]];
then
    source $SETTINGS_ROOT/aliases/_private;
fi
