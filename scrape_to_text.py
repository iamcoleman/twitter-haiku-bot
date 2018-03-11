"""
This .py creates a [json] file that is filled with the comments
of the top 15 hottest reddit posts in /r/AskReddit
"""

import praw
import json

def scrape_to_text():
	print("Scraping text from the comments of top five posts in AskReddit from the last month...")
	LW = praw.Reddit(client_id = 'HNM-hl4Uke56mQ',
					 client_secret = 'oUPkogZifvqrrcVcFLZy1_h9oh4',
	    	         username = 'LordWoodhouse',
	        	     password = 'pythonfinal',
	            	 user_agent = 'v1')

	subreddit = LW.subreddit('AskReddit')
	hot_python = subreddit.top(time_filter='month', limit=15)

	"""
	To get all the object things...
	print(dir(sumbission))
	"""

	i = 1
	for submission in hot_python:
		if not submission.stickied:
			print('\nPost',i,'\nTitle: {} \nUps: {} \nDowns: {} \nVisited: {}'.format(submission.title, 
																					  submission.ups, 
																					  submission.downs, 
																					  submission.visited))
			i += 1
		
			submission.comments.replace_more(limit=0)
			for comment in submission.comments.list():
				f = open("comments.json",'ab')
				f.write(comment.body.encode())
				f.close()

	print("Scraping Complete!")
