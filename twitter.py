import tweepy

def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)

def main():
  # Fill in the values noted in previous step here
  cfg = { 
    "consumer_key"        : "GZI67A7mCUSVAiKSotV7VL8iL",
    "consumer_secret"     : "iUb3v4KEB1GtCiXHxoygRTfZtpZYLayh74vcdMqGtCIahhqPDW",
    "access_token"        : "966150848358289408-zYjf4OeRmT5BEpThOIebtAsxkd8e7DV",
    "access_token_secret" : "0eSbBzenK7v935Y4mvZZDyZ0iBdw9rK0klLlzgemupEZb" 
    }

  api = get_api(cfg)
  tweet = "hey guys"
  status = api.update_status(status=tweet) 
  # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
  main()

