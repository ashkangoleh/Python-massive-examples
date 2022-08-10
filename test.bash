#/usr/bin/env bash

arg_value=${1:-pizza}
arg_value2=${2:-cheese}

if
    [ $arg_value == "pizza"] &
    [ $arg_value2 == "cheese" ]
then
    echo "with pineapple?"
else
    echo "bye bye bye"
fi
