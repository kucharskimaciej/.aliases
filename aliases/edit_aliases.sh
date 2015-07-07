#!/bin/zsh
ALIAS_DIR=$(dirname $0)

if [[ -f "$ALIAS_DIR/_$1" ]];
then
    vim "$ALIAS_DIR/_$1" && source $HOME/.zshrc && echo "Reloaded aliases";
else
    echo "File not found"
fi
