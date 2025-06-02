import streamlit as st
import requests
from datetime import date

API_URL = "https://assistente-demandas-backend-1.onrender.com"

st.set_page_config(page_title="Assistente de Demandas", layout="centered")

st.title("📋 Cadastro de Nova Demanda")

with st.form("form_demandas"):
    titulo = st.text_input("Título da demanda")
    descricao = st.text_area("Descrição")
    prioridade = st.selectbox("Prioridade", ["Baixa", "Média", "Alta"])
    status = st.selectbox("Status", ["Aberta", "Em Andamento", "Concluída"])
    nome_responsavel = st.text_input("Nome do responsável")
    email_responsavel = st.text_input("E-mail do responsável")
    solicitante = st.text_input("Quem está solicitando?")
    delegado = st.text_input("Para quem foi delegada a demanda?")
    prazo_entrega = st.date_input("Prazo estimado para conclusão", value=date.today())
    prazo_estimado = st.text_input("Prazo estimado (opcional, formato dd/mm/aaaa)", "")
    data_conclusao = st.text_input("Data de conclusão (se houver, formato dd/mm/aaaa)", "")
    reajuste_necessario = st.checkbox("Necessita de reajuste/refazer trabalho?")
    justificativa_reajuste = ""
    if reajuste_necessario:
        justificativa_reajuste = st.text_area("Justificativa para o reajuste")

    submitted = st.form_submit_button("Enviar demanda")

    if submitted:
        payload = {
            "titulo": titulo,
            "descricao": descricao,
            "prioridade": prioridade,
            "status": status,
            "nome_responsavel": nome_responsavel,
            "email_responsavel": email_responsavel,
            "solicitante": solicitante,
            "delegado": delegado,
            "prazo_entrega": prazo_entrega.strftime("%Y-%m-%d"),
            "prazo_estimado": prazo_estimado or None,
            "data_conclusao": data_conclusao or None,
            "reajuste_necessario": reajuste_necessario,
            "justificativa_reajuste": justificativa_reajuste or None
        }

        try:
            resposta = requests.post(f"{API_URL}/demandas/", json=payload)
            if resposta.status_code == 200:
                st.success("✅ Demanda cadastrada com sucesso!")
            else:
                st.error(f"❌ Erro ao cadastrar: {resposta.text}")
        except Exception as e:
            st.error(f"Erro de conexão: {e}")

# ----------------------------
# Botão para listar demandas
# ----------------------------
st.markdown("---")
if st.button("📂 Ver todas as demandas cadastradas"):
    try:
        resposta = requests.get(f"{API_URL}/demandas/")
        if resposta.status_code == 200:
            demandas = resposta.json()
            st.subheader("📄 Demandas encontradas:")
            for d in demandas:
                st.markdown(f"**ID #{d['id']} - {d['titulo']}**")
                st.write(f"Status: {d['status']} | Responsável: {d['nome_responsavel']}")
                st.write(f"Prazo: {d['prazo_entrega']}")
                st.write("---")
        else:
            st.error(f"Erro ao buscar demandas: {resposta.text}")
    except Exception as e:
        st.error(f"Erro de conexão: {e}")
