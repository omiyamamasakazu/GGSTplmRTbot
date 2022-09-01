import tweepy

#Twitter情報。これは公開NG。
#＊＊＊＊＊＊＊＊には自分自身のAPIキーなどを入力してください

consumer_key        = '＊＊＊＊＊＊＊＊'
consumer_secret     = '＊＊＊＊＊＊＊＊'
access_token        = '＊＊＊＊＊＊＊＊'
access_token_secret = '＊＊＊＊＊＊＊＊'

#Twitterの認証
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# 指定した条件（検索ワード、検索件数）に一致するユーザ情報を取得

search_results = api.search_tweets(q="", result_type="mixed",count=20)
for result in search_results:
    tweet_id = result.id #Tweetのidを取得
    user_name = result.user._json['screen_name'] #ユーザーのidを取得
    user_id= result.user._json['id']

    try:
        api.retweet(tweet_id) #リツイートする
    except Exception as e:
        print(e)
