import praw
import sys
import requests


reddit = praw.Reddit("comment_searcher")

#User:_____     Subreddit:_____
user= reddit.redditor("%s" % sys.argv[1])
subreddit = sys.argv[2]

print("User: " + user.name + "  Subreddit: " + subreddit + '\n')
for comment in user.comments.top(limit=None):
    if comment.subreddit == subreddit:
        if comment.is_submitter:
           print('* ', end="")
        else:
            print(comment.submission.title + "  by: ", end="")
            if(comment.submission.author is None):
                print("[deleted] \n")
            else:
                print(comment.submission.author.name + '\n')
        print(user.name)
        print(comment.body + '\n')

    


