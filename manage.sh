#!/bin/sh

main_menu()
{
  case $1 in
    startup)
      startup $argv[2]
      ;;
    test)
      tests $argv[2]
      ;;
    *)
      startup $argv[2] &
      tests $argv[2]
      ;;
  esac
}

startup()
{
  case $1 in
    cereberus)
      python cerberus/main.py
      ;;
    daedalus)
      python daedalus/main.py
      ;;
    *)
      python cerberus/main.py
      #python daedalus/main.py
      ;;
  esac
}

main_menu $argv[1]
