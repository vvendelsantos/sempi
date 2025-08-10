import streamlit as st

# Função para processar notas (mesma linha, espaço, vírgula ou ponto e vírgula)
def processar_notas(entrada):
    return [
        float(n.strip().replace(',', '.'))
        for n in entrada.replace('\n', ' ').replace(';', ' ').split()
        if n.strip()
    ]

# Critérios usados para notas
nomes_criterios_aprov_reprov = [
    "Critério 1",
    "Critério 2",
    "Critério 3",
    "Critério 4"
]

# Configuração da página
st.set_page_config(page_title="Sistema de Avaliação", layout="wide")

tabs = st.tabs(["✅ Aprovação", "❌ Reprovação", "📊 Resultado Final"])

# =========================
# Função para criar as abas
# =========================
def criar_aba(tipo):
    st.subheader(f"Avaliação - {tipo}")

    # Avaliador I
    st.markdown("### Avaliador(a) I")
    data_avaliador_i = st.text_input(f"Data Avaliador(a) I - {tipo}", value="4 de ago de 2025")
    default_notas_i_str = " ".join([str(0.0) for _ in nomes_criterios_aprov_reprov])
    notas_i_input = st.text_input(
        f"Notas Avaliador(a) I - {tipo} (mesma linha, separadas por espaço, vírgula ou ponto e vírgula)",
        value=default_notas_i_str
    )
    notas_i_digitadas = processar_notas(notas_i_input)

    # Avaliador II
    st.markdown("### Avaliador(a) II")
    data_avaliador_ii = st.text_input(f"Data Avaliador(a) II - {tipo}", value="4 de ago de 2025")
    default_notas_ii_str = " ".join([str(0.0) for _ in nomes_criterios_aprov_reprov])
    notas_ii_input = st.text_input(
        f"Notas Avaliador(a) II - {tipo} (mesma linha, separadas por espaço, vírgula ou ponto e vírgula)",
        value=default_notas_ii_str
    )
    notas_ii_digitadas = processar_notas(notas_ii_input)

    # Mostrar no HTML com a data à direita
    st.markdown(f"""
    <p><strong>👤 Avaliador(a) I</strong> <span style="float: right;">{data_avaliador_i}</span></p>
    <p>Notas: {notas_i_digitadas}</p>
    <p><strong>👤 Avaliador(a) II</strong> <span style="float: right;">{data_avaliador_ii}</span></p>
    <p>Notas: {notas_ii_digitadas}</p>
    """, unsafe_allow_html=True)

# Criar as três abas
with tabs[0]:
    criar_aba("Aprovação")

with tabs[1]:
    criar_aba("Reprovação")

with tabs[2]:
    criar_aba("Resultado Final")
