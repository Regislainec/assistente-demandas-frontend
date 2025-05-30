import streamlit as st
import requests
from datetime import date

st.title("Cadastro de Nova Demanda")

titulo = st.text_input("Título")
descricao = st.text_area("Descrição")
prioridade = st.selectbox("Prioridade", ["Baixa", "Média", "Alta"])
status = st.selectbox("Status", ["Aberta", "Em Andamento", "Concluída"])
nome_responsavel = st.text_input("Nome do Responsável")
email_responsavel = st.text_input("E-mail do Responsável")
solicitante = st.text_input("Quem solicita a demanda?")
delegado = st.text_input("Para quem foi delegada a demanda?")
prazo_entrega = st.date_input("Prazo estimado para conclusão").strftime("%Y-%m-%d")
data_conclusao = st.text_input("Data de conclusão da demanda (dd/mm/aaaa)", value="")
prazo_estimado = st.text_input("Prazo estimado (opcional)", placeholder="dd/mm/aaaa")
reajuste_necessario = st.checkbox("Necessita de reajuste/refazer trabalho?")
justificativa_reajuste = st.text_area("Justificativa para o reajuste") if reajuste_necessario else ""

if st.button("Cadastrar Demanda"):
    dados = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "status": status,
        "nome_responsavel": nome_responsavel,
        "email_responsavel": email_responsavel,
        "solicitante": solicitante,
        "delegado": delegado,
        "prazo_entrega": prazo_entrega,
        "prazo_estimado": prazo_estimado,
        "data_conclusao": data_conclusao,
        "reajuste_necessario": reajuste_necessario,
        "justificativa_reajuste": justificativa_reajuste
    }

    resposta = requests.post("https://assistente-demandas-3.onrender.com/demandas/", json=dados)

    if resposta.status_code == 200:
        st.success("Demanda cadastrada com sucesso!")
    else:
        st.error(f"Erro ao cadastrar demanda: {resposta.text}")
