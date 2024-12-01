# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")


def get_request(endpoint, **kwargs):
    params = ""
    if(kwargs):
        for key,value in kwargs.items():
            params=params+key+"="+value+"&"
    request_url = backend_url+endpoint+"?"+params
    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception:
        # If any error occurs
        print("Network exception occurred")
    except:
        # If any error occurs
        print("Network exception occurred")
    finally:
        print("get_request call complete!")

def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        response = requests.get(request_url)
        if response.status_code == 200:
            return response.json()  # Expecting the response to contain the sentiment
        else:
            print(f"Error: Received status code {response.status_code} from sentiment analyzer")
            return {"sentiment": "unknown"}  # Return a default value for sentiment
    except Exception as e:
        print(f"Network exception occurred: {e}")
        return {"sentiment": "unknown"}  # Return a default value for sentiment
def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    try:
        # this one ignores *all* errors on the line
        response = requests.post(request_url, json=data_dict)  # noqa: F821
        print(response.json())
        return response.json()
    except Exception:
        print("Network exception occurred")
    finally:
        print("post_review call complete!")