from bot import KeywordBot

def main():
    print("🤖 Super KeywordBot (TI + Diversão). Digite 'sair' para encerrar.\n")
    bot = KeywordBot("intents.json")
    history = []

    while True:
        user_input = input("Você: ")
        if user_input.lower() in ["sair", "exit", "quit"]:
            print("Bot: Até mais! Foi ótimo conversar com você.")
            break

        resposta, categoria = bot.responder_com_categoria(user_input)
        history.append({"Você": user_input, "Bot": resposta, "Categoria": categoria})
        print(f"Bot ({categoria}): {resposta}\n")

def exibir_historico(history):
    print("\n=== Histórico da Conversa ===")
    for item in history:
        print(f"Você: {item['Você']}")
        print(f"Bot ({item['Categoria']}): {item['Bot']}\n")

if __name__ == "__main__":
    main()
