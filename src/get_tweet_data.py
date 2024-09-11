import re

def get_tweet_data(tweet):
    regex_mention = re.compile(r"(?<=\s)@\S*")
    regex_tag = re.compile(r"(?<=\s)#\S*")

    mentions = list(set(regex_mention.findall(tweet)))
    tags = list(set(regex_tag.findall(tweet)))
    
    data = { 
        "tags": tags, 
        "mentions": mentions, 
        "tagCount": len(tags), 
        "mentionCount": len(mentions), 
        "length": len(tweet)
    }

    return data