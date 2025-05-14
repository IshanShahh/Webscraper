import requests 
from bs4 import BeautifulSoup
import praw
import re

reddit = praw.Reddit(
    client_id="nZg4aRNfxHhvuBVRbIs0Ww",
    client_secret="VDH1Tc3HLDXJUsjYQ6nnHkA8On5y8g",
    user_agent="SqueezeScraper"
)

subreddit = reddit.subreddit("Shortsqueeze")
posts = subreddit.hot(limit=25)

ticker_pattern = re.compile(r"\b[A-Z]{2,5}\b")


for post in posts:
    found = ticker_pattern.findall(post.title)
    if found:
        print(found)

# response = requests.get("https://www.reddit.com/r/Shortsqueeze/")
# text = BeautifulSoup(response.text, 'html.parser')
# divs = text.find_all('div')
# for lines in divs:
#     for _ in lines.find_all('a'):
#         print(_)