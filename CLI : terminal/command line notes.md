# Command Line Notes

- `pwd` print working directory
- `mkdir x` to make a new folder, x
- `cd x` to change directory to that folder, x
- `touch x` to create a file with name x
- `cd ./x` to go to x directory (not necessarily within current directory)
- `ls` list items in a folder
- `cd ..` two dots mean step out of directory one level

some more command line tips:
`!!` # run the last command executed
`sudo !!` # run the last command as root
`I<word>` # run last command starting with a specific word
`! word:p` # ^ list, but don't run that last command
`<space>command` # execute a command w/out saving in history
`echo "Is -1" | at midnight` # execute command at given time
`caffeinate -u -t 3600` # stop your mac from sleeping for 1h
`1s -lhS` # sort files by size in a directory
`qlmanage -p <file>` # QuickLook preview from command-line
`top -o vsize` # why is my mac slow?

name files and folders in lowercase and use dashes instead of spaces - kebab-case

path components in browser

/folder

./ current folder - this is done by default so
../ go up one folder level
folder-name/ directs browser into a folder with that name

relative urls for same domain
absolute urls for different domain

can write `clear` in terminal to clear it
