# Microsoft Cognitive Services CV API reference: https://westcentralus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa

# Import the request library to make a REST API call from Python 
import requests

# Import the json library to read the data from the web service
import json

# Add your subscription key 
subscription_key = "ADD_SUBSCRIPTION_KEY"

# Add your endpoint or request URL from Azure Cognitive Services 
endpoint = "ENDPOINT_ADDRESS"
request_url = endpoint + "vision/v2.0/analyze"

# Request the parameters you want to read
parameters = {"visualFeatures":"Description, Faces",
                "details":"Celebrities",
                "language":"en" }

# Request the headers
headers = {"Content-Type":"application/json",
             "Ocp-Apim-Subscription-Key":subscription_key}

# Pass in the image
image_path = "IMAGE_PATH_FROM_LOCAL_ADDRESS"
image_data = open(image_path, "rb").read()

# Use HTTP POST to call this function
response = requests.post(request_url, headers=headers, params=parameters, data=image_data)

# In case the call returns an error 
response.raise_for_status()

# Show JSON results 
results = response.json()
print(json.dumps(results))
print()

# Determine if the person in the image uploaded is a celebrity or not
print("This image's description is " + results['description']['captions'][0]['text'])

not_celebrity = results['categories'][0]['detail']['celebrities']
if not_celebrity == []:
    print("Based on Azure CV Cognitive Services, this person is not a celebrity yet.")
    print()
    quit()

celebrity = results['categories'][0]['detail']['celebrities'][0]['name']
if celebrity:
    print("This celebrity is " + celebrity)  
print()