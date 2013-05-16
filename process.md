# Policies and Procedures for experimental use of GitHub by the GeoPackage SWG

## Overview
The GeoPackage SWG intends to experiment with the use of GitHub as a collaboration platform, and the document formats suppored by GitHub -- Markdown and RST -- as a way to evolve the specification editing and public comment process. The versions of draft specifications in GitHub, in whole or in part, should not be considered official positions of the OGC as an organization. In this experimental stage, they are informal, non-normative, communications of the GeoPackage SWG.

## Document Publishing
OGC staff will create a GitHub "team" for use by the GeoPackage SWG, hereafter called the GeoPackage SWG Team (GST). 

1. The SWG will appoint a GST administrator for managing the technical aspects of the GitHub presence. 

1. The SWG Chair will identify the latest version of the draft GeoPackage specification for publishing to GitHub, or a portion thereof. 

1. SWG member(s) will then create a convert the document into Markdown or RST and create a public repository for the GST. The content will be identical to the Microsoft Word version in substance.

1. The SWG votes to approve that the Word document and the GitHub document are substantially the same.

1. GST admin will use GitHub labels and milestones to manage the process of prioritizing and adjuticating comments and changes. 

1. Once the document is formatted and public on GitHub the SWG announces it in typical OGC way: 
  * public a request for comments on http://www.opengeospatial.org/standards/requests
  * add in link to GitHub for the download
  * add in language on the comment section for using GitHub to make comments.
  
## Comments

Comments on the specification can be made in one of two ways:

1. Pull Requests (PRs) that contain the proposed changes to the document, with a comment from the author. These should have a label for the priority. (preferred) 
  * Pull Requests be made for each logical set of changes to the spec, against a user's branch, not their master. Pull Requests that do too many things at once will be rejected and the submitter will be asked to break it up in to multiple pull requests.
  * Submitters should only change their pull requests in dialog with the SWG. In other words after submitting they should not modify their request at all unless asked to by the SWG.
1. If the comment is of a more general nature then create as new 'issues' in the standard GitHub repo issue tracker, with proper labeling as well as a comment on what section of the spec it applies to.

SWG reviews PR and comments, and assigns them to the 'public review <date>' milestone if they are valid.

SWG continues to do their work during the public comment period, marking resolution of issues and PR's by closing the ticket and writing comments in it. (no need to email people, they should be notified automatically on tickets they opened, and they may "watch" the repo). PR's that are accepted will be merged in, possibly with continual dialog on the open PR to refine the resolution.

## Process

* SWG assigns pull requests/tickets to volunteer SWG members to work on resolution of the comment.
  - the volunteer becomes the 'owner', and is expected to move it towards a vote.
  - The owner gets any needed discussion going.
  - A proposed resolution is written in the comments of the ticket by the owner (could just be 'vote we accept this', or could be 'propose to reject this because of x,y,z reasons)
  - Owner marks it as 'ready for vote' and marks the milestone for the next teleconference.
  - ideally dialog happens in the pull requests about the merits, and people +1 in the comments in support of it.
* SWG teleconferences review tickets. 
  - Tickets with lots of comments that aren't resolved are discussed in the meetings. Ideally with an owner assigned to change the PR to reflect the consensus of the group.
  - Tickets with lots of +1's should be moved through quickly, basically most all the 'homework' should be done before the teleconference, telecons are just used to discuss open issues and ratify the +1's in the ticket.
  - An 'editor' either merges the pull request or post the official rejection comment, and closes the ticket.

