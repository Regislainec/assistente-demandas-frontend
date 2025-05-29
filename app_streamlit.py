# app_streamlit.py
import streamlit as st
import requests

st.title("Cadastro de Demandas")

nome_responsavel = st.text_input("Nome do responsável")
email = st.text_input("Email")
descricao = st.text_area("Descrição da demanda")
prioridade = st.selectbox("Prioridade", ["Alta", "Média", "Baixa"])
prazo_entrega = st.date_input("Prazo de entrega")
status = st.selectbox("Status", ["Aberta", "Em andamento", "Concluída"])

if st.button("Enviar Demanda"):
    payload = {
        "nome_responsavel": nome_responsavel,
        "email": email,
        "descricao": descricao,
        "prioridade": prioridade,
        "prazo_entrega": str(prazo_entrega),
        "status": status
    }

    try:
        response = requests.post("https://assistente-demandas-3.onrender.com/demandas/", json=payload)
        if response.status_code == 200:
            st.success("Demanda enviada com sucesso!")
        else:
            st.error(f"Erro ao enviar: {response.status_code} - {response.text}")
    except Exception as e:
        st.error(f"Erro ao enviar: {e}")
