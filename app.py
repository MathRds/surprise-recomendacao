import streamlit as st
import json
import os
from datetime import datetime

# Função para salvar dados em um arquivo JSON
def save_data(data, filename='data.json', folder='responses'):
    if not os.path.exists(folder):
        os.makedirs(folder)
    filepath = os.path.join(folder, filename)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

# Perguntas padrão
questions = [
    "Qual é o seu nome?",
    "Qual é a sua idade?",
    "Qual é a sua profissão?",
    "Qual é o seu hobby favorito?",
    "O que você prefere? (Escolha uma opção com imagem)"
]

images = {
    'Campo': 'images/campo.jpeg',
    'Praia': 'images/praia.jpeg',
    'Cidade': 'images/cidade.jpeg'
}

st.title('Formulário de Perguntas')

# Dicionário para armazenar as respostas
responses = {}

# Loop pelas perguntas e cria campos de entrada
for question in questions[:-1]:
    response = st.text_input(question)
    responses[question] = response

# Pergunta com opções e imagens
st.write(questions[-1])
option = st.radio(
    'Escolha uma opção:',
    list(images.keys())
)
responses[questions[-1]] = {
    'opcao': option,
    'imagem': images[option]
}
st.image(images[option], caption=option)

# Botão para salvar as respostas
if st.button('Salvar Respostas'):
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    filename = f'responses_{timestamp}.json'
    save_data(responses, filename)
    st.success(f'Respostas salvas em {filename}')
