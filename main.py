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

new_lines = []
for line in lines:
    # Post the tweet using the read line
    response = client.create_tweet(text=line.strip())

    # Print the response
    print(response)

    # If the tweet was not successful, keep the line for the next attempt
    if response is None or response.data["text"] != line.strip():
        new_lines.append(line)

    # Wait for 15 minutes (900 seconds) before the next tweet
    time.sleep(900)

# Write the remaining tweets back to the file
with open("tweet_content.txt", "w") as file:
    file.writelines(new_lines)

# Call the keep_alive() function to keep the script running
from keep_alive import keep_alive
keep_alive()
