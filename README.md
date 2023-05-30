# PSF Election Repository

This repository contains the tools and documentation for the way the Python
Software Foundation (the PSF) Elections are presently operated. This document
will cover the tools in the repository and the processes that the Election
Administrator is responsible for.


## A New Election

At least once a year, the PSF runs an election. We (at the time of this
writing) use [OpaVote][1]. Election administrators should log into
OpaVote using one of the options on the front page.

It is best to set your account profile timezone to `UTC` in order to ensure
that the start/stop dates configured for elections are correct to your
expectations.

Once signed into OpaVote, locate the button labeled `(+) Create Election`.
Click it, and then the administrator will be prompted for the following
information:

### Election Info

- "Title" - the display title, e.g., `Python Software Foundation Board of
  Directors Election 2023`

- "Description" - in the past, administrators used this to explain Approval
  voting and the importance of the election

    >    List of candidates: https://www.python.org/nominations/elections/2023-python-software-foundation-board/nominees/
    >
    >    This election uses Approval Voting.
         That is to say that you may Approve as many candidates
         or bylaws changes as you wish.
         You may choose to vote for 1, 2, 3, ..., N-1, N, or all N of the candidates.
         The top M vote-getters will be elected to the board,
         after all conflict-of-interest, affiliations, and co-affiliation sections
         of the PSF Bylaws have been satisfied.
    >
    >    The candidates have all been nominated on python.org https://www.python.org/nominations/elections/
    >
    >    Please carefully read the detailed candidate statements
         linked after each candidate's name.
         There is a wealth of talent, dedication, diversity, and integrity
         among these candidates.
    >
    >    It is your responsibility as
         a voting member of the Python Software Foundation
         to consider each of these statements.
         The order that the names appear on this ballot has been randomized
         and it will not match the order on the nomination page
         which is also randomized.
    >
    >   **Note**: Once you have cast your ballot you **WILL NOT**
        be able to modify it. Please consider the nominations carefully
        and cast your ballot once you have come to a decision.

- "Email text" - Include basic information on the vote, where to find more
  information, and a notice regarding the end of voting.

    >   The 2023 election for the Board of Directors
        of the Python Software Foundation is open.
        The full list of candidates is available at
        https://python.org/nominations/elections/2023-python-software-foundation-board/nominees.
    >
    >   Voting will close Friday, June 30, 2023 at 11:59 pm UTC as previously announced.
        See https://www.python.org/nominations/elections/2023-python-software-foundation-board/nominees/
        for details on the election as well as helpful countdown clocks.
    >
    >   **Note**: Once you have cast your ballot you **WILL NOT**
        be able to modify it. Please consider the nominations carefully
        and cast your ballot once you have come to a decision.

- "Language" - `English`

- "Expert mode" - You MUST enable expert mode! Which will reveal all options
  following this bullet.

- "Show results during voting" - "no"

- "Voting start date" - Optionally this to the date that voting will start.
  This will automatically send ballots at 12:01 AM that day
  (In the timezone specified in your account profile).

- "Voting stop date" - Optionally this to the date that voting will end.
  This will automatically close the election at 11:59 PM that day
  (In the timezone specified in your account profile).

- "Automatic reminders" - "yes"

- "Anonymous voting" - "yes"

- "Candidate names" - Add the names of candidates as they appear on the
  nomination statements, one-per-line.

- "Method" - "Approval Voting"

- "Number of winners" - Per [Bylaws Section 5.5][2], 3 or 4 depending on
  the outgoing cohort size for a given year. It *may* be more if any
  additional board vacancies have been created.

- "Shuffle candidate order": "yes"

- There *may* be additional questions such as bylaws changes, if so
  use the `(+) Add Another Contest` button and use judgement to determine
  how to add them.

### Setting up Voters

The Election Adminitsrator (EA) will receive a file with the first name, last
name, membership type, and email address of a voter.
In order to add voters to an election,
OpaVote requires they be uploaded in an ASCII text file in the format::

    email-address

For example::

    graffatcolmingov@gmail.com
    ewdurbin@pyfound.org

The format of the file the election administrator typically gets is of the
format::

    FirstName,LastName,MembershipType,Email

There is a tool in this repository to handle it called
``convert-exported-csv-for-opavote.py``. This will generate the necessary
format for OpaVote from the CSV file the EA receives.

It's important to note here that not all voters have a first or last name and
some don't have either.


## Running an Election

Running an election begins once the election starts. While an election is in
progress, a few things may happen:

- New voters may need to be added as they were missed when the original voter
  list was generated

- Some voters may need you to send/re-send their ballot notification email

The following sub-sections will cover these in detail.

### Adding Missed Voters

OpaVote allows us to add new voters after an election has begun although
the other details of the election or questions cannot be altered. The process for
adding new voters is the same as is detailed above in "Setting up Voters". The
EA will receive a new file full of the details of the voters who were missed.
Using that, the EA can generate a new CSV to upload to OpaVote using the same
tooling.

### Re-sending Ballot Emails

OpaVote provides statistics on pending, in-transit, rejected, and delivered
ballot emails. It also tracks opens, clicks, and visits.

If a reminder is necessary, it can be sent from the admin console by finding
the voter and clicking "Send Ballot".

If "Automatic reminders" was not selected during election setup,
OpaVote will automatically send reminders every three days throughout
the election period.

## Closing an Election

The end of an election requires the EA to verify the results of the election
with Helios and then present the results to the Executive Director of the PSF.
The Executive Director will then announce the results to the community.
At that time, the `🌎 Publish Results` button on OpaVote can be used to
publish the full results to all voters.

### Achieving Quorum

The PSF Bylaws_ state that one-third (1/3) of the members elligible to vote
will constitute a quorum. See also:

.. epigraph::

    Except as otherwise required by law, by the Certificate of Incorporation
    or by these Bylaws, one-third (1/3) of the members entitled to vote (the
    voting members), represented in person or represented by proxy, shall
    constitute a quorum at a meeting of members.

    For electronic votes, a quorum shall be reached as soon as one-third (1/3)
    of the members entitled to vote (the voting members) have cast their vote.
    If the voting period ends before a quorum is reached, the vote is declared
    void.

    -- Python Software Foundation Bylaws, Section 3.9. Member Quorum

For example, if there are 999 voters in an election, there must be 333 votes
cast at least in order to declare quorum.

### In the Event of a Tie

In the case of a Board of Directors Election, the top ``N`` candidates are
accepted based on the number of open seats in that Election. If there is a tie
for the ``Nth`` seat, then there is a script that may be used to break the tie
called ``break-ties.py`` (cleverly named, eh?).

Let's say that there is a 4 way tie between "Candidate 0", "Candidate 3",
"Candidate 8", and "Candidate 12" and we need 2 more people to round out the
total, then we would do::

    python3 break-ties.py -n 2 \
        -c "Candidate 0" \
        -c "Candidate 3" \
        -c "Candidate 8" \
        -c "Candidate 12"

And it would print the winning candidates. Re-running this script will always
result in the same candidates winning the tie breaker. This is by design so
that the tie breaker results may be verified by someone other than the EA.


[1]: https://www.opavote.com
[2]: https://www.python.org/psf/bylaws/
