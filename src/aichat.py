from openai import OpenAI
from pathlib import Path
import os
import time


class ChatBot:

    def __init__(self, parent=None):
        self.client = OpenAI(
            api_key=os.getenv('OPENAI_KEY', None)
        )
        
        #self.history = [{"role": "developer", "content": "Sei uno chef esperto e riconosciuto in tutto il mondo. Hai la capacità di creare piatti sopraffini da ingredienti poveri. Sei qui per aiutare l'utente a creare una ricetta gourmet con gli ingredienti che ti elencherà. Devi usare TUTTI gli ingredienti. Se decidi di scartarne uno devi motivare la scelta e se possibile proporre un'alternativa."}]
        self.history = [{"role": "developer", "content": "Sei un bambino di 3 anni con la conoscenza di Piero Angela, Alberto Angela e Alessandro Barbero combinati in un'unico essere. Il tuo scopo è simularne il comportamento all'utente, rispondendo alle sue domande sulla storia."}]
        #self.history = [{"role": "developer", "content": "Sei un conduttore televisivo esperto su tutto. La tua bravura ti consente di creare domande a risposta multipla (MAX 4 opzioni) sul momento per due giocatori. I due giocatori rispondono uno per volta. Ogni volta che un giocatore sbaglia, prende una penalità. Quando uno dei due giocatori raggiunge 3 penalità, il gioco finisce."}]
        #self.history = [{"role": "developer", "content": "Sei Gerry Scotti. Devi leggere il testo che ti viene proposto dall'utente come se stessi presentando una puntata di Striscia la Notizia."}, {"role": "user", "content": "Senza lilleri un si lallera trallallero trallalla. Tre tigri contro tre tigri contro tre leopardi!!! L'accendiamo?"}]

    def getHistory(self):
        output = []
        for history in self.history[1:]:
            output.append(history['content'] + "\n\r")
        return output

    def run(self, msg):
        mode = -1
        
        if msg == "":
            return

        self.history.append({"role" : "user", "content" : msg})
        
        response = self.client.responses.create(
            model="gpt-4.1-nano-2025-04-14",
            input=self.history
        )
        
        self.history.append({"role" : "assistant", "content" : response.output_text})

        return response.output_text
        

