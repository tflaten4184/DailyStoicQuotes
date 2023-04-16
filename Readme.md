# Purpose

This project is for automatically sending a daily email reminder for the corresponding chapter of The Daily Stoic for a given day. I used Python to parse a PDF and reformat it to use it as a source for the daily quotes.

All credit for the book itself goes to the original authors; Ryan Holiday and Stephen Hanselman. I've omitted the book's text from this repo due to copyright reasons. However, this code can still be useful for similar use-cases.

https://en.wikipedia.org/wiki/The_Daily_Stoic

# Setup instructions

The script `mailer.py` requires some additional info in order to run:
* API key for the gmail account you'd like to use. Follow Google's documentation to set this up for your account so that Python can send emails using it. Store this as a virtual environment variable (.env), along with the email address you wish to send from. The file .env should look like this, with the appropriate values substituted for each value:
```
apikey=...
# Email from which scheduled messages will be sent
botEmail=...
# Email of person with access to subscriber list.
maintainerEmail=...
```
* List of subscribers (email addresses), subscribersList.txt. Each email address must be on it's own line.
* Text file ProdSource.txt containing the text from the book. (Omitted here due to copyright)

Once that has been setup, you can schedule the script to run daily at your preferred time using your OS scheduling tool. For Windows, use Task Scheduler.

Currently the subscriber list must be edited manually to add/remove subscribers. It's important to only add people to this list if they've agreed, since the only way to unsubscribe is for the developer to manually edit the text file.