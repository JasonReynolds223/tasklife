
# \nIf the context is not related to scheduling, answer with 'Wrong data inputted. Please check again.'\nContext: You only answer about scheduling.

import openai

openai.api_key = "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"

prompt = [
    {"role": "system", "content": "You: Hello, I have a question about payment method."},
    {"role": "user", "content": "Answer the question based on the context below.\nQuestion: Extract keywords in description."},
]


def optimize_data(data):
    prompt.append({"role": "user", "content" : data}) 
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=prompt,
        temperature=0.7
    )
    result = response.choices[0].message.content
    return result


