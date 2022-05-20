**Table of Contents**

- [Contribution Guidelines](#contribution-guidelines)
- [How to Help](#how-to-help)
- [Contributing Code](#contributing-code)
  - [Fork the Project](#fork-the-project)
  - [Clone Your Fork](#clone-your-fork)
- [Running the Application](#running-the-application)
  - [Manual Mode](#manual-mode)
  - [Docker Mode](#docker-mode)
  - [Web Server Mode](#web-server-mode)
- [Contributing Code](#contributing-code)
- [Frequently Asked Questions](#frequently-asked-questions)

# Contribution Guidelines

Please play nice. We follow this ["Code of Conduct"](https://codeforgreenville.org/about/code-of-conduct).

# How to Help

You don't need to be a "coder" to contribute. Many issues have UI, UX, accessibility, SEO, content / copywriting, and all order of non-code related conversations and improvements to be discussed.

Our focused task-based discussions happen mostly within GitHub [Issues](https://github.com/codeforgreenville/upstate_tech_cal_service/issues) and [Pull Requests](https://github.com/codeforgreenville/upstate_tech_cal_service/pulls) (also known as PRs).

You can also ask questions and connect with the development team in a less structured venue by signing up for [Code For Greenville's Slack and visiting the #hackgreenville channel](https://codeforgreenville.org)

Before starting a new issue, please review and / or search the [current "open" issues](https://github.com/codeforgreenville/upstate_tech_cal_service/issues/) to avoid duplicates.

If you can't find what you were looking for then [open a new issue](https://github.com/codeforgreenville/upstate_tech_cal_service/issues/new) to share your suggestions or bugs.

When in doubt, you can reach out to an active project contributor:

| Name            | GitHub | Role |
|:----------------|:-------|:-----|
| Ramona Spence | [@ramonaspence](https://github.com/ramonaspence) | Primary App Development, Python
| Jim Ciallella | [@allella](https://github.com/allella) | Bugs, Documentation, Newcomer Help, Hosting 


# Contributing Code

If you feel ready to contribute code to this project, then follow the below steps.

<details><summary><b>Step 1</b> - Fork the Repository on GitHub</summary>

['Forking'](https://help.github.com/articles/about-forks/) is a step where you get your own copy of the repository (a.k.a repo) on GitHub.

This is essential as it allows you to work on your own copy of the code. It allows you to request changes to be pulled into the Events API's main repository from your fork via a pull request.

Follow these steps to fork the `https://github.com/codeforgreenville/upstate_tech_cal_service` repository:
1. Go to the [Events API Repo repository on GitHub](https://github.com/codeforgreenville/upstate_tech_cal_service).
2. Click the "Fork" Button in the upper right-hand corner of the interface ([Need help?](https://help.github.com/articles/fork-a-repo/)).
3. After the repository has been forked, you will be taken to your copy of the repository at `https://github.com/YOUR_USER_NAME/upstate_tech_cal_service`.

</details>
<details><summary><b>Step 2</b> - Preparing the Development Environment</summary>

Install [Git](https://git-scm.com/) and a code editor of your choice. We recommend using [VS Code](https://code.visualstudio.com/).

Clone your forked copy of the Events API code. ['Cloning'](https://help.github.com/articles/cloning-a-repository/) is where you download a copy of the repository from a `remote` location to your local machine. Run these commands on your local machine to clone the repository:

1. Open a Terminal in a directory where you would like the Events API project to reside.

2. Clone your fork of the Events API code, make sure you replace `YOUR_USER_NAME` with your GitHub username:

    ```sh
    git clone https://github.com/YOUR_USER_NAME/upstate_tech_cal_service.git
    ```

This will download the entire repository to a `upstate_tech_cal_service` directory.

Now that you have downloaded a copy of your fork, you will need to set up an `upstream`. The main repository at `https://github.com/codeforgreenville/upstate_tech_cal_service` is often referred to as the `upstream` repository. Your fork at `https://github.com/YOUR_USER_NAME/upstate_tech_cal_service` is often referred to as the `origin` repository.

You need a reference from your local copy to the `upstream` repository in addition to the `origin` repository. This is so that you can sync changes from the `upstream` repository to your fork which is called `origin`. To do that follow the below commands:

1. Change directory to the new upstate_tech_cal_service directory:

    ```sh
    cd upstate_tech_cal_service
    ```

2. Add a remote reference to the main Events API GitHub repository. We're refer to this as "HG" in the later steps.

    ```sh
    git remote add upstream https://github.com/codeforgreenville/upstate_tech_cal_service.git
    ```

3. Ensure the configuration looks correct:

    ```sh
    git remote -v
    ```

    The output should look something like below:
    ```sh
    origin    https://github.com/YOUR_USER_NAME/upstate_tech_cal_service.git (fetch)
    origin    https://github.com/YOUR_USER_NAME/upstate_tech_cal_service.git (push)
    upstream    https://github.com/codeforgreenville/upstate_tech_cal_service.git (fetch)
    upstream    https://github.com/codeforgreenville/upstate_tech_cal_service.git (push)
    ```
</details>


<details><summary><b>Step 3</b> - Decide Whether to Run the Application Now, or Later</summary>

It's possible to contribute simple changes, like to README.md, without running the application. However, for many situations you will need to get the application running to view pages, see your code in action, and test changes.  

If you want to proceed immeditely with running the client, database, and server, then follow the steps in the [**Running the Application**](#running-the-application) section, below. Then, return here and continue to the next step of this section. 

</details>

<details><summary><b>Step 4</b> - Make Changes and Test the Code :fire:</summary>

> **Note: Always follow the following steps before starting a new branch or pull request.**

Contributions are made using [GitHub's Pull Request](https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/about-pull-requests) (aka PR) pattern.  This allows anyone to suggest changes for review, commenting, and eventual apporval / merging into the main project's repo.

Before creating a new git "branch" you'll want to sync up with the "remote upstream", which is just a fancy way of saying the main Events API GitHub repo.

1. Save any uncommitted changes using `git stash` because the following steps can possibly reset / delete things in order to stay in sync with the upstream.

2. Validate that you are on the `master` branch

    ```sh
    git status
    ```

    You should get an output like this:
    ```sh
    On branch master
    Your branch is up-to-date with 'origin/master'.

    nothing to commit, working directory clean
    ```

    If you are not on master or your working directory is not clean, resolve any outstanding files/commits and checkout `master`:
    ```sh
    git checkout master
    ```

3. Sync the latest changes from the Events API upstream `master` branch to your local master branch.

   This is very important to avoid conflicts later.

    > **Note:** If you have any outstanding Pull Request that you made from the `master` branch of your fork, you will lose them at the end of this step. You should ensure your pull request is merged by a moderator before performing this step. To avoid this scenario, you should *always* work on a branch separate from master.
    
    This step **will sync the latest changes** from the main repository of HG.

    Update your local copy of the Events API upstream repository:
    ```sh
    git fetch upstream
    ```

    Hard reset your master branch with the Events API master:
    ```sh
    git reset --hard upstream/master
    ```

    Push your master branch to your origin to have a clean history on your fork on GitHub:
    ```sh
    git push origin master --force
    ```

    You can validate if your current master matches the upstream/master or not by performing a diff:
    ```sh
    git diff upstream/master
    ```

    If you don't get any output, you are good to go to the next step.

4. Clean up old branch
  It's also good practice to clean up any orphaned branches from time to time.
    ```sh
    git remote prune origin
    git gc --prune
    ```

2. Selecting a branch name
  Working on a separate branch for each issue helps you keep your local work copy clean. You should never work on the `master` branch. This will soil your copy of the Events API and you may have to start over with a fresh clone or fork.
    
  All new branches / contributions should be made off of the `master` branch, but not in it, as described below.

  Check that you are on `master` as explained previously, and branch off from there by typing:
    ```sh
    git checkout -b fix/update-readme
    ```
  Your branch name should start with `fix/`, `feat/`, `docs/`, etc. Avoid using issue numbers in branches. Keep them short, meaningful and unique.

  Some examples of good branch names are:
    ```
    fix/update-nav-links
    fix/calendar-popup-css
    docs/typos-in-readme
    feat/add-sponsors
    ```

3. Edit files and write code on your favorite editor. Then, check and confirm the files you are updating:

    ```sh
    git status
    ```

    This should show a list of `unstaged` files that you have edited.
    ```sh
    On branch docs/typos-in-readme
    Your branch is up to date with 'upstream/docs/typos-in-readme'.

    Changes not staged for commit:
    (use "git add/rm <file>..." to update what will be committed)
    (use "git checkout -- <file>..." to discard changes in working directory)

        modified:   CONTRIBUTING.md
        modified:   README.md
    ...
    ```

5. Stage the changes and make a commit

    In this step, you should only mark files that you have edited or added yourself. You can perform a reset and resolve files that you did not intend to change if needed.

    ```sh
    git add path/to/my/changed/file.ext
    ```

    Or you can add all the `unstaged` files to the staging area using the below handy command:

    ```sh
    git add .
    ```

    Only the files that were moved to the staging area will be added when you make a commit.

    ```sh
    git status
    ```

    Output:
    ```sh
    On branch docs/typos-in-readme
    Your branch is up to date with 'upstream/docs/typos-in-readme'.

    Changes to be committed:
    (use "git reset HEAD <file>..." to unstage)

        modified:   CONTRIBUTING.md
        modified:   README.md
    ```

    Now, you can commit your changes with a short message like so:

    ```sh
    git commit -m "fix: my short commit message"
    ```

    We highly recommend making a conventional commit message. This is a good practice that you will see on some of the popular Open Source repositories. As a developer, this encourages you to follow standard practices.

    Some examples of conventional commit messages are:

    ```md
    fix: update API routes
    feat: RSVP event
    fix(docs): update database schema image
    ```
    Keep your commit messages short. You can always add additional information in the description of the commit message.

6. Push the new branch to your fork / origin. For example, if the name of your branch is `docs/typos-in-readme`, then your command should be:
    ```sh
    git push origin docs/typos-in-readme
    ```
</details>

<details><summary><b>Step 5</b> - Propose a Pull Request (PR)</summary>

1. Once a branch of your changes has been committed & pushed to your fork / origin you will automatically see a message when you visit your GitHub fork page.

The message will appear near the top of the page saying `Compare and Pull Request` which has a link to start a pull request based on your most recently pushed branch.

2. By default, all pull requests need to be matched against `base repository: codeforgreenville/upstate_tech_cal_service` and `base: master`, which should be the values set in the drop-downs on the left side of the "Comparing Changes" section at the top of the pull request creation page / form.

3. In the body of your PR include a more detailed summary of the changes you made and why.

    - Fill in the details as they seem fit to you. This information will be reviewed and a decision will be made whether or not your pull request is going to be accepted.

    - If the PR is meant to fix an existing bug/issue then, at the end of
      your PR's description, append the keyword `closes` and #xxxx (where xxxx
      is the issue number). Example: `closes #1337`. This tells GitHub to
      automatically close the existing issue, if the PR is accepted and merged.

You have successfully created a PR. Congratulations! :tada:
</details>


# Running the Application
There are three ways to run the appliation:
1. On your local computer using the "Manual Mode"
1. On your local computer using the "Docker Mode"
1. On a server running Apache or Nginx using "Web Server Mode"

## Manual Mode

These steps are for localhost / local testing of the application.

1. **Prerequisite**: follow the fork and clone steps above.  
1. **Prerequisite**: [Install Python](https://wiki.python.org/moin/BeginnersGuide/Download) 3.9, or later.
1. **Prerequisite**: [Install Pipenv](https://pipenv.pypa.io/en/latest/#install-pipenv-today)
	1. Verify the installation with `pipenv --version`, the output should look something like:  
	    > pipenv, version 2021.5.29
1. Run `pipenv install` to install the required Python packages. This installs dependencies listed in the project's Pipfile and creates a virtualenv for the project. 
      1. You can verify the env has been created by checking for it at `~/.local/share/virtualenvs/`
      1. To install a new package, you can use `pipenv install <package-name>`
      1. To activate the subshell, use `pipenv shell`
      1. For more help with available Pipenv commands, use `pipenv -h` 
1. Create a local config.ini file, if one does not exist.
	1. `cp config.ini.example-docker config.ini && nano config.ini`
	1. Fill in the placeholder values in your `config.ini` with the real values for the following, `nano config.ini`
		1. Register your own [Eventbrite token](https://www.eventbrite.com/support/articles/en_US/How_To/how-to-locate-your-eventbrite-api-user-key?lg=en_US)
		1. Flask secret can be any long random string
		1. (No longer needed) Version 3 of the Meetup.com API requires an Oauth Key. However, as of Oct 2019, we're using only public GET API endpoints that require not authentication. It's not necessary to register a Meetup.com API key unless/until the app needs access to an authenticated endpoint, at which point the key could be added to the config file
1. Create a local logging_config.ini file
   1. `cp logging_config.ini.example logging_config.ini`
   1. `mkdir logs`

1. Test with gunicorn WSGI Server on a localhost port
   1. Run the following to generate / update the `all_meetups.json` file in your application directory.
   1. pipenv shell && python update_cal_data.py && exit
   1. Start a "localhost" web server: `gunicorn --bind 0.0.0.0:8000 app:app`
   1. Visit the localhost application in your web browser, and see if it works: `http://localhost:8000/api/gtc?tags=1'`

## Docker Mode

See [the Docker Deploy notes](https://github.com/codeforgreenville/upstate_tech_cal_service/blob/master/deploy_notes_docker.md) for more on using Docker to run the application on a local computer.

## Web Server Mode

See [the Deploy Notes](https://github.com/codeforgreenville/upstate_tech_cal_service/blob/master/deploy_notes_initial.md) if you're trying to run the application under Apache or Nginx on a web server.

# Frequently Asked Questions

<details>
<summary>What do we need help with right now?</summary>

See our [issues queue](https://github.com/codeforgreenville/upstate_tech_cal_service/issues) and [pull requests](https://github.com/codeforgreenville/upstate_tech_cal_service/pulls) for current and previously discussed tasks.
</details>

<details>
<summary>I found a typo. Should I report an issue before I can make a pull request?</summary>

For typos and other wording changes, you can directly open pull requests without first creating an issue. Issues are more for discussing larger problems associated with code or structural aspects of the application.
</details>

<details>
<summary>I am new to GitHub and Open Source, where should I start?</summary>

Read freeCodeCamp's [How to Contribute to Open Source Guide](https://github.com/freeCodeCamp/how-to-contribute-to-open-source).

Then, come back and see our ["How to Help"](#how-to-help) section on how to specificially get involved in this project.
</details>

# Kudos
Thanks to [freeCodeCamp's Chapter project](https://github.com/freeCodeCamp/chapter) for the template for this CONTRIBUTING.md.
