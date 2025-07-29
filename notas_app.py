import streamlit as st

st.set_page_config(page_title="Gerador de Avaliação SEMPI", layout="centered")

st.title("📩 Gerador de Avaliação - VII SEMPI")

st.markdown("Preencha as notas abaixo para gerar o email em HTML com o resultado da avaliação.")

# Dados do participante
nome = st.text_input("Nome do(a) participante")

# Notas do Avaliador 1
st.subheader("👤 Avaliador(a) I")
notas_a1 = []
for i in range(1, 8):
    nota = st.number_input(f"Critério {i} - Avaliador(a) I", min_value=0.0, max_value=10.0, step=0.1, format="%.1f", key=f"a1_c{i}")
    notas_a1.append(nota)
media_a1 = round(sum(notas_a1) / len(notas_a1), 2)
st.markdown(f"**Média Avaliador(a) I:** {media_a1}")

# Notas do Avaliador 2
st.subheader("👤 Avaliador(a) II")
notas_a2 = []
for i in range(1, 8):
    nota = st.number_input(f"Critério {i} - Avaliador(a) II", min_value=0.0, max_value=10.0, step=0.1, format="%.1f", key=f"a2_c{i}")
    notas_a2.append(nota)
media_a2 = round(sum(notas_a2) / len(notas_a2), 2)
st.markdown(f"**Média Avaliador(a) II:** {media_a2}")

# Outras notas
nota_escrito = st.number_input("Nota Final do Trabalho Escrito", min_value=0.0, max_value=10.0, step=0.1, format="%.1f")
nota_oral = st.number_input("Nota Final da Apresentação Oral", min_value=0.0, max_value=10.0, step=0.1, format="%.1f")
nota_geral = round((nota_escrito + nota_oral) / 2, 2)

# Geração do HTML
if st.button("📤 Gerar HTML"):
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
        <tr><th>Critério</th><th>Nota</th></tr>""" + "".join(
        f"<tr><td>{i+1}. Critério</td><td>{nota:.1f}</td></tr>" for i, nota in enumerate(notas_a1)
    ) + f"""
      </table>
      <p><strong>Média ponderada do(a) Avaliador(a) I: {media_a1}</strong></p>
    </div>

    <div class="box">
      <p><strong>👤 Avaliador(a) II</strong></p>
      <table>
        <tr><th>Critério</th><th>Nota</th></tr>""" + "".join(
        f"<tr><td>{i+1}. Critério</td><td>{nota:.1f}</td></tr>" for i, nota in enumerate(notas_a2)
    ) + f"""
      </table>
      <p><strong>Média ponderada do(a) Avaliador(a) II: {media_a2}</strong></p>
    </div>

    <div class="nota-final">
      Nota final do trabalho escrito: <strong>{nota_escrito:.1f}</strong><br />
      Nota final da apresentação oral: <strong>{nota_oral:.1f}</strong><br />
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

    <p>Atenciosamente,</p>
    <p><strong>Comissão Organizadora da VII SEMPI</strong></p>
  </div>
</body>
</html>
"""
    st.success("✅ HTML gerado com sucesso!")
    st.code(html, language="html")
