import pytest
from bot import KeywordBot

bot = KeywordBot("intents.json")

def test_saudacao():
    resposta = bot.responder("oi, tudo bem?")
    assert resposta in bot.intents["saudacao"]["respostas"]

def test_despedida():
    resposta = bot.responder("tchau, até logo")
    assert resposta in bot.intents["despedida"]["respostas"]

def test_sem_match():
    resposta = bot.responder("qual o sentido da vida?")
    assert resposta == "Não entendi... pode reformular?"