
- ```git init``` turns git on for current directory
- ```git status``` to see status of directory (any changed files etc. )
- ```git add x file``` to add x file to git
- ```git diff``` to show how a file has changed
- ```git add .``` to add all files changes
- you can have more than one remote (github repository) that a local repo syncs to, the main one is called origin
- ```git remote add <remote-name e.g. origin>```(url of github repo) - to add remote to local repo to link it with github
- ```git remote -v``` view remote addresses
- ```git remote set-url <remote-name><url>``` to change a remote url
- ```git push <remote name e.g. origin> <branch e.g. master>``` push changes to remote repo from local
- ```git remote add <remote name e.g.upstream> (url)``` to connect to original github of forked repository and be able to pull changes.
- ``git status`` to see what branch you're on and any changes
- ``git branch <branch name>`` to make new branch off existing one. Then can work with other developers on features.``
- ```git checkout <branch name>``` to switch branch
- ``git checkout -b <branch name>`` to create and switch to a branch in one line
- ``git merge`` to merge git branches. Will work unless there is merge conflict.
- ``git branch`` to list branches
- ``git branch -m <New branch name>`` to rename branch currently on
- ``git pull <remote name> <branch name>`` pull changes from remote (github) branch
- ``git fetch --dry-run`` see changes to the remote before you pull in
- ``git status`` to check the status of git repo - what files are tracked, what changes have been made etc.

## Staging

``git add .``  will add everything in current repo

``git reset .`` will set everything back to untracked.

for each of these: if want to just add one file you can give name of that file, don't use .

## Committing

- ```git commit-m "message here"``` to commit change to git and add "message here" as message
- ``git commit -a -m "message`` / ``git commit -am`` to add files and commit in one command.
- ``git log`` to see history of commits.

## VS Code tricks

- "u" next to file - untracked
- "a" - added. (green)
- "m" - modified (Yellow)
- file removed, goes red
in source control - three dots provides list of commands you can run in git

still worth being familiar with git in cli

in bottom left corner

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

More git resources:

- <https://gitimmersion.com/>
- <https://docs.github.com/en>
- <http://rogerdudler.github.io/git-guide/>
- <https://support.github.com/>
- <https://docs.github.com/en/desktop>
- <https://thenewstack.io/tutorial-git-for-absolutely-everyone/>
- <https://cs.fyi/guide/git-cheatsheet>
- <https://www.atlassian.com/git>
