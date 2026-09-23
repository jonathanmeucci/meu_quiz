import unicodedata

def normalizar(texto):
    texto = texto.lower()
    texto = unicodedata.normalize('NFKD', texto)
    texto = ''.join(c for c in texto if not unicodedata.combining(c))
    return texto

perguntas = [
    {
        "pergunta": "Qual é a capital do Brasil?",
        "opcoes": ["Rio de Janeiro", "Brasília", "São Paulo"],
        "resposta": "Brasília"
    },
    {
        "pergunta": "Quanto é 7 x 8?",
        "opcoes": ["54", "56", "58"],
        "resposta": "56"
    },
    {
        "pergunta": "Qual linguagem estamos usando agora?",
        "opcoes": ["Java", "Python", "C++"],
        "resposta": "Python"
    }
]

acertos = 0

for item in perguntas:
    print("\n" + item["pergunta"])
    for opcao in item["opcoes"]:
        print("-", opcao)

    resposta_usuario = input("Sua resposta: ")

    if normalizar(resposta_usuario) == normalizar(item["resposta"]):
        print("Certo!")
        acertos += 1
    else:
        print(f"Errado! A resposta certa era: {item['resposta']}")

print(f"\nVocê acertou {acertos} de {len(perguntas)} perguntas.")