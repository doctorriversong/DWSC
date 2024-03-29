import tweepy
import time
import datetime
import keys
import schedule

# Initialize Tweepy
client = tweepy.Client(keys.bearer_token, keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret, keys.access_token, keys.access_token_secret)
api = tweepy.API(auth)

# Get the current date and time
current_date = datetime.date.today()

# Format the date as a string
formatted_date = current_date.strftime("%B, %d, %Y")

with open("tweet_content.txt", "r") as file:
    lines = file.readlines()

with open("tweet_content.txt", "w") as file:
    for line in lines:
        # Post the tweet using the read line
        response = client.create_tweet(text=line.strip())

        # Print the response
        print(response)

        # Delete the line from the file if it was tweeted
        if response is not None and response.data["text"] == line.strip():
            lines.remove(line)

        # Wait for 15 minutes (900 seconds) before the next tweet
        time.sleep(900)

# Call the keep_alive() function to keep the script running
from keep_alive import keep_alive
keep_alive()