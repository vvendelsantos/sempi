import streamlit as st

st.set_page_config(page_title="Gerador de Email SEMPI", layout="centered")

st.title("📩 Gerador de Email Avaliação VII SEMPI")

# Entradas das notas
nome = st.text_input("Nome do(a) participante")

st.markdown("### Notas Avaliador(a) I")
C1_A1 = st.number_input("1. Correspondência ao tema e seção temática", 0.0, 10.0, step=0.1, format="%.1f", key="C1_A1")
C2_A1 = st.number_input("2. Originalidade e contribuição", 0.0, 10.0, step=0.1, format="%.1f", key="C2_A1")
C3_A1 = st.number_input("3. Clareza do problema, objetivos e justificativa", 0.0, 10.0, step=0.1, format="%.1f", key="C3_A1")
C4_A1 = st.number_input("4. Adequação metodológica", 0.0, 10.0, step=0.1, format="%.1f", key="C4_A1")
C5_A1 = st.number_input("5. Clareza e coerência dos resultados", 0.0, 10.0, step=0.1, format="%.1f", key="C5_A1")
C6_A1 = st.number_input("6. Domínio do conteúdo apresentado", 0.0, 10.0, step=0.1, format="%.1f", key="C6_A1")
C7_A1 = st.number_input("7. Adequação ao tempo de apresentação", 0.0, 10.0, step=0.1, format="%.1f", key="C7_A1")
media_A1 = round((C1_A1 + C2_A1 + C3_A1 + C4_A1 + C5_A1 + C6_A1 + C7_A1) / 7, 2)

st.markdown("### Notas Avaliador(a) II")
C1_A2 = st.number_input("1. Correspondência ao tema e seção temática", 0.0, 10.0, step=0.1, format="%.1f", key="C1_A2")
C2_A2 = st.number_input("2. Originalidade e contribuição", 0.0, 10.0, step=0.1, format="%.1f", key="C2_A2")
C3_A2 = st.number_input("3. Clareza do problema, objetivos e justificativa", 0.0, 10.0, step=0.1, format="%.1f", key="C3_A2")
C4_A2 = st.number_input("4. Adequação metodológica", 0.0, 10.0, step=0.1, format="%.1f", key="C4_A2")
C5_A2 = st.number_input("5. Clareza e coerência dos resultados", 0.0, 10.0, step=0.1, format="%.1f", key="C5_A2")
C6_A2 = st.number_input("6. Domínio do conteúdo apresentado", 0.0, 10.0, step=0.1, format="%.1f", key="C6_A2")
C7_A2 = st.number_input("7. Adequação ao tempo de apresentação", 0.0, 10.0, step=0.1, format="%.1f", key="C7_A2")
media_A2 = round((C1_A2 + C2_A2 + C3_A2 + C4_A2 + C5_A2 + C6_A2 + C7_A2) / 7, 2)

st.markdown("### Notas finais")
Nota_Final_Escrito = st.number_input("Nota final do trabalho escrito", 0.0, 10.0, step=0.1, format="%.1f")
Nota_Final_Oral = st.number_input("Nota final da apresentação oral", 0.0, 10.0, step=0.1, format="%.1f")
Nota_Geral = round((Nota_Final_Escrito + Nota_Final_Oral) / 2, 2)

if st.button("📤 Gerar HTML personalizado"):

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
        <tr><td>1. Correspondência ao tema e seção temática</td><td>{C1_A1:.1f}</td></tr>
        <tr><td>2. Originalidade e contribuição</td><td>{C2_A1:.1f}</td></tr>
        <tr><td>3. Clareza do problema, objetivos e justificativa</td><td>{C3_A1:.1f}</td></tr>
        <tr><td>4. Adequação metodológica</td><td>{C4_A1:.1f}</td></tr>
        <tr><td>5. Clareza e coerência dos resultados</td><td>{C5_A1:.1f}</td></tr>
        <tr><td>6. Domínio do conteúdo apresentado</td><td>{C6_A1:.1f}</td></tr>
        <tr><td>7. Adequação ao tempo de apresentação</td><td>{C7_A1:.1f}</td></tr>
      </table>
      <p><strong>Média ponderada do(a) Avaliador(a) I: {media_A1:.2f}</strong></p>
    </div>

    <div class="box">
      <p><strong>👤 Avaliador(a) II</strong></p>
      <table>
        <tr><th>Critério</th><th>Nota</th></tr>
        <tr><td>1. Correspondência ao tema e seção temática</td><td>{C1_A2:.1f}</td></tr>
        <tr><td>2. Originalidade e contribuição</td><td>{C2_A2:.1f}</td></tr>
        <tr><td>3. Clareza do problema, objetivos e justificativa</td><td>{C3_A2:.1f}</td></tr>
        <tr><td>4. Adequação metodológica</td><td>{C4_A2:.1f}</td></tr>
        <tr><td>5. Clareza e coerência dos resultados</td><td>{C5_A2:.1f}</td></tr>
        <tr><td>6. Domínio do conteúdo apresentado</td><td>{C6_A2:.1f}</td></tr>
        <tr><td>7. Adequação ao tempo de apresentação</td><td>{C7_A2:.1f}</td></tr>
      </table>
      <p><strong>Média ponderada do(a) Avaliador(a) II: {media_A2:.2f}</strong></p>
    </div>

    <div class="nota-final">
      Nota final do trabalho escrito: <strong>{Nota_Final_Escrito:.1f}</strong><br />
      Nota final da apresentação oral: <strong>{Nota_Final_Oral:.1f}</strong><br />
      Nota geral (média ponderada): <strong>{Nota_Geral:.2f}</strong>
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
