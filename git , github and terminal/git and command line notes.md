
- ```pwd``` print working directory
- ```mkdir x``` to make a new folder, x 
- ```cd x``` to change directory to that folder, x 
- ```touch x``` to create a file with name x
- ```cd ./x``` to go to x directory (not necessarily within current directory)
- ```ls``` list items in a folder
-  ```git init``` turns git on for current directory
- ```git status``` to see status of directory (any changed files etc. )
- ```git add x file``` to add x file to git
- ```git commit-m "message here"``` to commit change to git and add "message here" as message
- ```git diff``` to show how a file has changed 
- ```git add .``` to add all files changes
- you can have more than one remote (github repository) that a local repo syncs to, the main one is called origin
- ```git remote add <remote-name e.g. origin>```(url of github repo) - to add remote to local repo to link it with github
- ```git remote -v``` view remote addresses
- ```git remote set-url <remote-name><url>``` to change a remote url
- ```git push <remote name e.g. origin> <branch e.g. master>``` push changes to remote repo from local
- ```cd ..``` two dots mean step out of directory one level
- ```git remote add <remote name e.g.upstream> (url)``` to connect to original github of forked repository and be able to pull changes. 
- ``git status`` to see what branch you're on and any changes 
- ``git branch <branch name>`` to make new branch off existing one
- ```git checkout <branch name>``` to switch branch
- ``git checkout -b <branch name>`` to create and switch to a branch in one line
- ``git branch`` to list branches
- ``git branch -m <New branch name>`` to rename branch currently on 
- ``git pull <remote name> <branch name>`` pull changes from remote (github) branch 
- ``git fetch --dry-run`` see changes to the remote before you pull in













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




- Can edit github online by pressing down . when looking at github file. 
- There is also github cli for working in the command line. 
- \- git is one option for version control and  is local
- -git commit – one point in time
- Can git merge different changes
- Lots of commands, gets harder but is easy to start with
- Git init my-first-git
- Cd my-first-git (create file 1)
- Git add file1.txt 
- Git commit -m”my first commit” 
- Designed to fit into the background
- Journal not a backup
- github is case-sensitive

name files and folders in lowercase and use dashes instead of spaces - kebab-case 

path components in browser 

/folder 

./ current folder - this is done by default so 
../ go up one folder level 
folder-name/ directs browser into a folder with that name

relative urls for same domain 
absolute urls for different domain


More git resources: 
- https://gitimmersion.com/
- https://docs.github.com/en
- http://rogerdudler.github.io/git-guide/
- https://support.github.com/
- https://docs.github.com/en/desktop