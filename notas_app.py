import streamlit as st

st.set_page_config(page_title="Gerador de Emails SEMPI", layout="wide")

st.title("Gerador de Emails - VII SEMPI")

tabs = st.tabs(["Avaliação Completa", "Desclassificação", "Lembrete da Apresentação"])

# --- Aba 1: Avaliação Completa ---
with tabs[0]:
    st.header("Avaliação Completa")

    nome = st.text_input("Nome do Autor(a)", key="nome")
    
    st.subheader("Notas Avaliador(a) I")
    c1_a1 = st.number_input("1. Correspondência ao tema e seção temática", min_value=0.0, max_value=10.0, step=0.1, format="%.1f", key="c1_a1")
    c2_a1 = st.number_input("2. Originalidade e contribuição", min_value=0.0, max_value=10.0, step=0.1, format="%.1f", key="c2_a1")
    c3_a1 = st.number_input("3. Clareza do problema, objetivos e justificativa", min_value=0.0, max_value=10.0, step=0.1, format="%.1f", key="c3_a1")
    c4_a1 = st.number_input("4. Adequação metodológica", min_value=0.0, max_value=10.0, step=0.1, format="%.1f", key="c4_a1")
    c5_a1 = st.number_input("5. Clareza e coerência dos resultados", min_value=0.0, max_value=10.0, step=0.1, format="%.1f", key="c5_a1")
    c6_a1 = st.number_input("6. Domínio do conteúdo apresentado", min_value=0.0, max_value=10.0, step=0.1, format="%.1f", key="c6_a1")
    c7_a1 = st.number_input("7. Adequação ao tempo de apresentação", min_value=0.0, max_value=10.0, step=0.1, format="%.1f", key="c7_a1")

    media_a1 = round((c1_a1 + c2_a1 + c3_a1 + c4_a1 + c5_a1 + c6_a1 + c7_a1) / 7, 2)
    st.write(f"Média ponderada do(a) Avaliador(a) I: **{media_a1}**")

    st.subheader("Notas Avaliador(a) II")
    c1_a2 = st.number_input("1. Correspondência ao tema e seção temática", min_value=0.0, max_value=10.0, step=0.1, format="%.1f", key="c1_a2")
    c2_a2 = st.number_input("2. Originalidade e contribuição", min_value=0.0, max_value=10.0, step=0.1, format="%.1f", key="c2_a2")
    c3_a2 = st.number_input("3. Clareza do problema, objetivos e justificativa", min_value=0.0, max_value=10.0, step=0.1, format="%.1f", key="c3_a2")
    c4_a2 = st.number_input("4. Adequação metodológica", min_value=0.0, max_value=10.0, step=0.1, format="%.1f", key="c4_a2")
    c5_a2 = st.number_input("5. Clareza e coerência dos resultados", min_value=0.0, max_value=10.0, step=0.1, format="%.1f", key="c5_a2")
    c6_a2 = st.number_input("6. Domínio do conteúdo apresentado", min_value=0.0, max_value=10.0, step=0.1, format="%.1f", key="c6_a2")
    c7_a2 = st.number_input("7. Adequação ao tempo de apresentação", min_value=0.0, max_value=10.0, step=0.1, format="%.1f", key="c7_a2")

    media_a2 = round((c1_a2 + c2_a2 + c3_a2 + c4_a2 + c5_a2 + c6_a2 + c7_a2) / 7, 2)
    st.write(f"Média ponderada do(a) Avaliador(a) II: **{media_a2}**")

    nota_final_escrito = st.number_input("Nota final do trabalho escrito", min_value=0.0, max_value=10.0, step=0.1, format="%.2f", key="nota_final_escrito")
    nota_final_oral = st.number_input("Nota final da apresentação oral", min_value=0.0, max_value=10.0, step=0.1, format="%.2f", key="nota_final_oral")

    nota_geral = round((nota_final_escrito + nota_final_oral) / 2, 2)
    st.write(f"Nota geral (média ponderada): **{nota_geral}**")

    if st.button("📤 Gerar HTML Avaliação Completa"):
        html = f"""<!DOCTYPE html>
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
        <tr><td>1. Correspondência ao tema e seção temática</td><td>{c1_a1:.1f}</td></tr>
        <tr><td>2. Originalidade e contribuição</td><td>{c2_a1:.1f}</td></tr>
        <tr><td>3. Clareza do problema, objetivos e justificativa</td><td>{c3_a1:.1f}</td></tr>
        <tr><td>4. Adequação metodológica</td><td>{c4_a1:.1f}</td></tr>
        <tr><td>5. Clareza e coerência dos resultados</td><td>{c5_a1:.1f}</td></tr>
        <tr><td>6. Domínio do conteúdo apresentado</td><td>{c6_a1:.1f}</td></tr>
        <tr><td>7. Adequação ao tempo de apresentação</td><td>{c7_a1:.1f}</td></tr>
      </table>
      <p><strong>Média ponderada do(a) Avaliador(a) I: {media_a1}</strong></p>
    </div>

    <div class="box">
      <p><strong>👤 Avaliador(a) II</strong></p>
      <table>
        <tr><th>Critério</th><th>Nota</th></tr>
        <tr><td>1. Correspondência ao tema e seção temática</td><td>{c1_a2:.1f}</td></tr>
        <tr><td>2. Originalidade e contribuição</td><td>{c2_a2:.1f}</td></tr>
        <tr><td>3. Clareza do problema, objetivos e justificativa</td><td>{c3_a2:.1f}</td></tr>
        <tr><td>4. Adequação metodológica</td><td>{c4_a2:.1f}</td></tr>
        <tr><td>5. Clareza e coerência dos resultados</td><td>{c5_a2:.1f}</td></tr>
        <tr><td>6. Domínio do conteúdo apresentado</td><td>{c6_a2:.1f}</td></tr>
        <tr><td>7. Adequação ao tempo de apresentação</td><td>{c7_a2:.1f}</td></tr>
      </table>
      <p><strong>Média ponderada do(a) Avaliador(a) II: {media_a2}</strong></p>
    </div>

    <div class="nota-final">
      Nota final do trabalho escrito: <strong>{nota_final_escrito:.2f}</strong><br />
      Nota final da apresentação oral: <strong>{nota_final_oral:.2f}</strong><br />
      Nota geral (média ponderada): <strong>{nota_geral:.2f}</strong>
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
        st.success("✅ HTML gerado com sucesso!")
        st.code(html, language="html")


# --- Aba 2: Desclassificação ---
with tabs[1]:
    st.header("Desclassificação")

    nome_des = st.text_input("Nome do Autor(a) para Desclassificação", key="nome_des")
    
    motivos = st.session_state.get("motivos", [""])  # manter lista em sessão

    def add_motivo():
        motivos.append("")
        st.session_state["motivos"] = motivos

    def remove_motivo():
        if motivos:
            motivos.pop()
            st.session_state["motivos"] = motivos

    # Controle para editar motivos
    st.write("### Motivos para desclassificação (edite os textos):")
    for i in range(len(motivos)):
        motivos[i] = st.text_input(f"Motivo {i+1}", value=motivos[i], key=f"motivo_{i}")

    col1, col2 = st.columns(2)
    with col1:
        st.button("➕ Adicionar motivo", on_click=add_motivo)
    with col2:
        st.button("➖ Remover motivo", on_click=remove_motivo)

    if st.button("📤 Gerar HTML Desclassificação"):
        motivos_html = "".join(f"<li>{m}</li>" for m in motivos if m.strip() != "")
        html_des = f"""<!DOCTYPE html>
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
        <strong>31 de julho de 2025</strong>.
      </p>

      <p>
        Permanecemos à disposição para quaisquer dúvidas ou esclarecimentos que se fizerem necessários.
      </p>
    </div>
  </body>
