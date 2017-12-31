# CCS PC Chair's Guide

The main tasks for the PC Chair are:

- (November-March) [Forming the PC](#pc)
- (March-April) [Writing the Call for Papers](#cfp)
- (March-May) Preparing for the review process
- (mid-May) Paper submission deadline
- (May-August) [Managing the review process](#reviewing)
- (July-September) [Test-of-Time Award](#tot)
- (August) [Posting the accepted papers](#posting)
- (August-September) Planning the sessions
- (August-September) [Selecting the Awards](#awards), Program Chair's Welcome
- (October-November) Conference
- (November-January) Post-Conference

# <a name="pc"></a>Forming the Program Committee

The biggest mistake most PC chairs make is starting from the previous
year's PC and making some adjustments from there. This leads to
ossified program committees.  The CCS 2016 had taken this approach,
and ended up with a committee that was over 65% overlapping with CCS
2015.

Its important to have some continuity and include some senior
community members in the PC, but also important that no one becomes a
"tenured" PC member and that there is substantial turnover between
program committees each year, and that there are ample opportunities
for new researchers to participate in PCs. A good target is to have
about 20-30% of the PC be returning from the past year, but the
majority of PC members should be new.

The directory [/pc/](/pc) contains scripts I developed for analyzing
data on PC members for major security conferences, and data on who was
on the PCs (this was mostly collected by cut-and-pasting from
conference websites, and then attempting to clean up the data as much
as possible manually. It was remarkable how many people's names were
mispelled on the official conference sites!).  I did not find a good
way to collect data on authors, but Davide Balzarotti's [_System
Security Circus_](http://s3.eurecom.fr/~balzarot/notes/top4/) site
provides some useful stats.

We automatically eliminated from consideration anyone who had been on
the previous three CCS PCs (2014, 2015, and 2016) since we didn't want
to have any 4-time repeat PC members. To maintain some consistency, we
looked at all the PC members who had been on exactly 2 of the past 3
PCs, and selected a subset of those to invite. Then, we looked for
potential new candidates from various sources: people who had
published in CCS 2016, new PhDs in computer security and cryptography,
and people who were on PCs for other conferences.  We also received a
handful of requests from people wanting to be on the PC. We considered
volunteering to be a strong positive, except in cases when it seems
motivated by career desparation, and generally invited volunteers who
had published in recent top-tier conferences and seemed qualified to
be on the PC.

We sent out our first batch of PC invitation on January 18 (see
[/mailers/sendinvites.py](/mailers/sendinvites.py) for the script we
used to send out PC invitations).  Responses were collected using a
Google form, which was simple and worked well for us.  Based on the
responses to these, we sent out second and third batches of
invitations. The PC was finalized by early April, in advance of the
CFP release on April 19 (which was set as that target to be one month
ahead of the submission deadline).

The biggest challenge in forming a PC for a complex conference like
CCS is ensuring there are enough qualified PC members in the right
areas to review the submissions. This is especially difficult in
cryptography &mdash; more specialized expertise is needed to review
papers in many areas of cryptography, and our invitation acceptance
rate was significantly lower for cryptographers than it was for
systems security researchers. So, its important to pay attention to
the make-up of the committee as the first round of invitations come
back and to make adjustments in subsequent invitations.

The acceptance rate for PC invitations was very high, and only a few
people were non-responsive. Nearly all of the declines were gracious
and offered good excuses for not wanting to take on the responsibility
and workload of being on the PC. Overall, 71% of invitations were
accepted (142 out of 198).  

**Note:** I can share the google sheet we used to model PC load and
  keep track of PC candidates with individual PC chairs on request,
  but don't want to make this public since it includes non-public
  information such as people that we ended up not inviting to the PC,
  or who declined invitations.

# <a name="reviewing"></a>Reviewing Schedule

Here's the schedule we followed for CCS 2017: (public dates are
**bolded**, others are internal dates)

**April 19:** Call for Papers Posted  
**April 22:** Submission server ready to accept submissions

**May 19:** Paper submission deadline  
May 21: Round 1 Reviewing starts (after PC chairs make first pass on papers to remove invalid submissions, reviewing assignments)  
**June 16:** Deadline for first round of reviews  
**June 16-July 6:** On-line discussions, second reviewing round  
**July 6:** Deadline for second round of reviews  
**July 7-10:** Author response period  
**July 11-24:** On-line discussions, third reviewing round  
**July 24:** Deadline for third round of reviews, responses to author rebuttals  
July 26: Request final external reviews  
**July 24-August 1:** Final on-line discussions  
**August 2:** Author notification  
**September 1:** Camera-ready final paper deadline

This was determined in January, and included in the PC member
invitations, since we thought it was important to make the schedule
clear to PC members before they accept the invitation.  The main
constraints on the schedule are based on the strange demands of the
publisher to have the camera-ready deadline be more than 8 weeks
before the conference. We negotiated as much as we could to reduce
this time period, but couldn't move the camera-ready deadline later
than September 1, and thought we needed a month (less a day) between
author notification and camera-ready deadline. This didn't leave
enough time for active shepherding, but we thought having more time
for the review process was more important. I have heard rumors that
ACM is finally reconsidering its publishing contract, so perhaps there
will be a more sensible schedule possible in future years where the
camera-ready deadline and author notification can both move back
several weeks.

The paper submission deadline, author response period, author
notification, and camera-ready dates were made public in the CFP
and we viewed those as firm committments to authors.

# <a name="cfp"></a>Call for Papers

To create the CFP, we started with last year's CFP and put this into a
Google doc. We made some edits based on discussions among the
co-chairs and feedback from last year's conference, and requested
comments from the PC.  

Unlike the PC membership, for the CFP, it is recommended to preserve
continuity in the conference by starting with the previous year's CFP,
and only making changes with justification.

The biggest changes we made for the CFP were:

1. Adding a paragraph about making allowances for authors who are
unable to travel to the US because of travel restrictions that had
been put in place after the location of the conference was
determined. Although we had strong personal feelings about how
horrendous US immigration has become, we tried to word the paragraph
in a politically-neutral way but to make it clear that the conference
would not discriminate against authors whose nationality may make it
infeasible for them to travel to the conference. (Unfortunately, this
was the case for several presenters of accepted papers.) This
paragraph should not be necessary for CCS 2018 to be held in Toronto,
Canada, and in general, CFPs have included a paragraph requiring one
author from each accepted paper come to the conference to present the
paper.

2. Adding a paragraph about holding Practice Sessions before the
conference. There was a lot of discussion about this, and based on
this, the wording was changed to make it clear these would be
voluntary. Organizing the practice sessions and finding Session Chairs
willing to host practice sessions was difficult, but I believe about
half the sessions did this and all who did found it to be worthwhile,
and the others at least benefited from having email introductions
before the conference.

3. Changing the paper format requirements to increase the length to be
more in-line with other top-tier security conferences (we settled on
12 pages of body content, with any number of additional pages for
bibliography and appendices).  We included text in the CFP to attempt
to discourage authors from abusing appendices to avoid the spirit of
the page limit, which we see as increasingly common in our
community. We did not enforce this in draconian ways, but did redact
appendices that we considered improper in submissions by editing the
submitted PDFs.  The question of what is and is not considered valid
material to include in an appendix is not that clear, however, and I'm
not sure if there is a good way to describe it that would be
interpreted consistently.

### Reviewing Form

We didn't spend a lot of time thinking about the reviewing form before
reviewing started, and after that it was too late to change it.  The
biggest mistake we made was not including separate ratings for
"Reviewer Confidence" and "Reviewer Expertise" (instead, we just had
"Reviewer Expertise", which is much less useful). 

It would also be good to consider having an explicit part of the
review form be "questions for authors" (to make it abundantly clear
what the reviewers would like authors to respond to in the response
period) and perhaps to have a "Comments on Authors' Response" section
(which we just made a separate section of the review text). We were
vigilant (with the help for the Discussion Committee) in ensuring that
reviewers did provide responses to author responses, but it was harder
than it could have been since it was necessary to find these marked in
the original reviews.

# <a name="posting"></a>Posting Papers

Within a day or two of sending out the paper decisions, the list of
accepted papers should be posted on the web.  Depending on how much
control you have over the main CCS web server, it might work to use
that for this, but we found it was not an acceptable option for us and
set up a github pages site
([https://acmccs.github.io/](https://acmccs.github.io/)) for
this. Having a site you can generate programmatically and control
makes things a lot easier and more managable then needing to go
through the web chairs for each update.

You can download CSV files from hotcrp with all the paper information,
but some hand editing is necessary to make affiliations consistent,
fix mispelled names (yes, many people mispell their own names in their
submissions), and deal with accented letters in names and strange
symbols in paper titles.  

The scripts provided in [/web](/web) generate the website with pages
for [Papers](https://acmccs.github.io/papers/),
[Authors](https://acmccs.github.io/authors/),
[Institutions](https://acmccs.github.io/institutions/), and
[Topics](https://acmccs.github.io/topics/) (these are based on the
user-selected topics in the submissions, so its worth thinking about
the list of topics when creating the submission page with both
reviewing and organization in mind).  Once the Sessions were
determined, we also generated pages for each
[Session](https://acmccs.github.io/fullsessions/), and for the [Award
Finalists](https://acmccs.github.io/finalists/). If you update the CSV
files with the appropriate information, it is easy to generate all of
these with just one `make github` command with the provided scripts.

To use the web scripts, you need to have [Hugo](https://gohugo.io/)
installed, and set up a github pages site for hosting the generated
html (or something else, but the provided scripts work with github
pages).

# <a name="awards"></a>Paper Awards

Determining winners for awards is an important responsibility of the
PC chairs, and its important that this is done with a fair,
substantive, and meaningful processs.  

As the number of papers in our top conferences has increased, awards
are becoming more and more important to people's careers, but many
conferences still treat the award selection process as an afterthought
and end up deciding awards in fairly arbitrary ways.

### Form a paper awards committee

This should be about 8 PC members, including the PC chairs (one of
whom should be the Awards Committee Chair). It is best to ask specific
people you think would be valuable to have on this committee, ensuring
a good mix of the community, and letting them know in advance that it
will have a considerable workload.

### Select the award finalists 

We selected a handful of top-ranked papers at automatic aware
nominees, and any PC member was allowed to nominate any paper they
considered award worthy.  We ended up with 22 papers nominated.

For this group, the Awards Committee voted to select a group of Best
Paper Finalists. For this first voting stage, which took about 2
weeks, committee members were not expect to have read all the papers,
but could vote that they thought a paper was award worthy, did not
think a paper should be considered for an award, or that they were not
familiar enough with the paper to have an opinion (or that they were
conflicted on the paper).

Based on these votes, we (the PC chairs) selected a set of finalist
papers. In general, papers that had more positive support than
negative support were selected as finalists.  We did not have a
specific target number of finalists, but ended up with 11 papers
designated as award finalists. 

The finalists were made public, and recognized in the CCS program
before the conference.

### Selecting the Awardees

For the final stage in the process, each member of the Paper Awards
Committee had two weeks to consider the finalist papers, and everyone
was expected to review the final (camera-ready) versions of all of the
finalist papers. 

We set up a separate hotcrp server with just the finalist papers in it
to make the final versions available to the committee and provide a
system for reviewing separate from the original reviewing system. We
didn't expect BPAC members to write detailed reviews for the papers at
this stage (especially given they would not go back to the authors),
but did get both review scores and text comments, and had some
additional discussion.

This led to selecting 5 Best Paper Awards and 2 Real-World Impact
Awards.  (The _Read-World Impact Award_ was a new award we created for
CCS 2017, with approval of the SIGSAC chairs.) 

### Presenting the Awards

The Best Paper Awards are presented at the CCS Banquet the second
evening of the main conference. We made up a PowerPoint loop to show
all the Finalists during the banquet, and then a separate PowerPoint
deck for presenting the awards. It is worthwhile rehearse among the PC
chairs how you will present the awards and trying to figure out how to
pronounce winners names before the award presentation.

# <a name="tot"></a>Test-of-Time Award

One of the other responsibilities and privlidges of the CCS PC chairs
is to present the CCS Test-of-Time Award to recognizes papers from CCS
ten years prior that have had the greatest impact on security research
and practice over the past decade. 

This can and should be done early, and around the other main time
committments you have for the conference.  There was no established
process for how to do this conveyed to us, so this is what we did.

We formed a separate committee for the Test-of-Time Award, and did not
limit membership to PC members. We included the PC Chairs from CCS
2007 on the committee (and one of us as chair of this committee), as
well as the PC Chairs (excluding on PC chair who was conflicted with
one of the potential CCS 2007 papers under consideration), and invited
two additional PC members (for six total committee members).

We didn't want the award to be primarily based on citation counts, but
did consider that having a reasonbly high number of citations is one
way to see impact of papers. So, the process started by collecting
citation stats on all the CCS 2007 papers from google scholar (this
was managable to do manually for the 55 papers in CCS 2007 &mdash; I
think it would be hard to automate this, since its important to look
for subsequent journal versions of some papers and consider all the
citations). Based on the citation counts, there were 5 papers clearly
worth considering, and in dicussions with the T-o-T Committee, one
additional paper was considered.

After this, we followed a voting-discussion process similar to the one
described for the Best Paper Awards above, to select the winner.  (We
settled on just one paper, although in previous years there had been
multiple awards.)

We informed the winner early enough for them to be able to make travel
arrangements to attend CCS (and in our case, it was also a great
opportunity for the winner to be an honorary session chair on a
session of papers that was inspired by the winning paper).

The Test-of-Time Award was presented at the CCS Banquet after the Best
Paper Awards, and it is good to make a brief statement about the
significance of the paper and why it was selected for the award.



