#!/bin/bash

ALIAS_DIR=~/.aliases

if [[  -f "$ALIAS_DIR/_$1" ]];
then
    vim "$ALIAS_DIR/_$1" && source "$ALIAS_DIR/aliases" && echo "Reloaded $ALIAS_DIR/aliases";
else
    echo "File not found"
fi