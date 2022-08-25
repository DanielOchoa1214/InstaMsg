import os
import openai

openai.api_key = "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"


def generateMsg(prompt):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response["choices"][0].text
