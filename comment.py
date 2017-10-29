import praw
import sys
import requests


reddit = praw.Reddit("comment_searcher")

#User:_____     Subreddit:_____
user= reddit.redditor("%s" % sys.argv[1])
subreddit = sys.argv[2]

print("User: " + user.name + "  Subreddit: " + subreddit)
for comment in user.comments.top(limit=None):
    if comment.subreddit == subreddit:
        if comment.is_submitter:
           print('* ', end="")
        print(comment.body + '\n')

    


