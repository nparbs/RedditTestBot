#!/usr/bin/python
#NICK PARBS REDDIT TEST BOT V1
import praw
import os
import re
import time
import config



def bot_login():
	reddit = praw.Reddit(username = config.username,
				password = config.password,
				client_id = config.client_id,
				client_secret= config.client_secret,
				user_agent = config.username + " python bot V1 by /u/nparbs")
					
	return reddit

def run_bot(reddit):	
	# Have we run this code before?
	if not os.path.isfile("posts_replied_to.txt"):
		posts_replied_to = []

	# Load the list of posts we have replied to
	else:
		# Read the file into a list and remove any empty values
		with open("posts_replied_to.txt", "r") as f:
			posts_replied_to = f.read()
			posts_replied_to = posts_replied_to.split("\n")
			posts_replied_to = list(filter(None, posts_replied_to))

	# Get values from our subreddit
	subreddit = reddit.subreddit('ParbsBotTest')
	for submission in subreddit.hot(limit=10):
		#if submission.title
		#print("Title: ", submission.title)
		#print("Text: ", submission.selftext)
		#print("Score: ", submission.score)
		#print("---------------------------------\n")

		# If we haven't replied to this post before
		if submission.id not in posts_replied_to:

			# Do a case insensitive search
			if re.search("SEARCH", submission.title, re.IGNORECASE):
				# Reply to the post
				submission.reply("REPLY")
				print("Bot replying to : ", submission.title)

				# Store the current id into our list
				posts_replied_to.append(submission.id)

	# Write our updated list back to the file
	with open("posts_replied_to.txt", "w") as f:
		for post_id in posts_replied_to:
			f.write(post_id + "\n")
	
reddit = bot_login()

while True:
	run_bot(reddit)
	time.sleep(1)
