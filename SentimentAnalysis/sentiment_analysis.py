import requests, json#Import requests library to handle HTTP requests

# analysis function
def sentiment_analyzer(text_to_analyse):
# Define a function named sentiment_analyzer that takes a string
    url= 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = {"raw_document": { "text": text_to_analyse }}
    response = requests.post(url, json = myobj, headers=headers)
    #Parsing JSON response from the API formatted_response
    formatted_response = json.loads(response.text)
    print(formatted_response)
    # Extracting sentiment label and score from the response
    label = formatted_response['documentSentiment']['label']
    score = formatted_response['documentSentiment']['score']

    return {'label': label, 'score': score}