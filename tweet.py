import tweepy
from details import deets
def extract(q):
    keywords = q.split(" ")
    print(keywords)
    pos = keywords.index("tweet")
    x = keywords[pos+1]
    sent = ' '.join(str(k) for k in keywords[pos+1:])
    return sent

def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)

def tweet(q):
    
    # Fill in the values noted in previous step here
      cfg = { 
      "consumer_key"        : str(deets.consumer_key),
      "consumer_secret"     : str(deets.consumer_secret),
      "access_token"        : str(deets.access_token),
      "access_token_secret" : str(deets.access_token_secret) 
      }
      try:
          api = get_api(cfg)
          tweet = extract(q)
          status = api.update_status(status=tweet)
          print("DONE")
      except exception as e:
          print("Tweet failed!Please try again")
  
#tweet("hey!! can you tweet heyyaa!! wht r u upto guys?")