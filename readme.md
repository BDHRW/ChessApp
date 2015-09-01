#Chess App, Powered by Django


Basic Git info.

Before you make changes make sure you are always up to date with your code-base (`git pull origin master`). If you need to have the codebased halted to work on a certain feature, create a new branch. If you accept your changes, merge it in the code-base (Its called google)

Setup Guide
---

Clone the repository

    $ git clone (REMOTE)

Remote represents the url to the project. (If your using ssh keys, use the git@github.com to access the project) (If you are using https simply use the url of the main page of the project with .git appended to the end)

Virtual Environments
---

In your terminal run (Ignore `$`, it represents bash)

`$ virtualenv env` to create a virtual environment

Activate the virtualenv (you must be in the same directory as your `env` folder)

###[Its a UNIX system](https://www.youtube.com/watch?v=dFUlAQZB9Ng) (Mac/Linux)

`$ source env/bin/activate`

###[Windows](https://www.youtube.com/watch?v=kGYcNcFhctc)

(In Git bash, may be different for other terminal emulators)

`$ source env/Scripts/activate`


Install what we need (Make sure you are in your virtualenv)

`$ pip install django`

WIP - Quick write up to make sure this project isn't destroyed earlier on. Will add Django info next
