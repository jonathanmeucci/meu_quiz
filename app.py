from flask import Flask, render_template, request

app = Flask(__name__)

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

@app.route("/", methods=["GET", "POST"])
def quiz():
    resultado = None
    if request.method == "POST":
        acertos = 0
        for i, item in enumerate(perguntas):
            resposta_usuario = request.form.get(f"pergunta{i}")
            if resposta_usuario == item["resposta"]:
                acertos += 1
        resultado = f"Você acertou {acertos} de {len(perguntas)} perguntas."

    return render_template("index.html", perguntas=perguntas, resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)