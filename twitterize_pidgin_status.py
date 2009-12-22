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

 LICENSE:
 Copyright (c) 2009 Radu Cotescu

 Permission is hereby granted, free of charge, to any person
 obtaining a copy of this software and associated documentation
 files (the "Software"), to deal in the Software without
 restriction, including without limitation the rights to use,
 copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the
 Software is furnished to do so, subject to the following
 conditions:

 The above copyright notice and this permission notice shall be
 included in all copies or substantial portions of the Software.

 Except as contained in this notice, the name(s) of the above
 copyright holders shall not be used in advertising or otherwise
 to promote the sale, use or other dealings in this Software
 without prior written authorization.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
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
					print status
					os.system(status)
					break

setFeed()
changeStatus()

# EOF