</html>"""
        st.success("✅ HTML gerado com sucesso!")
        st.code(html_des, language="html")


# --- Aba 3: Lembrete da Apresentação ---
with tabs[2]:
    st.header("Lembrete da Apresentação")

    tempo_apresentacao = st.text_input("Tempo para exposição do trabalho (minutos)", value="XX", key="tempo_exp")
    tempo_arguicao = st.text_input("Tempo para arguição/comentários (minutos)", value="X", key="tempo_arg")

    if st.button("📤 Gerar HTML Lembrete da Apresentação"):
        html_lembrete = f"""<!DOCTYPE html>
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
      padding: 0 20px 20px 20px;
    }}
    .container {{
      max-width: 700px;
      margin: auto;
    }}
    p {{
      margin-bottom: 16px;
    }}
    a {{
      color: #0645ad;
      text-decoration: none;
    }}
    a:hover {{
      text-decoration: underline;
    }}
    .highlight {{
      background-color: #f0f0f0;
      border-left: 4px solid #999999;
      padding: 12px 16px;
      border-radius: 4px;
      margin: 16px 0;
      font-size: 0.95em;
    }}
  </style>
</head>
<body>
  <div class="container">
    <p>Prezados(as),</p>

    <p>
      A Comissão Organizadora da <strong>VII Semana Acadêmica da Propriedade Intelectual (VII SEMPI)</strong> relembra que as apresentações dos resumos aprovados acontecerão <strong>amanhã</strong>. A programação completa, contendo datas, horários, locais e a ordem das apresentações, já se encontra disponível no site oficial do evento:
    </p>

    <p>
      <a href="https://www.even3.com.br/vii-semana-academica-da-propriedade-intelectual-594540/" target="_blank" rel="noopener noreferrer">
        https://www.even3.com.br/vii-semana-academica-da-propriedade-intelectual-594540/
      </a>
    </p>

    <div class="highlight">
      <p><strong>⚠️ Orientações importantes:</strong></p>
      <ul style="margin-top: 0; padding-left: 20px;">
        <li>Autores que apresentarão seus trabalhos presencialmente devem comparecer ao local da sessão com, no mínimo, <strong>20 minutos de antecedência</strong>.</li>
        <li>Essa orientação também se aplica aos participantes com apresentação on-line autorizada, mediante justificativa formal.</li>
        <li><strong>Não serão permitidas correções ou substituições</strong> do arquivo de apresentação durante o evento.</li>
      </ul>
    </div>

    <p>
      Cada apresentador(a) disporá de até <strong>{tempo_apresentacao} minutos</strong> para a exposição do trabalho, seguidos de até <strong>{tempo_arguicao} minutos</strong> para arguição e/ou comentários dos(as) avaliadores(as).
    </p>

    <p>
      Cada trabalho será avaliado por, no mínimo, dois pareceristas. Os critérios de avaliação da apresentação oral seguem os mesmos adotados para o trabalho escrito, com o acréscimo dos seguintes itens:
    </p>

    <ul style="padding-left: 20px;">
      <li>Domínio do conteúdo apresentado;</li>
      <li>Adequação ao tempo de apresentação.</li>
    </ul>

    <p>
      Cada critério será avaliado em uma escala de 0 a 10, e a nota final de cada avaliador será calculada com base na média ponderada das notas atribuídas. A nota final da apresentação corresponderá à média aritmética das avaliações dos dois pareceristas.
    </p>

    <p>
      Para fins de premiação, será considerada a média ponderada entre a nota do resumo e a nota da apresentação.
    </p>

    <p>
      Desejamos uma excelente apresentação!
    </p>
  </div>
</body>
</html>"""

        st.success("✅ HTML do Lembrete da Apresentação gerado!")
        st.code(html_lembrete, language="html")
