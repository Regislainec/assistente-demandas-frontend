# app_streamlit.py
import streamlit as st
import requests

st.set_page_config(page_title="Cadastro de Demandas", layout="centered")
st.title("Cadastro de Demandas")

with st.form("formulario_demanda"):
    titulo = st.text_input("Título da demanda")  # <-- CAMPO OBRIGATÓRIO
    nome_responsavel = st.text_input("Nome do responsável")
    email_responsavel = st.text_input("Email")
    descricao = st.text_area("Descrição da demanda")
    prioridade = st.selectbox("Prioridade", ["Alta", "Média", "Baixa"])
    prazo_entrega = st.date_input("Prazo de entrega")
    status = st.selectbox("Status", ["Aberta", "Em andamento", "Concluída"])
    enviar = st.form_submit_button("Enviar Demanda")

if enviar:
    dados = {
        "titulo": titulo,
        "descricao": descricao,
        "nome_responsavel": nome_responsavel,
        "email_responsavel": email_responsavel,
        "prioridade": prioridade,
        "prazo_entrega": str(prazo_entrega),
        "status": status,
    }

    try:
        st.info("Enviando dados para o backend...")
        response = requests.post(
            "https://assistente-demandas-3.onrender.com/demandas/",
            json=dados,
            timeout=10
        )
        st.code(response.text)
        if response.status_code == 200:
            st.success("Demanda enviada com sucesso!")
        else:
            st.error(f"Erro {response.status_code}: {response.text}")
    except requests.exceptions.RequestException as e:
        st.error(f"Falha na requisição: {e}")
    except Exception as e:
        st.error(f"Erro inesperado: {e}")
