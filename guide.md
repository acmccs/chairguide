# CCS PC Chair's Guide

The main tasks for the PC Chair are:

- (November-March) [Forming the PC](#forming)
- (March-April) Writing the [Call for Papers]
- (March-May) Preparing for the review process
- (mid-May) Paper submission deadline)
- (May-August) Managing the review process
- (July-September) Test-of-Time Award
- (August) Posting the accepted papers
- (August-September) Planning the sessions
- (August-September) Selecting the Awards, Program Chair's Welcome
- (October-November) Conference
- (November-January) Post-Conference

# Forming the Program Committee

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

# Reviewing Schedule

Here's the schedule we followed for CCS 2017:

**April 19:** Call for Papers Posted  
**April 22:** Submission server ready to accept submissions

**May 19:** Paper submission deadline  
**June 16:** Deadline for first round of reviews  
**June 16-July 6:** On-line discussions, second reviewing round  
**July 6:** Deadline for second round of reviews  
**July 7-10:** Author response period  
**July 11-24:** On-line discussions, third reviewing round  
**July 24:** Deadline for third round of reviews, responses to author rebuttals  
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

# Call for Papers

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
reviewing started, and after that it was too late to change it. 



# Awards

Determining winners for awards is an important responsibility of the
PC chairs, and its important that this is done with a fair,
substantive, and meaningful processs.  

As the number of papers in our top conferences has increased, awards
are becoming more and more important to people's careers, but many
conferences still treat the award selection process as an afterthought
and end up deciding awards in fairly arbitrary ways.



### Form a paper awards committee

### Select the award nominees 

**Make the list of nominated papers public** before the conference,
  providing a meaningful recognition.


