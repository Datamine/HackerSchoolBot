# John Loeber | Python 2.7.6 | Nov-5-2014 | Debian x86_64 | www.johnloeber.com

from twitterapi import api
from ast import literal_eval
from time import sleep

# inefficient approach, as memory-efficiency is not so important for this.
def update(tweetid):
    with open("tweetids","a") as f:
        f.write(str(tweetid)+'\n')
    return

def main():
    with open("hackerschoolers2","r") as f:
        hsers = [x.rstrip('\n') for x in f.readlines()]
    with open("tweetids","r") as g:
        tweetids = [x.rstrip('\n') for x in g.readlines()]
    while True:
        tweets = api.GetMentions(count=800)
        tweets = filter(lambda y: y.GetUser.screen_name in hackerschoolers2,tweets)
        tweets = filter(lambda z: z.id not in tweetids,tweets)
        for j in tweets:
            if len(j.text)>20:
                try:
                    api.PostRetweet(j.id)
                except:
                    print "error 1"
            else:
                name = j.GetUser().screen_name
                t2 = api.GetUserTimeline(screen_name=name,count=50)
                try:
                    api.PostRetweet(t2[t2.index(j)+1].id)
                except:
                    print "error 2"
            update(j.id)
        sleep(120)

if __name__=='__main__':
    main()
