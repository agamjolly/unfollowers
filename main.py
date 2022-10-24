import os
from instagrapi import Client
from flask import Flask
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
cl = Client()

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')


@app.route('/')
def index(cl=cl):
    cl.login(USERNAME, PASSWORD)
    user_id = cl.user_id_from_username(USERNAME)
    followers_list = cl.user_followers(user_id)
    following_list = cl.user_following(user_id)

    return {
        "unfollowers": list(set([
            following_list[follower].username for follower in following_list
        ]) - set([
            followers_list[follower].username for follower in followers_list]))
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
