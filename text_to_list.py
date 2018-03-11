"""
This .py turns the [json] file from 'scrape_to_text.py' into
a list of useable comments
"""

def text_to_list():
	print("\nTurning [json] to a list of comments...")
	with open("comments.json", encoding="utf8") as f:
		for line in f:
			content = f.readlines()
	content = [x.strip() for x in content]
	goodComments = []
	i = 0
	while i < len(content):
		# Change [600] to get longer/shorter comments
		if len(content[i]) > 600:
			goodComments.append(content[i])
		i = i + 1
	print("List Complete!")
	return goodComments