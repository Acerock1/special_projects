#!/usr/bin/env python3

import requests
import os
import openai
import argparse

ai_key = "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"
Openai_prompt = input("How may I help you today?")
openai.api_key = ai_key
response = openai.Completion.create(
        model = "text-davinci-003" ,
        prompt = Openai_prompt ,
        max_tokens = 7 ,
        temperature = 0.5)
  

print(response)


