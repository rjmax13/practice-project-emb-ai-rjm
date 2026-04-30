import requests #Import requests library to handle HTTP requests

# analysis function
def sentiment_analyzer(text_to_analyse);
# Define a function named sentiment_analyzer that takes a string
    input(text_to_analyse) url= 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    headers = {<header_dictionary>}
	myobj = {"raw_document": { "text": text_to_analyse }}
	response = requests.post(url, json = myobj, headers=header)
    return response.text