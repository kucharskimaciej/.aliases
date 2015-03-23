#!/bin/bash

ALIAS_DIR=~/.aliases

# colors
red='\033[0;31m'
green='\033[0;32m'
NC='\033[0m' # No Color
reg="(alias )([a-zA-Z0-9]+)(='(.+)')?(\s#.+)?"
fn_reg="(function )?([a-zA-Z0-9]+)(\s\(\)\s+\{\s+(.+)\s+\})"

tmp_file_reg="~$"

for node in "$ALIAS_DIR"/_*
do
    if [[ $node =~ $tmp_file_reg ]];
    then
        continue;
    fi
    echo -e "${red}$(echo $node | grep -Po '[a-zA-Z0-9]+$')${NC}"
    while read ALIAS
    do
        if [[ $ALIAS =~ $fn_reg ]];
        then
            printf "${green}%-10s${NC} %-50s\n" "${BASH_REMATCH[2]}" "${BASH_REMATCH[4]}"
        fi
        if [[ $ALIAS =~ $reg ]];
        then
            printf "${green}%-10s${NC} %-50s\n" "${BASH_REMATCH[2]}" "${BASH_REMATCH[4]}"
        fi

    done < $node
    echo -e ""
done