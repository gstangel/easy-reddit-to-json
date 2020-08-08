import praw
import os.path
import json

#insert your client id, secret key, bot name, and username 
reddit = praw.Reddit(client_id = "", client_secret = "", user_agent = "", username = "")

#Change what data you want appended to the JSON file using these variables
appendComments = True
appendAuthor = True
appendPostBody = True
appendTitle = True
appendDateTime = True
appendPostID = True
appendNumComments = True
appendNumUpvotes = True
appendFlair = True
appendUpvoteRatio = True
appendURL = True

targetSubreddit = "wallstreetbets"
postLimit = 50


def post_to_json():
    #.new defines the sorting method, other methods include .hot, .top
    for submission in reddit.subreddit(targetSubreddit).hot(limit=postLimit):
        post = {}
        post['post'] = []
        
        try:
            #naming file as postid
            filename = str(submission.id) + ".json"

            if appendPostID == True:
                post['post'].append({'postID': str(submission.id)})
            if appendFlair == True:
                post['post'].append({'flair': str(submission.link_flair_text)})
            if appendNumUpvotes == True:
                post['post'].append({'upvotes': str(submission.score)})
            if appendUpvoteRatio == True:
                post['post'].append({'upvoteRatio': str(submission.upvote_ratio)})
            if appendAuthor == True:
                post['post'].append({'author': str(submission.author)})
            if appendTitle == True:
                post['post'].append({'title': str(submission.title)})
            if appendPostBody == True:
                post['post'].append({'bodytext': str(submission.selftext)})
            if appendDateTime == True:
                post['post'].append({'dateTimePosted': str(submission.selftext)})
            if appendURL == True:
                post['post'].append({'url': str(submission.url)})
                #adding comments  to dictionary
            if appendComments == True:
                for comment in submission.comments.list():
                        #filter out bots
                    if ("bot" in comment.body) == False:
                            #write comment to file
                        post['post'].append({'comment': comment.body})
                #writing JSON
                with open(filename, "w+") as outfile:
                    json.dump(post, outfile)
     #catch encoding errors for emojis, no commetns
        except:
            continue

if __name__ == '__main__':
    post_to_json()
