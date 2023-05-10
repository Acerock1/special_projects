
import os
import argparse
import requests


#Parses CLI arguments
Parser = argparse.ArgumentParser()
Parser.add_argument("prompt1", help= "The first argument from the command line to send to openai")
Parser.add_argument("file_name", help= "Name of file to save code")
args = Parser.parse_args()

#api authentication variables
Api_endpoint = "https://api.openai.com/v1/completions"
api_key = os.getenv("OPENAI_API_KEY")

#request metadata
request_headers = {
    "Content-type": "application/json",
    "Authorization": "Bearer" + api_key 
}

#body of api query (dynamic)
request_data = {
    "model": "text-davinci-003",
    "prompt": f"{args.prompt1}",
    "max_tokens": 300,
    "Temperature": 0.5,
    "n": 1
}

#AI response
response =requests.post(Api_endpoint, headers=request_headers , json=request_data, timeout=10)

#paste AI response in a new file or print error message on CLI
if response.status_code == 200:
    response_text = print(response.json()["choices"][0]["text"])
    with open(args.file_name, "w") as file:
        file.write(response_text)
else:
    print(f"Requests failed with status code {str(response.status_code)}")