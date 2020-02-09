import pytest
import tweet_api
import google_api

def test():
    assert tweet_api.print_tweet("@Twitter",10) == True
    assert tweet_api.print_tweet("@Discovery",30) == True
    
if __name__ == "__main__":
    test()