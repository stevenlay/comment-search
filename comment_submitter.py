import praw
import sys
import requests


reddit = praw.Reddit("comment_searcher")

#User:_____     Subreddit:_____
user= reddit.redditor("%s" % sys.argv[1])


print("User: " + user.name + '\n')
for comment in user.comments.top(limit=None):
        if comment.is_submitter:
            print('* ', end="")
            print(comment.submission.title)
            print(comment.submission.shortlink)
            print("------------------------------- \n")