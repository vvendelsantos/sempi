import streamlit as st

st.title("Gerador de Emails - VII SEMPI")

tab1, tab2 = st.tabs(["Avaliação Completa", "Desclassificação"])

# Aba avaliação omitida aqui (igual antes) só focando na aba desclassificação com motivos dinâmicos

with tab2:
    st.header("Email de Desclassificação")

    nome_desc = st.text_input("Nome do(a) participante (Desclassificação)", key="nome2")

    # Lista de motivos dinâmicos
    motivos = st.session_state.get("motivos", ["", "", ""])  # inicia com 3 motivos vazios

    def adicionar_motivo():
        motivos.append("")
        st.session_state["motivos"] = motivos

    st.button("➕ Adicionar motivo", on_click=adicionar_motivo)

    # Renderizar caixas de texto para cada motivo
    for i in range(len(motivos)):
        motivos[i] = st.text_input(f"Motivo {i+1}", value=motivos[i], key=f"motivo_{i}")

    st.session_state["motivos"] = motivos  # salvar no session_state

    prazo_resubmissao = st.text_input("Prazo para ressubmissão", value="31 de julho de 2025", key="prazo")

    if st.button("📤 Gerar Email Desclassificação"):
        # Montar lista HTML dos motivos preenchidos (ignorar vazios)
        motivos_html = "\n".join(f"<li>{m}</li>" for m in motivos if m.strip() != "")

        html_desc = f"""<!DOCTYPE html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <style>
      body {{
        font-family: Arial, sans-serif;
        line-height: 1.6;
        color: #333333;
        background-color: #ffffff;
        margin: 0;
        padding: 0;
      }}
      .container {{
        padding: 20px;
      }}
      .box {{
        background-color: #f0f0f0;
        border-left: 4px solid #999999;
        padding: 16px;
        margin: 20px 0;
        border-radius: 4px;
      }}
      ol {{
        padding-left: 20px;
        margin: 0;
      }}
    </style>
  </head>
  <body>
    <div class="container">
      <p>Prezado(a) autor(a),</p>

      <p>Esperamos que esta mensagem o(a) encontre bem.</p>

      <p>
        Agradecemos o envio do seu resumo expandido à
        <strong>VII Semana Acadêmica da Propriedade Intelectual (VII SEMPI)</strong>. Após análise preliminar (<em>desk review</em>), informamos que seu trabalho <strong>não atendeu</strong> integralmente às diretrizes estabelecidas pela Comissão Organizadora para avançar à próxima etapa de avaliação por pares.
      </p>

      <div class="box">
        <p><strong>📌 Principais aspectos a serem corrigidos:</strong></p>
        <ol>
          {motivos_html}
        </ol>
      </div>

      <p>
        Solicitamos, gentilmente, que as correções sejam realizadas e o trabalho corrigido seja ressubmetido no sistema até o dia
        <strong>{prazo_resubmissao}</strong>.
      </p>

      <p>
        Permanecemos à disposição para quaisquer dúvidas ou esclarecimentos que se fizerem necessários.
      </p>
    </div>
  </body>
</html>"""

        st.success("✅ Email Desclassificação gerado!")
        st.code(html_desc, language="html")
