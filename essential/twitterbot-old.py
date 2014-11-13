# John Loeber | Python 2.7.6 | Nov-5-2014 | Debian x86_64 | www.johnloeber.com

from twitterapi import api
from ast import literal_eval
from time import sleep

# "hstimestamps" is an inefficient way of maintaining a store of latest
# ids, but all other ways each only had one of (a) practicality,
# (b) data sanity in case of crashes, (c) efficiency.
# As the file in question is small, I'm going for an
# inefficient approach, as efficiency is not so important.

def update(user,tweetid):
    # Not using r+ because of problems w/r/t/ overwriting due to diff. lengths
    with open("hstimestamps","r") as g:
        tdict = literal_eval(g.read().rstrip('\n'))
    tdict[user] = tweetid
    with open("hstimestamps","w") as h:
        h.write(str(tdict))
    return

def getsinceid(i):
    with open("hstimestamps","r") as l:
        d = literal_eval(l.read().rstrip('\n'))
    return d[i]

def main():
    with open("hackerschoolers2","r") as f:
        hsers = [x.rstrip('\n') for x in f.readlines()]
    while True:
        tweets = api.GetMentions(count=800)
        tweets = filter(lambda y: y.GetUser.screen_name in hackerschoolers2,tweets)
        for i in hsers:
            try:
                tweets = api.GetUserTimeline(screen_name=i,include_rts=False, exclude_replies=False,since_id=getsinceid(i))
            except:
                continue
            if tweets:
                for j in tweets:
                    for k in j.user_mentions:
                        if "hsalums" in str(k) and len(j.text)>20:
                            try:
                                api.PostRetweet(j.id)
                            except:
                                print "error 1"
                        elif "hsalums" in str(k):
                            # Inelegant, but it's the best way to retrieve
                            # the desired tweet while catching edge cases
                            t2 = api.GetUserTimeline(screen_name=i,since_id=j.id)
                            # +10 to ensure against count omission
                            t3 = api.GetUserTimeline(screen_name=i,include_rts=False,count = len(t2)+10)
                            try:
                                api.PostRetweet(t3[t3.index(j)+1].id)
                            except:
                                print "error 2"
                update(i,tweets[0].id)
        sleep(120)

if __name__=='__main__':
    main()
