"""
Tie all this stuff together
"""
import scrape_to_text
import text_to_list
import haiku
from random import randint

def HaiHaus():
	# Scrape Reddit
	scrape_to_text.scrape_to_text()

	# Compile the list of comments
	goodComments = text_to_list.text_to_list()

	# Make a list of [15] haikus
	haikus = []
	i = 0
	while i < 45:
		n = randint(0, len(goodComments))
		boy = haiku.Haiku(goodComments[n])
		boy.generateHaiku()
		ting = boy.getHaikuList()
		haikus.append(ting)
		i += 1

	# Return a list of [15] haikus
	return haikus