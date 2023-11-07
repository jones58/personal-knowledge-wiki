## Basic commands

- `git init` turns git on for current directory
- `git status` to see status of directory (any changed files etc. )
- `git add x file` to add x file to git
- `git diff` to show how a file has changed
- `git add .` to add all files changes
- you can have more than one remote (github repository) that a local repo syncs to, the main one is called origin
- `git remote add <remote-name e.g. origin>`(url of github repo) - to add remote to local repo to link it with github
- `git remote -v` view remote addresses
- `git remote set-url <remote-name><url>` to change a remote url
- `git push <remote name e.g. origin> <branch e.g. master>` push changes to remote repo from local
- `git remote add <remote name e.g.upstream> (url)` to connect to original github of forked repository and be able to pull changes.
- `git status` to see what branch you're on and any changes

- `git merge` to merge git branches. Will work unless there is merge conflict.
- `git pull <remote name> <branch name>` pull changes from remote (github) branch
- `git fetch --dry-run` see changes to the remote before you pull in
- `git status` to check the status of git repo - what files are tracked, what changes have been made etc.

## Staging

`git add .` will add everything in current repo

`git reset .` will set everything back to untracked.

for each of these: if want to just add one file you can give name of that file, don't use .

## Committing

- `git commit-m "message here"` to commit change to git and add "message here" as message
- `git commit -a -m "message` / `git commit -am` to add files and commit in one command.
- `git log` to see history of commits.

## VS Code tricks

File explorer:

- "u" next to file - untracked
- "a" - added. (green)
- "m" - modified (Yellow)
- file removed, goes red

Source control:

- Three dots provides list of commands you can run in git
- Still worth being familiar with git in cli
- In bottom left corner can see the button to click on the branch - can do things like start a new branch by pressing this.

## Github

### Initial steps

- Login to GitHub

- Create your repository on GitHub:

- Open your desired folder that you wish to add to GitHub in VS Code:

- CMD+O then select the desired folder.

- Open up a terminal in VS Code and check that your file path is correct, you want to
  ensure that you are in the correct folder before initialising your Git repository.

- Initial Git Commands:

  - `git init`

  - `git add .`

  - `git commit -m "useful commit message"`

  - `git branch -M main`

  - `git remote add origin (URL of Git Repo)`

  - `git push -u origin main`

Your local repo and centralised GitHub repo should now be linked.

Git Commands to use after initialisation when additional changes are made:

- `git add .`

- `git commit -m "useful commit message"`

- `git push`

##  Remote

- git remote will show what remote git repo is linked to - will not show anything if not connected.
  - can also do git remote show origin to show what's on remote origin.
- `git push origin main -u` - the u here stands for upstream. This basically means you can use pull without any extra arguments. When remote repo is the main source of info.

## Merge and merge conflicts

- when local and online repo have different commits, have to merge them.

Two ways to do this:

1. `git fetch` will download latest changes.
   `git merge origin/master` then merges the changes from origin master on top of local code. origin/master can be any branch here which you want to be on top of other. Will show up as fast-forward - this is the most common merge strategy.
2. `git pull` does both at same time. If didn't use -u (upstream) flag earlier, then don't need to write out fully as `git pull origin/master` which specifies the branch to put on top. That has already been specified by -u (the most up to date repo).
   This will fail if current repo hasn't been commited.

## Clone

- Copy remote repo with `git clone repo-url local-directory` where local directory is your name for your copy of the repo.
- It keeps same git features, like branch etc. so you can pull future updates from remote repo.

## Github Codespaces

- Can edit github online by pressing down . when looking at github file.
- this opens cloud version of vscode
- this can be helpful if want to make small pull request without having to put on local machine with clone.
- if try to use terminal, you can set it up as a codespace running in cloud.

## Collaboration

- It's common to rename master branch to main, do this with: `git branch -M main`

- `git branch` to list branches. Highlighted in green shows current branch.
- `git branch <name>` to create a new branch with `<name>`
- `git branch -d <name>` to delete branch with name. Will only do it if no unmerged changes on it. Use -D to delete no matter what.
- `git branch -m <name>` to rename branch currently on
- `git checkout <name>` to switch branch
- `git checkout -b <name>` to create and switch to a branch in one command
- `git checkout -` to switch back to previous branch.

- Git Lens is a good plugin when working in a team - shows who has made changes.

