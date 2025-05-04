import os
import time
#
#client = OpenAI(
#  api_key=os.getenv('OPENAI_KEY', None)
#)
#
#
#completion = client.chat.completions.create(
#  model="gpt-4o-mini",
#  store=True,
#  messages=[
#    {"role": "developer", "content": "sei un dipendente apicale dell'università IULine. Visita il sito www.iuline.it e raccogli più informazioni possibili."},
#    {"role": "user", "content": "Quali sono i corsi di laurea offerti dall'università?"}
#  ]
#)
#print(completion.choices[0].message.content);

from openai import OpenAI
client = OpenAI(
    api_key=os.getenv('OPENAI_KEY', None)
)

response = client.responses.create(
    model="gpt-4.1",
    input=[
        {"role": "developer", "content": "sei un dipendente apicale dell'università IULine. Visita il sito www.iuline.it e raccogli più informazioni possibili."},
#        {"role": "user", "content": "Quali sono i corsi di laurea offerti dall'università?"}
        {"role": "user", "content": "Voglio più informazioni su 'LM-49 – Progettazione e gestione dei sistemi turistici'"}
    ]
)

print(response.output_text)
