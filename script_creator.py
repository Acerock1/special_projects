#!/usr/bin/env python3

import requests
import os
import openai
 

Openai_prompt = input("How may I help you today?")
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Completion.create(
  model="text-davinci-003",
  prompt="f"{Openai_prompt}",
  max_tokens=7,
  temperature=0.5
)

print(openai.completion.create)


'''
api_endpoint =  https://api.openai.com/v1/completions
api_key = ""

openai.Completion.create(
  model="text-davinci-003",
  prompt='f"Write a "',
  max_tokens=100,
  temperature=
)
 
'''
