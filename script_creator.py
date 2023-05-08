#!/usr/bin/env python3

import requests
import os
import openai
import argparse

'''
parser = argparse.ArgumentParser(description='OpenAI prompt')
parser.add_argument('prompt', metavar='P', type=str, help='The prompt for the OpenAI API')
args = parser.parse_args()
'''
ai_key = "YOUR_OPENAI_API_KEY"
openai.api_key = ai_key
response = openai.Completion.create(
    model="text-davinci-003",
    prompt=args.prompt,
    max_tokens=7,
    temperature=0.5
)

print(response)


