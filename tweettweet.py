import tweepy
import time

auth = tweepy.OAuthHandler('KUsAbhAaOHN1qiE07QcWnxOb8', 'DH9vD1L3C7vNvvwEyg8jL70BWWKpEzOqHd2hymQmxmA8R9rSgw')
auth.set_access_token('1208507030606139395-bLgTSiua0XGV8Le5MT746yW9iYgTj1', '40qQEdeNuMnQWJ4EYVVXjcurTh0BqiMYHXfNfUZmNgiSr')

api = tweepy.API(auth)
user = api.me()

#Generous Bot
#Auto-Refollows new followers

def limit_handler(cursor):
	try:
		while True:
			try:
				yield cursor.next()
			except StopIteration:
				return
	except tweepy.RateLimitError:
		time.sleep(1000)

for follower in limit_handler(tweepy.Cursor(api.followers).items()):
	print(follower.name)
	follower.follow()