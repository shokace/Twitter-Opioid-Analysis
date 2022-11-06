import pip._vendor.requests as requests
import os
import json
import pandas as pd
from textblob import TextBlob


# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = "AAAAAAAAAAAAAAAAAAAAAJHbhgEAAAAAsQH3IOXabq3TwpPhwYM6EabBzx0%3DLxw4YBFnU3gWLu5wIkcetHq8KW6UVgj3bQ0Ad0UPTQOGDvRwtI"

search_url = "https://api.twitter.com/2/tweets/search/recent"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
query_params = {'query': 'drug_use','tweet.fields': 'author_id',
'max_results': 100,
}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2FullArchiveSearchPython"
    return r


def connect_to_endpoint(url, params):
    global response
    response = requests.get(url, auth=bearer_oauth, params=params).json()
    # print(response.status_code)
    # if response.status_code != 200:
    #     raise Exception(response.status_code, response.text)
    # return response.json()


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    #print(json.dumps(json_response, indent=4, sort_keys=True))
    df = pd.DataFrame(response['data'])
    sentences = df['text']
    sentimentList = []
    

    for sentence in sentences:
        sentimentList.append(TextBlob(sentence).sentiment.polarity)
        
         
    df['Sentiment'] = sentimentList
    df.to_csv('response_python.csv') 
      
    
        
        
       




if __name__ == "__main__":
    main()



# Turn data into dataframes with pandas CHECK
# Read text from dataframe and classify by sentiment CHECK
# Insert senitment into dataframe 
# Plot data on a bar chart 