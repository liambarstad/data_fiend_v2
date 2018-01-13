#!/bin/sh

main_menu()
{
  if [ ! -z $1 ]; then
    case $1 in
      startup)
        startup $2
        ;;
      test)
        tests $2
        ;;
      *)
        echo "Invalid option ${1} selected"
        exit 1
        ;;
    esac
  else
    tests
    startup
  fi
}

startup()
{
  if [ ! -z $1 ]; then
    case $1 in
      cerberus) 
        echo "booting up ${1}..."
        python cerberus/main.py
        ;;
      daedalus)
        echo "booting up ${1}..."
        python daedalus/main.py
        ;;
      *)
        echo "Invalid option ${1} selected"
        exit 1
        ;;
    esac
  else
    echo "booting up..."
    python cerberus/main.py &
    python daedalus/main.py
  fi
}

tests()
{
  if [ ! -z $1 ]; then
    case $1 in
      cerberus)
        echo "testing ${1}..."
        nosetests cerberus/tests
        ;;
      daedalus)
        echo "testing ${1}..."
        nosetests daedalus/tests
        ;;
      *)
        echo "Invalid option ${1} selected"
        exit 1
        ;;
    esac
  else
    echo "testing..."
    nosetests cerberus/tests
    nosetests daedalus/tests
  fi
}

ARG0=$1
ARG1=$2
main_menu $ARG0 $ARG1