## Merge conflicts

- Happen when difference on same line between two branches trying to merge.
- Use `git diff` to compare differences on branches.
- Easiest way to fix is in vscode editor, by picking what you want and then committing with something like:
  `git commit -am "resolve merge conflict"`
- If want to abandon merge, can do: `git merge --abort`

## Forking from Github

- copies repo to your own account. Keeps link for updates from the upstream (original) repo.
- when working with fork locally, you can get online changes with:
  - `git remote add upstream <original-url-here>` to sync with original
  - `git fetch upstream` to get changes
  - `git rebase upstream origin/master` to add changes on top of own work.

## Pull request

- Often, will work on repo in fork and then submit pull request to merge changes with original repo.
- Steps:
  - fork repo
  - clone to local repo
  - git branch new branch name
  - git checkout new branch name
  - add, commit, push
  - go back to github and click compare and pull request.
- NB always follow contribution guidelines - best to submit issue first before submitting pull request.

## Fix issues

- `git reset` - unstages all staged files
- `git reset <commit-ID>` - goes back to previous commit but keeps all changes in working directory/ local branch version. Can find commit ids by using `git log`
- `git reset <commit-ID> --hard` - goes back to previous commit and reverts all changes. Be careful and don't use this with commits already on Github. Better to use command below.
- `git revert <commit-ID> -m "reverting last commit"` undo commit with new commit.
- `git commit --amend -m "better message"` - change message of last commit.
- `git add <your-file>` and
  `git commit --amend --no-edit` to add file to previous commit.
- `git stash` adds stuff that can be applied later. To bring them back use `git stash pop`.
- For working with multiple stashes:

  - If want to give name to stash:`git stash save <name>`
  - retrieve list of stashes: `git stash list`
  - then pick stash by its index: `git stash apply 1` where 1 is the index number. This means don't have to use pop, for most recent stash but can choose out of order.

  ## Rebase

  - with large team, rebase is often better than merge.
  - better to do with local feature branches. Not good for other people working on branch remotely.

  - `git checkout <featurebranchname>`
  - `git rebase master`

  - This takes feature branch and puts it on front of master branch. So it looks like editing feature from the latest copy of master branch, rather than old copy that was forked.

## squash

- If have pointless commits, to avoid having too many we can squash them into one commit message:
  `git rebase master --interactive` - replace pic with squash for commits you want to squash into one. - can also use `fixup` - which discards message from commits you're squashing. - this brings up another file where you csan customise commit message. - last thing you do before submitting pull request/new feature into master branch.

## Github Actions

Helps speed up project by automating workflow.

- reusable actions to solve common issues
- Continuous integration: commit code to a shared repo often to avoid merge conflicts
  - specified in .yaml file.
- Continuous deployment: helps push code out to customers, whereas continuous integration is about merging code in
- See also : [https://fireship.io/lessons/five-useful-github-actions-examples/](Github Actions examples)

## Hooks

- Runs some code after an event in git happens. In javascript, [Husky](https://github.com/typicode/husky) package is good. Can lint code etc.

## More git resources

- <https://gitimmersion.com/>
- <https://docs.github.com/en>
- <http://rogerdudler.github.io/git-guide/>
- <https://support.github.com/>
- <https://docs.github.com/en/desktop>
- <https://thenewstack.io/tutorial-git-for-absolutely-everyone/>
- <https://cs.fyi/guide/git-cheatsheet>
- <https://www.atlassian.com/git>
- <https://www.youtube.com/watch?v=ecK3EnyGD8o>
- <https://skills.github.com/>
- <https://learn.foundersandcoders.com/workshops/git-terminal/>
- <https://www.reddit.com/r/webdev/comments/1671gnt/git_cheat_sheets_14_visual_aids/>
- <https://www.youtube.com/watch?v=D80u__nYYWw>
- <https://rogerdudler.github.io/git-guide/>
- <https://fireship.io/courses/git/>
- <https://jvns.ca/blog/2023/11/01/confusing-git-terminology/>

### Github specific resources

- <https://github.com/dwyl/github-reference>
- <https://github.com/Gazler/githug>
- <https://gist.github.com/suewonjp/7493de784f4a88c63d1810031609ee35>

### Github alternatives

<https://git.disroot.org/>
Codeberg
Gitness
Radicle
Bitbucket
Gitlab
