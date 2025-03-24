import pytest

from src.problems.heap_priority_queue.design_twitter.script import Twitter


@pytest.fixture
def twitter():
    return Twitter()


def test_example(twitter):
    twitter.postTweet(1, 5)
    assert twitter.getNewsFeed(1) == [5]

    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    assert twitter.getNewsFeed(1) == [6, 5]

    twitter.unfollow(1, 2)
    assert twitter.getNewsFeed(1) == [5]


def test_multiple_tweets(twitter):
    for i in range(1, 15):
        twitter.postTweet(1, i)
    feed = twitter.getNewsFeed(1)
    assert feed == list(range(14, 4, -1))  # Should contain tweets 14 to 5 (10 tweets)


def test_follow_self(twitter):
    twitter.postTweet(1, 101)
    twitter.follow(1, 1)  # Follow self
    assert twitter.getNewsFeed(1) == [101]


def test_follow_unfollow(twitter):
    twitter.postTweet(1, 1)
    twitter.postTweet(2, 2)
    twitter.follow(1, 2)
    assert twitter.getNewsFeed(1) == [2, 1]
    twitter.unfollow(1, 2)
    assert twitter.getNewsFeed(1) == [1]


def test_no_tweets(twitter):
    assert twitter.getNewsFeed(1) == []


def test_follow_multiple(twitter):
    twitter.postTweet(1, 11)
    twitter.postTweet(2, 22)
    twitter.postTweet(3, 33)
    twitter.follow(1, 2)
    twitter.follow(1, 3)
    feed = twitter.getNewsFeed(1)
    assert feed == [33, 22, 11]
