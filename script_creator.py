#!/usr/bin/env python3

import requests
import os
import openai
 

Openai_prompt = input("How may I help you today?")
openai.api_key = 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
openai.Completion.create(model = "text-davinci-003" ,prompt = Openai_prompt ,max_tokens = 7 ,temperature = 0.5)
  

print(openai.completion.create)


