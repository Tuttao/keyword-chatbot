import json
import random

class KeywordBot:
    def __init__(self, intents_file="intents.json"):
        with open(intents_file, "r", encoding="utf-8") as f:
            self.intents = json.load(f)

    def responder_com_categoria(self, mensagem: str):
        mensagem_lower = mensagem.lower()
        for categoria, data in self.intents.items():
            if any(keyword in mensagem_lower for keyword in data["keywords"]):
                resposta = random.choice(data["respostas"])
                return resposta, categoria
        return "Não entendi... pode reformular?", "sem_categoria"
