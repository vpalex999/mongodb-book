"""
TweetArchiver будет состоять из двух компонентов:

1. архиватор.
2. визуализатор.

Архиватор будет выполнять API поиска, предоставляемый Twitter, и сохранять найденные "твиты",
а визуализатор - показывать результаты в браузере.
"""
import pymongo
import twitter as t
from pymongo import MongoClient

DATABASE_NAME = "twitter-archive"
COLLECTION_NAME = "tweets"
TAGS = ["mongodb", "python"]


class TweetArchiver:
    def __init__(self, tag: str) -> None:
        self.tag = tag

        self.connection = MongoClient(
            host="localhost", port=27018, username="root", password="example")
        self.db = self.connection[DATABASE_NAME]
        self.tweets = self.db[COLLECTION_NAME]

        self.tweets_found = 0

    def save_tweets_for(self):
        self.tweets.insert_one({"tag": self.tag})


for tag in TAGS:
    archive = TweetArchiver(tag)
    archive.save_tweets_for()
