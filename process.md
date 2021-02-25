## Using GitHub for GeoPackage comments

### Overview
The GeoPackage Standards Working Group (SWG) intends to experiment with the use of GitHub as a collaboration platform, 
and the document formats supported by GitHub as a way to evolve the standard 
editing and public comment process. The versions of draft specifications in GitHub, in whole or in part, 
should not be considered official positions of the OGC as an organization. In this experimental stage, 
they are informal, non-normative, communications of the GeoPackage SWG.
  
### Comments

Comments on the standard can be made in one of two ways:

1. Issues created in the standard GitHub repo issue tracker. Using the [create a new issue](https://github.com/opengis/geopackage/issues/new) tool, explain the issue as clearly as possible. This can be used for questions, comments, and change requests.
1. Pull Requests (PRs) that contain the proposed changes to the document, with a comment from the author. 
  
   * Pull Requests are made for each logical set of changes to the specification, against a user's branch, not master. Pull Requests that do too many things at once will be rejected and the submitter will be asked to break it up in to multiple pull requests.
   * Submitters should only change their pull requests in dialog with the SWG. In other words after submitting they should not modify their request at all unless asked to by the SWG.


You can review and comment on submitted [pull requests](https://github.com/opengis/geopackage/pulls) and [issues](https://github.com/opengis/geopackage/issues?milestone=5&page=1&state=open).

The SWG will handle labeling of issues and the assignment of milestone.

If accepted the SWG will accept the change or provide a reason as to why it is not incorporated in the ticket, and
then close it.

### Using GitHub

For those who are new to GitHub the following information may help get you up to speed.

#### GUI only Editing

Most everything needed to edit the GeoPackage repository can be done completely through the web with GitHub,
without using git.

You can just hit 'edit' on any of the repository pages.
This will automatically 'fork' the repository in to your own copy.
A fork is a personal copy of a repository.
You can also create a fork before editing by hitting the 'Fork' button at the top right of this page.
You can find more detailed instructions on forking a repo on the 
[Fork A Repo](https://help.github.com/articles/fork-a-repo) page.

To edit the document. we are using [AsciiDoc](https://asciidoc.org/)
For quick hints on AsciiDoc,
this [cheat sheet](https://docs.netapp.com/us-en/contribute/asciidoc_syntax.html) can be quite helpful.

After editing there you can create a '[pull request](https://help.github.com/articles/creating-a-pull-request)' 
from your fork to submit the work for review and merging. You just hit 'compare and review' from your own 
version of the repository, or any branch in it, and then can click to create a pull request right there.

If you are making a more substantial set of changes, or more than one logical change to the spec, it is 
best to create a branch to work on the set. Pull requests are associated with the branches they are made on, so if 
you make more changes based on feedback then all changes can get pulled in when ready. 

Note you can create new branches as well as new files completely through the web. You can even create new
directories:

![creating directories](http://i.stack.imgur.com/n3Wg3.gif)

If there is anything that you need to do with git, but you aren't comfortable with using it and don't want to
learn it, then just create an issue and someone will certainly be able to assist.

#### Using Git

There are countless tutorials on using Git and Github, but we will give a quick overview here and point to
more resources.

After creating your fork of the GeoPackage repository you will need to copy it to your computer (clone). 
The URL of your fork will be https://github.com/username/geopackage.git where username should be replaced by 
your github username. Cloning the repository can be done using the git command-line client 
(git clone https://github.com/username/geopackage.git) or using a git GUI like the GitHub 
[Windows](http://windows.github.com/) or [Mac](http://mac.github.com/) or [SourceTree](http://sourcetreeapp.com/).

Once the repository has been cloned to your computer you can make the changes that 
you would like to suggest. Many text editors have plugins for formatting and previewing AsciiDoc.

Once you're done making your changes, commit them and push them to the github servers. The free 
[Pro Git](http://git-scm.com/book) book provides detailed instructions on [committing 
changes](http://git-scm.com/book/en/Git-Basics-Recording-Changes-to-the-Repository) and 
[pushing changes to a server](http://git-scm.com/book/en/Git-Basics-Working-with-Remotes#Pushing-to-Your-Remotes).

Now that your change has been pushed to github you should initiate a pull request to request that your 
change be integrated in the master copy of the repository. The GitHub [pull request help page](https://help.github.com/articles/using-pull-requests) 
provides detailed instructions on how to do this.


### Process

* SWG assigns pull requests/tickets to volunteer SWG members to work on resolution of the comment.
  - the volunteer becomes the 'owner', and is expected to move it towards a vote.
  - The owner gets any needed discussion going.
  - A proposed resolution is written in the comments of the ticket by the owner (could just be 'vote we accept this', or could be "propose to reject this because of x,y,z reasons")
  - Owner marks it as 'ready for vote' and marks the milestone for the next teleconference.
  - ideally dialog happens in the pull requests about the merits, and people +1 in the comments in support of it.
* Issues are reviewed during SWG teleconferences. 
  - Administrative changes can be approved by a voice vote and can be published through a corregendum (i.e., x.y.z version number).
  - Substantive changes (which make non-editorial changes to requirements) require a SWG motion and can be published through a minor revision (i.e., x.y.0 version number). 
  - Critical changes (which are breaking) require a major revision (i.e., x.0.0). The SWG is not currently chartered to release a major revision of GeoPackage.
  - An 'editor' either merges the pull request or posts the official rejection comment, and closes the ticket.

