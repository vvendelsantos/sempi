import streamlit as st

st.set_page_config(page_title="Gerador de Emails - VII SEMPI", layout="wide")
st.title("Gerador de Emails - VII SEMPI")

tab1, tab2, tab3 = st.tabs(["Avaliação Completa", "Desclassificação", "Resultado Trabalho Escrito"])

# --- Aba Avaliação Completa ---
with tab1:
    st.header("Email de Avaliação Completa")

    nome = st.text_input("Nome do(a) participante", key="nome")

    st.subheader("Notas Avaliador(a) I")
    c1_a1 = st.text_input("1. Correspondência ao tema e seção temática (Avaliador I)", key="c1_a1")
    c2_a1 = st.text_input("2. Originalidade e contribuição (Avaliador I)", key="c2_a1")
    c3_a1 = st.text_input("3. Clareza do problema, objetivos e justificativa (Avaliador I)", key="c3_a1")
    c4_a1 = st.text_input("4. Adequação metodológica (Avaliador I)", key="c4_a1")
    c5_a1 = st.text_input("5. Clareza e coerência dos resultados (Avaliador I)", key="c5_a1")
    c6_a1 = st.text_input("6. Domínio do conteúdo apresentado (Avaliador I)", key="c6_a1")
    c7_a1 = st.text_input("7. Adequação ao tempo de apresentação (Avaliador I)", key="c7_a1")
    media_a1 = st.text_input("Média ponderada Avaliador(a) I", key="media_a1")

    st.subheader("Notas Avaliador(a) II")
    c1_a2 = st.text_input("1. Correspondência ao tema e seção temática (Avaliador II)", key="c1_a2")
    c2_a2 = st.text_input("2. Originalidade e contribuição (Avaliador II)", key="c2_a2")
    c3_a2 = st.text_input("3. Clareza do problema, objetivos e justificativa (Avaliador II)", key="c3_a2")
    c4_a2 = st.text_input("4. Adequação metodológica (Avaliador II)", key="c4_a2")
    c5_a2 = st.text_input("5. Clareza e coerência dos resultados (Avaliador II)", key="c5_a2")
    c6_a2 = st.text_input("6. Domínio do conteúdo apresentado (Avaliador II)", key="c6_a2")
    c7_a2 = st.text_input("7. Adequação ao tempo de apresentação (Avaliador II)", key="c7_a2")
    media_a2 = st.text_input("Média ponderada Avaliador(a) II", key="media_a2")

    nota_final_escrito = st.text_input("Nota final do trabalho escrito", key="nota_final_escrito")
    nota_final_oral = st.text_input("Nota final da apresentação oral", key="nota_final_oral")
    nota_geral = st.text_input("Nota geral (média ponderada)", key="nota_geral")

    if st.button("📤 Gerar Email Avaliação Completa"):
        html_email = f"""<!DOCTYPE html>
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
    table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 10px;
    }}
    th, td {{
      text-align: left;
      padding: 8px;
      border-bottom: 1px solid #ccc;
    }}
    th {{
      background-color: #e0e0e0;
    }}
    .nota-final {{
      background-color: #dff0d8;
      border-left: 4px solid #5cb85c;
      padding: 16px;
      margin-top: 20px;
      border-radius: 4px;
      font-weight: bold;
    }}
    a {{
      color: #0645ad;
      text-decoration: none;
    }}
    a:hover {{
      text-decoration: underline;
    }}
  </style>
</head>
<body>
  <div class="container">
    <p>Prezados(as),</p>

    <p>Espero que esta mensagem os(as) encontre bem.</p>

    <p>
      A Comissão Organizadora da <strong>VII Semana Acadêmica da Propriedade Intelectual (VII SEMPI)</strong> os(as) parabeniza pela apresentação do trabalho.
      Abaixo, apresentamos as avaliações realizadas pelos membros do Comitê Científico, com base nos critérios previamente definidos:
    </p>

    <div class="box">
      <p><strong>👤 Avaliador(a) I</strong></p>
      <table>
        <tr><th>Critério</th><th>Nota</th></tr>
        <tr><td>1. Correspondência ao tema e seção temática</td><td>{c1_a1}</td></tr>
        <tr><td>2. Originalidade e contribuição</td><td>{c2_a1}</td></tr>
        <tr><td>3. Clareza do problema, objetivos e justificativa</td><td>{c3_a1}</td></tr>
        <tr><td>4. Adequação metodológica</td><td>{c4_a1}</td></tr>
        <tr><td>5. Clareza e coerência dos resultados</td><td>{c5_a1}</td></tr>
        <tr><td>6. Domínio do conteúdo apresentado</td><td>{c6_a1}</td></tr>
        <tr><td>7. Adequação ao tempo de apresentação</td><td>{c7_a1}</td></tr>
      </table>
      <p><strong>Média ponderada do(a) Avaliador(a) I: {media_a1}</strong></p>
    </div>

    <div class="box">
      <p><strong>👤 Avaliador(a) II</strong></p>
      <table>
        <tr><th>Critério</th><th>Nota</th></tr>
        <tr><td>1. Correspondência ao tema e seção temática</td><td>{c1_a2}</td></tr>
        <tr><td>2. Originalidade e contribuição</td><td>{c2_a2}</td></tr>
        <tr><td>3. Clareza do problema, objetivos e justificativa</td><td>{c3_a2}</td></tr>
        <tr><td>4. Adequação metodológica</td><td>{c4_a2}</td></tr>
        <tr><td>5. Clareza e coerência dos resultados</td><td>{c5_a2}</td></tr>
        <tr><td>6. Domínio do conteúdo apresentado</td><td>{c6_a2}</td></tr>
        <tr><td>7. Adequação ao tempo de apresentação</td><td>{c7_a2}</td></tr>
      </table>
      <p><strong>Média ponderada do(a) Avaliador(a) II: {media_a2}</strong></p>
    </div>

    <div class="nota-final">
      Nota final do trabalho escrito: <strong>{nota_final_escrito}</strong><br />
      Nota final da apresentação oral: <strong>{nota_final_oral}</strong><br />
      Nota geral (média ponderada): <strong>{nota_geral}</strong>
    </div>

    <p>
      Aproveitamos para convidá-los(as) a participar da <strong>cerimônia de encerramento</strong>, que será realizada amanhã, <strong>5 de setembro de 2025, às XXh</strong>, no auditório do SergipeTec.
      Durante a solenidade, serão entregues os <strong>Certificados de Menção Honrosa</strong> aos três trabalhos com as maiores notas gerais em cada seção temática. Também será concedido o <strong>Certificado de Reconhecimento de “Melhor Trabalho”</strong> ao(à) autor(a) do trabalho que obteve a maior nota geral do evento.
    </p>

    <p>
      📣 Sua presença será muito importante e tornará o encerramento ainda mais especial!
    </p>

    <p>
      Permanecemos à disposição para quaisquer dúvidas ou esclarecimentos que se fizerem necessários.
    </p>
  </div>
</body>
</html>"""

        st.success("✅ Email Avaliação Completa gerado!")
        st.code(html_email, language="html")

