import os
import sys
import time

# Send a GET request to the Heroku app every 30 minutes to keep it alive
def keep_alive():
    while True:
        try:
            os.system("curl https://keep-alive-twit-bot.herokuapp.com")
        except:
            print("Couldn't send the request")
        time.sleep(30 * 60)