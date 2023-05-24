#!/bin/bash
case "$1" in
    Username*) exec echo "$NAME" ;;
    Password*) exec echo "$PASS" ;;
esac