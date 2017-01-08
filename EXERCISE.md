l
COMPOSE
Labels
Inbox (66)
Starred
Important
Sent Mail
Drafts (45)
Circles
STA/ Work
UT (279)
More 
Hangouts

 
 
 
  More 
4 of 1,040  
 
Print all In new window
Braintree Coding Problem for Software Engineer
Inbox
x 

Rebecca Tobin
AttachmentsJan 4 (3 days ago)

to me, molly.orloff 
Greetings!

 

Thanks again for your time today. I have attached a coding problem that will help us get a better sense of your skills. We are interested not only in your solution to the stated problem, but also in your process and style, so please include whatever you like to indicate that to us. 

Implement your solution in any programming language you wish, ideally one with which you are familiar.

Please write automated tests and include them with your submission, along with a README that includes usage instructions, an overview of your design decisions, and why you picked the programming language you used for the solution.

You may be asked to update or extend your solution, so please make sure to use tools and a language you would be comfortable using in an interview. We ask that you return it to us within one week. 

Please confirm that you received this email and when you're finished zip it up and email it back to me. We ask that you please not post the challenge or your solution anywhere online - even in a private space. Let me know if you have any questions. We look forward to seeing your code and good luck! 

Thanks!


Attachments area
	
Click here to Reply, Reply to all, or Forward
6.59 GB (0%) of 1,039 GB used
Manage
Terms - Privacy
Last account activity: 34 minutes ago
Details
Rebecca Tobin

rebecca.tobin@getbraintree.com
San Francisco Bay Area
Talent Acquisition at Braintree
Technical/University Recruiter at Braintree/Venmo
LinkedInCONNECT
Rebecca is in your third-degree network. You may know them through:
Megan Weddle (LION) on LinkedIn
Sameer Saproo on LinkedIn
Stefanie Lemcke on LinkedIn
Amos Schwartzfarb on LinkedIn
Joe Yoo on LinkedIn

support | privacy | my profile	rapportive
People (2)
Rebecca Tobin
Add to circles

Show details


# Basic Credit Card Processing
-----

Imagine that you're writing software for a credit card provider.  Implement a
program that will add new credit card accounts, process charges and credits
against them, and display summary information.

## Requirements:

- Your program must accept input from two sources: a filename passed in
  command line arguments and STDIN. For example, on Linux or OSX both
  './myprogram input.txt' and './myprogram < input.txt' should work.
- Your program must accept three input commands passed with space delimited
  arguments.
- "Add" will create a new credit card for a given name, card number, and limit
   - Card numbers should be validated using Luhn 10
   - New cards start with a $0 balance
- "Charge" will increase the balance of the card associated with the provided
  name by the amount specified
   - Charges that would raise the balance over the limit are ignored as if they
     were declined
   - Charges against Luhn 10 invalid cards are ignored
- "Credit" will decrease the balance of the card associated with the provided
  name by the amount specified
   - Credits that would drop the balance below $0 will create a negative balance
   - Credits against Luhn 10 invalid cards are ignored
- When all input has been read and processed, a summary should be generated and
  written to STDOUT.
- The summary should include the name of each person followed by a colon and
  balance
- The names should be displayed alphabetically
- Display "error" instead of the balance if the credit card number does not pass
  Luhn 10

## Input Assumptions:

- All input will be valid -- there's no need to check for illegal characters
  or malformed commands.
- All input will be space delimited
- Credit card numbers may vary in length up to 19 characters
- Credit card numbers will always be numeric
- Amounts will always be prefixed with "$" and will be in whole dollars (no
  decimals)

## Example Input:

```
Add Tom 4111111111111111 $1000
Add Lisa 5454545454545454 $3000
Add Quincy 1234567890123456 $2000
Charge Tom $500
Charge Tom $800
Charge Lisa $7
Credit Lisa $100
Credit Quincy $200
```

## Example Output:

```
Lisa: $-93
Quincy: error
Tom: $500
```

Implement your solution in any programming language you wish, but keep in mind
we may ask you to explain or extend your code.  Please write automated tests
and include them with your submission.

In addition to your code and tests, please also include a README that explains:

- An overview of your design decisions
- Why you picked the programming language you used
- How to run your code and tests, including how to install any dependencies
  your code may have.

Thank you!

**Note: this information is confidential. It is prohibited to share, post online
or otherwise publicize without Braintree's prior written consent.**
