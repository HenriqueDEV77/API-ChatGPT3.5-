import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


def enviar_mensagem(mensagem):
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": mensagem}
        ],
    )
    return resposta["choices"][0]["message"]["content"]


def main():
    while True:
        texto = input("Digite aqui qual os sintomas que tem interesse de saber: ")

        if texto.lower() == "obrigado":
            break
        else:
            resposta = enviar_mensagem(texto)
            print("Chatbot:", resposta)


    print("Chatbot:", enviar_mensagem("Agradecemos, até a próxima!"))


if __name__ == "__main__":
    main()
