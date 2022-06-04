#!/bin/bash
# Run the command given as parameter (launch ssh server)
# Make sure to run chmod +x entrypoint.sh after creation of this file
echo "running the following command (given as parameter):"
command="\""$@"\""
echo $command
sh -c "\"""$command""\""

echo "exit container"

