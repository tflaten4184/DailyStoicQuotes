# Purpose

This project is for automatically sending a daily email reminder for the corresponding chapter of The Daily Stoic for a given day.
All credit goes to the original authors; Ryan Holiday and Stephen Hanselman.

https://en.wikipedia.org/wiki/The_Daily_Stoic

# Setup instructions

The script `mailer.py` requires some additional info in order to run:
* API key for the gmail account you'd like to use. Follow Google's documentation to set this up for your account so that Python can send emails using it.
* List of subscribers (email addresses), subscribersList.txt. Each email address must be on it's own line.

Once that has been setup, you can schedule the script to run daily at your preferred time using your OS scheduling tool. For Windows, use Task Scheduler.

Currently the subscriber list must be edited manually to add/remove subscribers. It's important to only add people to this list if they've agreed, since the only way to unsubscribe is for the developer to manually edit the text file.