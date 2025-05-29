import streamlit as st
import requests
from datetime import datetime

# Título do app
st.title("Cadastro de Demandas")

# Campos do formulário
nome = st.text_input("Nome do responsável")
email = st.text_input("Email")
descricao = st.text_area("Descrição da demanda")
prioridade = st.selectbox("Prioridade", ["Baixa", "Média", "Alta"])
prazo = st.date_input("Prazo de entrega", value=datetime.today())
status = st.selectbox("Status", ["Aberta", "Em andamento", "Concluída"])

# Botão de envio
if st.button("Enviar Demanda"):
    payload = {
        "nome_responsavel": nome,
        "email": email,
        "descricao": descricao,
        "prioridade": prioridade,
        "prazo": prazo.isoformat(),
        "status": status
    }

    try:
        response = requests.post(
            "https://assistente-demandas-3.onrender.com/demandas/",
            json=payload
        )
        if response.status_code == 200:
            st.success("Demanda enviada com sucesso!")
        else:
            st.error(f"Erro ao enviar: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"Erro de conexão: {e}")
