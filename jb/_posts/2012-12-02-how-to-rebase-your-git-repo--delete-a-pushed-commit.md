---
layout: post
title: "How to rebase your git repo / delete a pushed commit"
description: ""
category: 
tags: [git, skills]
---
{% include JB/setup %}

If you have a commit (or some commits / some huge files) that you
really want to totally delete from your repo, to make it cleaner or
smaller, you can create a new repo, and use a "git-rebase" command to
do it.

The best place of this operation is to delete the stuff you don't want
while **preserving all the historical commits** of the original
repository.

Suppose the old repo is repo_a, and you should go through this process:

* Create a new empty repo, say, "repo_b".
* Do not clone repo_b; instead, copy the repo_a to repo_b: 

        $ cp -r repo_a repo_b 
        $ cd repo_b

* Find the commit you want to delete. For example, you want to delete 
  the commit with a huge file in
  somepath/hugefile. You can locate the commit by *git log*:

        $ git log somepath/hugefile

  then you get a commit-id of the commit you want to delete.

* Then tag your commit using this:

        $ git tag TODELETE commit-id

* use the MAGIC rebase:

        $ git rebase -i TODELETE~1

  This will start the rebase in interactive mode -i at the point just
  before the commit you want to whack. The editor will start up
  listing all of the commits since then. Delete the line containing
  the commit you want to obliterate and save the file. Rebase will do
  the rest of the work, deleting only that commit, and replaying all
  of the others back into the log.
  [Reference](http://stackoverflow.com/questions/1338728/how-to-delete-a-git-commit)

  It will show a message, on top of the message there are a set of
  "pick" commands. Find the one who pick the TODELETE commit, and
  delete that line.

  Save the message, and the rebase is done! the TODELETE commit is
  gone!

* Check if it is really gone, by either of these commands:

          $ git log 
          $ git hist (if you have configured alias "hist")

  and you find that in master branch you do not have TODELETE commit anymore.

  If you use 

          $ git log --all
          $ git hist --all (if you have configured alias "hist")

  you can see that the *rebase* creates a branch.

* Push the change to the new repository

        $ git remote remove origin git remote add origin

        $ git@YOUR_REMOTE_PATH/repo_b.git git push -u origin master 
          # to push changes for the first time

* This will change the "origin" of the local repo_b, to the remote
  repo_b, and do the initial push of the new repo.

* Delete and clone the new repo: Now the repo_b still contains 
  TODELETE in a branch, so you can delete it and clone it from 
  remote. Now it is clean.


