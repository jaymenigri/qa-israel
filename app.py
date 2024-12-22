import openai
import streamlit as st

# Configure sua chave de API do OpenAI
openai.api_key = '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'

# Função para a resposta genérica com fontes específicas
def resposta_generica(pergunta):
    custom_prompt = (
        "Responda esta pergunta com base exclusivamente nas seguintes fontes: "
        "- Livro: 'A History of Israel' de Benny Morris. "
        "- Publicações da Universidade Hebraica de Jerusalém. "
        "- Artigos publicados por Alan Dershowitz, Samuel Feldberg e Ben Shapiro. "
        "Ignore quaisquer outras fontes ou interpretações."
        f"\n\nPergunta: {pergunta}"
    )

    try:
        # Fazendo a chamada para a API do OpenAI usando o modelo gpt-3.5-turbo
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Usando gpt-3.5-turbo para melhor performance
            messages=[
                {"role": "system", "content": "Você é um assistente inteligente."},
                {"role": "user", "content": custom_prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )
        # Retornando a resposta gerada pelo modelo
        return response['choices'][0]['message']['content'].strip()

    except Exception as e:
        return f"Ocorreu um erro ao gerar a resposta: {str(e)}"

# Interface do Streamlit
st.title("Aplicativo de Perguntas e Respostas sobre Israel")

pergunta = st.text_input("Faça sua pergunta sobre Israel:")

if pergunta:
    resposta = resposta_generica(pergunta)
    st.write(resposta)
