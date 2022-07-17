#!/bin/bash
while getopts s:c:h flag; do
    case "${flag}" in
    s) strategy=${OPTARG} ;;
    c) commit_ini=${OPTARG} ;;
    h) echo "-s <strategy>  -c <auto commit configuration>" ;;
    esac
    if [ -f .env ]; then

        filename=".env"

        strategy_name=$(grep TEST1 $filename | cut -d "=" -f2)
        auto_commit_ini=$(grep TEST2 $filename | cut -d "=" -f2)

        if [[ $strategy != "" && $commit_ini != "" && $auto_commit_ini != "" && $commit_ini != "" ]]; then
            sed -i "s/$strategy_name/$strategy/" $filename
            sed -i "s/$auto_commit_ini/$commit_ini/" $filename
        fi
    fi

done
