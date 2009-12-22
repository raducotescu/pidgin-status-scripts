#!/usr/bin/python                               
# pidgin_status_change.py                                               
"""                                                                     
Handy script for changing Pidgin's status with a post from a feed passed as argument.
Usage:                                                                               
        python pidgin_status_change.py your_feed_link                                

For further details visit:
        http://radu.cotescu.com/2009/08/26/python-and-pidgin-status-on-ubuntu-linux/

Authors:
        Tudor Barbu,    http://motane.lu
        Radu Cotescu,   http://radu.cotescu.com
"""

import commands
import feedparser
import random
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
                        index = random.randint( 0, len( feed['items'] ) - 1 )
                        print time.strftime("%d-%m-%Y, %H:%M:%S", time.localtime())
                        print """\tStatus:\n\t%s\n\t%s""" % ( feed['items'][index].title.encode("utf-8"), feed['items'][index].link.encode("utf-8") )
                        status = 'purple-remote "setstatus?status=available&message=%s %s"' % ( feed['items'][index].title, feed['items'][index].link )
                        os.system(status.encode("utf-8"))

setFeed()
changeStatus()

# EOF