# --- Aba Desclassificação ---
with tab2:
    st.header("Email de Desclassificação")

    nome_desc = st.text_input("Nome do(a) participante (Desclassificação)", key="nome2")

    if "motivos" not in st.session_state:
        st.session_state.motivos = ["", "", ""]

    col1, col2 = st.columns(2)
    with col1:
        if st.button("➕ Adicionar motivo"):
            st.session_state.motivos.append("")
    with col2:
        if st.button("➖ Remover último motivo"):
            if len(st.session_state.motivos) > 1:
                st.session_state.motivos.pop()

    for i in range(len(st.session_state.motivos)):
        st.session_state.motivos[i] = st.text_input(f"Motivo {i+1}", value=st.session_state.motivos[i], key=f"motivo_{i}")

    prazo_resubmissao = st.text_input("Prazo para ressubmissão", value="31 de julho de 2025", key="prazo")

    if st.button("📤 Gerar Email Desclassificação"):
        motivos_html = "\n".join(f"<li>{m}</li>" for m in st.session_state.motivos if m.strip() != "")

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

# --- Aba Resultado Trabalho Escrito ---
with tab3:
    st.header("Email Resultado do Trabalho Escrito")

    nome_res = st.text_input("Nome do(a) participante (Resultado)", key="nome3")

    st.subheader("Notas Avaliador(a) I")
    c1_r_a1 = st.text_input("1. Correspondência ao tema e seção temática (Avaliador I)", key="c1_r_a1")
    c2_r_a1 = st.text_input("2. Originalidade e contribuição (Avaliador I)", key="c2_r_a1")
    c3_r_a1 = st.text_input("3. Clareza do problema, objetivos e justificativa (Avaliador I)", key="c3_r_a1")
    c4_r_a1 = st.text_input("4. Adequação metodológica (Avaliador I)", key="c4_r_a1")
    c5_r_a1 = st.text_input("5. Clareza e coerência dos resultados (Avaliador I)", key="c5_r_a1")
    media_r_a1 = st.text_input("Média ponderada Avaliador(a) I", key="media_r_a1")
    parecer_a1 = st.text_area("Parecer Avaliador(a) I", key="parecer_a1")

    st.subheader("Notas Avaliador(a) II")
    c1_r_a2 = st.text_input("1. Correspondência ao tema e seção temática (Avaliador II)", key="c1_r_a2")
    c2_r_a2 = st.text_input("2. Originalidade e contribuição (Avaliador II)", key="c2_r_a2")
    c3_r_a2 = st.text_input("3. Clareza do problema, objetivos e justificativa (Avaliador II)", key="c3_r_a2")
    c4_r_a2 = st.text_input("4. Adequação metodológica (Avaliador II)", key="c4_r_a2")
    c5_r_a2 = st.text_input("5. Clareza e coerência dos resultados (Avaliador II)", key="c5_r_a2")
    media_r_a2 = st.text_input("Média ponderada Avaliador(a) II", key="media_r_a2")
    parecer_a2 = st.text_area("Parecer Avaliador(a) II", key="parecer_a2")

    nota_final_res = st.text_input("Nota final do trabalho", key="nota_final_res")

    link_even3 = st.text_input("Link do evento", 
                               value="https://www.even3.com.br/vii-semana-academica-da-propriedade-intelectual-594540/",
                               key="link_even3")

    if st.button("📤 Gerar Email Resultado Trabalho Escrito"):
        html_res = f"""<!DOCTYPE html>
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
    table {{
      width: 100%;
      border-collapse: collapse;
      margin-top: 10px;
    }}
    th, td {{
      text-align: left;
      padding: 8px;
      border-bottom: 1px solid #ccc;
    }}
    th {{
      background-color: #e0e0e0;
    }}
    .nota-final {{
      background-color: #dff0d8;
      border-left: 4px solid #5cb85c;
      padding: 16px;
      margin-top: 20px;
      border-radius: 4px;
      font-weight: bold;
    }}
    .parecer {{
      margin-top: 10px;
      font-style: italic;
      color: #444;
    }}
    a {{
      color: #0645ad;
      text-decoration: none;
    }}
    a:hover {{
      text-decoration: underline;
    }}
  </style>
</head>
<body>
  <div class="container">
    <p>Prezados(as),</p>

    <p>Esperamos que esta mensagem os(as) encontre bem.</p>

    <p>
      Temos o prazer de informar que o seu resumo expandido foi <strong>aprovado</strong> para apresentação oral na
      <strong>VII Semana Acadêmica da Propriedade Intelectual (VII SEMPI)</strong>.
    </p>

    <p>
      Abaixo, apresentamos as avaliações realizadas pelos membros do Comitê Científico, com base nos critérios previamente definidos:
    </p>

    <div class="box">
      <p><strong>👤 Avaliador(a) I</strong></p>
      <table>
        <tr>
          <th>Critério</th>
          <th>Nota</th>
        </tr>
        <tr><td>1. Correspondência ao tema e seção temática</td><td>{c1_r_a1}</td></tr>
        <tr><td>2. Originalidade e contribuição</td><td>{c2_r_a1}</td></tr>
        <tr><td>3. Clareza do problema, objetivos e justificativa</td><td>{c3_r_a1}</td></tr>
        <tr><td>4. Adequação metodológica</td><td>{c4_r_a1}</td></tr>
        <tr><td>5. Clareza e coerência dos resultados</td><td>{c5_r_a1}</td></tr>
      </table>
      <p><strong>Média ponderada do(a) Avaliador(a) I: {media_r_a1}</strong></p>
      <p class="parecer">"{parecer_a1}"</p>
    </div>

    <div class="box">
      <p><strong>👤 Avaliador(a) II</strong></p>
      <table>
        <tr>
          <th>Critério</th>
          <th>Nota</th>
        </tr>
        <tr><td>1. Correspondência ao tema e seção temática</td><td>{c1_r_a2}</td></tr>
        <tr><td>2. Originalidade e contribuição</td><td>{c2_r_a2}</td></tr>
        <tr><td>3. Clareza do problema, objetivos e justificativa</td><td>{c3_r_a2}</td></tr>
        <tr><td>4. Adequação metodológica</td><td>{c4_r_a2}</td></tr>
        <tr><td>5. Clareza e coerência dos resultados</td><td>{c5_r_a2}</td></tr>
      </table>
      <p><strong>Média ponderada do(a) Avaliador(a) II: {media_r_a2}</strong></p>
      <p class="parecer">"{parecer_a2}"</p>
    </div>

    <div class="nota-final">
      Nota final do trabalho: <strong>{nota_final_res}</strong>
    </div>

    <p>
      As orientações para a elaboração e o envio do arquivo da apresentação estão disponíveis no site do evento:<br />
      <a href="{link_even3}" target="_blank">
        {link_even3}
      </a>
    </p>

    <p>
      Permanecemos à disposição para quaisquer dúvidas ou esclarecimentos que se fizerem necessários.
    </p>
  </div>
</body>
</html>"""

        st.success("✅ Email Resultado Trabalho Escrito gerado!")
        st.code(html_res, language="html")
