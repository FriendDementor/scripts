#!/bin/bash
# Check if in the actual branch of git $1 can be merged with ff

gitinstall=$(git --version | grep -c "git version")
gitstatus=$(git status | grep -c "On branch")

if [[ $gitinstall > 0 ]];
then
    #if [[ $gitstatus > 0 ]];
    #then
    #    echo "git repo found :)"
        git merge-base $1 HEAD
        git rev-parse HEAD
    #else
    #    echo "git repository not found";
    #fi 
else
    echo "git install not found"
fi

