## api-design-jyueling

API implemented  to get Twitter Feeds and Text description of the images, by using Tweepy and Google Vision API.

## Requirement

Get credentials of Twitter API and Google Vision API

- [Twitter API](https://developer.twitter.com/en/apps)
- [Google Vision API](https://cloud.google.com/vision/docs/quickstart-cli?hl=en)
	<br> Copy the JSON file under the same directory of python files.
	<br> Change the filename in google_api.py 
	```python
  os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="yourfilename.json"
  ```
## CB and CI

Test case pass when check locally. Due to security concern, the credentials are all removed so that test failed here.
  
## Usage

There is an example in main.py
```python
   tweet_api.print_tweet("@Twitter",10)
```
This API get the 10 tweets from Twitter. It prints out the twitter feeds and description of the images.

## Example Result
![Image text](https://github.com/BUEC500C1/api-design-jyueling/raw/master/example_result.png)

