import praw
import requests
from bs4 import BeautifulSoup
import time


reddit = praw.Reddit(client_id='YOUR_CLIENT_ID',
                     client_secret='YOUR_CLIENT_SECRET',
                     user_agent='YOUR_USER_AGENT',
                     username='YOUR_USERNAME',
                     password='YOUR_PASSWORD')


def get_vote_count():
    url = 'https://example.com'  
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    vote_count = soup.find('div', {'class': 'vote-count'}).text
    return vote_count


while True:
    vote_count = get_vote_count()
    subreddit = reddit.subreddit('YOUR_SUBREDDIT_NAME')
    post = subreddit.submit(title='General Elections Vote Count', selftext=vote_count)
    post.edit(vote_count)
    time.sleep(3600)
