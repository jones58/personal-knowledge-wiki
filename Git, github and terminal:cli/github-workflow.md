Establishing an effective GitHub workflow is crucial for maintaining organization and facilitating project upkeep. As projects grow in size, keeping track of changes and understanding contributors' contributions becomes increasingly important.

Here are some key considerations:

- Ensure that all team members adopt the same code formatter ([prettier](https://prettier.io/docs/en/install.html)) to prevent merge conflicts arising from inconsistent formatting.

- Avoid making changes directly to the main branch. Instead, pull the latest changes from main and create a new branch for your work:

  ```bash
  git checkout main
  git pull
  git checkout -b "fix-login-button"
  ```

- Commit frequently to make it easier to revert specific changes:

  ```bash
  git add .
  git commit -m "fix bug with login button"
  ```

- Craft meaningful commit messages following the convention of using imperative language (e.g., "add tests for signup form").

- Ensure that commit messages make sense when read in the format: "If applied, this commit will: `<your commit message>`."

- If you forget to commit during a coding session, utilize VSCode's ability to [stage selected lines](https://stackoverflow.com/questions/34730585/how-can-i-commit-some-changes-to-a-file-but-not-others-in-vscode) from the source control panel.

- When pair programming, remember to co-commit, as outlined in the [GitHub Docs](https://docs.github.com/en/github/committing-changes-to-your-project/creating-and-editing-commits/creating-a-commit-with-multiple-authors).

- Before pushing your branch, ensure it's up-to-date with the main branch:

  ```bash
  git pull origin main
  git push origin <type-current-branch-name-here>
  ```

- [Link pull requests to issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue) and close issues upon completion.

- Conduct team reviews of pull requests and opt for collaborative merging. In smaller projects with tight deadlines, ensure your pair is aware of your changes and their potential impact on their code.
