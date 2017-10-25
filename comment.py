import praw
import sys
import requests

reddit = praw.Reddit("comment_searcher")
user= reddit.redditor("%s" % sys.argv[1])
subreddit = sys.argv[2]
print("User: " + user.name + "  Subreddit: " + subreddit)
for comment in user.comments.top(limit=None):
    if comment.is_submitter and (comment.subreddit == subreddit):
        print('* ', end="")
        print(comment.body + '\n')
    elif comment.subreddit == subreddit:
        print (comment.body +  '\n')

    


