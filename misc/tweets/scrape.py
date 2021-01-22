TOKEN = 'AAAAAAAAAAAAAAAAAAAAAE%2FUIgEAAAAAStTDHwRHyd7qv3EGUBZmrA%2BYFIM%3DpkK5vBNoAHyIkzWxLscYoBcduByca04USOYX1hGeh4Q7zNrTaw'

curl --request GET --url 'https://api.twitter.com/1.1/search/tweets.json?q=nasa&result_type=popular' --header 'authorization: OAuth oauth_consumer_key="consumer-key-for-app",oauth_nonce="generated-nonce", oauth_signature="generated-signature",oauth_signature_method="HMAC-SHA1", oauth_timestamp="generated-timestamp",oauth_token=TOKEN, oauth_version="1.0"'
#$ twurl /1.1/search/tweets.json?q=nasa&result_type=popular
