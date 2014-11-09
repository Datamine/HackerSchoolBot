# John Loeber | Python 2.7.6 | Nov-5-2014 | Debian x86_64 | www.johnloeber.com

from twitterapi import api
import time
from ast import literal_eval

def main():
    with open("hackerschoolers2","r") as f:
        hsers = map(rstrip('\n'), f.readlines())
    with open("hstimestamps","r+") as g:

    while True:
        for i in hsers:
                # This is an inefficient way of maintaining a store of latest
                # ids, but all other ways each only had one of (a) practicality,
                # (b) data sanity in case of crashes, (c) efficiency.
                # As the file in question is small, I'm going for an
                # inefficient approach, as it's not so important.
                
                tweets = api.GetUserTimeline(screen_name=i,include_rts=False,
                                exclude_replies=False,since_id=getsinceid(i,g))
                for j in tweets:
                     

        sleep(120)

if __name__=='__main__':
    main()
