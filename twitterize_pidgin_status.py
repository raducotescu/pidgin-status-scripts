#!/usr/bin/python                               
# twitterize_pidgin_status.py                                               
"""                                                                     
 Handy script for changing Pidgin's status with the last tweet from your Twitter
 account feed.
 Usage:                                                                               
 	python twitterize_pidgin_status.py your_twitter_status_feed_link                                

 For further details visit:
 	http://radu.cotescu.com/?p=1079
 Authors:
 	Radu Cotescu,   http://radu.cotescu.com
"""

import commands
import feedparser
import os
import sys
import time

# feed url
FEED = []

def setFeed():
	if sys.argv is not None and len( sys.argv ) < 3:
		global FEED
		FEED = sys.argv[1]

def changeStatus():
	if len( FEED ) is not None:
		if commands.getoutput('pidof pidgin') != '':
			feed = feedparser.parse( FEED )
			print time.strftime('%d-%m-%Y, %H:%M:%S', time.localtime())
			for i in range(0, len(feed['items'])):
				content = feed['items'][i].title.encode('utf-8')
				link = feed['items'][i].link.encode('utf-8')
				startPos = content.find(":") + 2 
				utilMsg = content[startPos : len(content)]
				if not utilMsg.startswith('@'):
					tweet = ''.join(utilMsg.split('#'))
					tweet = tweet.replace('&', 'and')
					tweet = tweet.replace('"', '');
					print """\tStatus:\n\t%s""" % tweet
					status = 'purple-remote "setstatus?status=available&message=%s"' % tweet
					os.system(status)
					break

setFeed()
changeStatus()

# EOF

