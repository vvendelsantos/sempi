import streamlit as st

def gerar_html(dados):
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
      A Comissão Organizadora da <strong>VII Semana Acadêmica da Propriedade Intelectual (VII SEMPI)</strong>
      os(as) parabeniza pela apresentação do trabalho. Abaixo, apresentamos as avaliações realizadas
      pelos membros do Comitê Científico:
    </p>

    <div class="box">
      <p><strong>👤 Avaliador(a) I</strong></p>
      <table>
        <tr><th>Critério</th><th>Nota</th></tr>
        <tr><td>1. Correspondência ao tema e seção temática</td><td>{dados['C1_A1']}</td></tr>
        <tr><td>2. Originalidade e contribuição</td><td>{dados['C2_A1']}</td></tr>
        <tr><td>3. Clareza do problema, objetivos e justificativa</td><td>{dados['C3_A1']}</td></tr>
        <tr><td>4. Adequação metodológica</td><td>{dados['C4_A1']}</td></tr>
        <tr><td>5. Clareza e coerência dos resultados</td><td>{dados['C5_A1']}</td></tr>
        <tr><td>6. Domínio do conteúdo apresentado</td><td>{dados['C6_A1']}</td></tr>
        <tr><td>7. Adequação ao tempo de apresentação</td><td>{dados['C7_A1']}</td></tr>
      </table>
      <p><strong>Média ponderada do(a) Avaliador(a) I: {dados['Media_A1']}</strong></p>
    </div>

    <div class="box">
      <p><strong>👤 Avaliador(a) II</strong></p>
      <table>
        <tr><th>Critério</th><th>Nota</th></tr>
        <tr><td>1. Correspondência ao tema e seção temática</td><td>{dados['C1_A2']}</td></tr>
        <tr><td>2. Originalidade e contribuição</td><td>{dados['C2_A2']}</td></tr>
        <tr><td>3. Clareza do problema, objetivos e justificativa</td><td>{dados['C3_A2']}</td></tr>
        <tr><td>4. Adequação metodológica</td><td>{dados['C4_A2']}</td></tr>
        <tr><td>5. Clareza e coerência dos resultados</td><td>{dados['C5_A2']}</td></tr>
        <tr><td>6. Domínio do conteúdo apresentado</td><td>{dados['C6_A2']}</td></tr>
        <tr><td>7. Adequação ao tempo de apresentação</td><td>{dados['C7_A2']}</td></tr>
      </table>
      <p><strong>Média ponderada do(a) Avaliador(a) II: {dados['Media_A2']}</strong></p>
    </div>

    <div class="nota-final">
      Nota final do trabalho escrito: <strong>{dados['Nota_Final_Escrito']}</strong><br />
      Nota final da apresentação oral: <strong>{dados['Nota_Final_Oral']}</strong><br />
      Nota geral (média ponderada): <strong>{dados['Nota_Geral']}</strong>
    </div>

    <p>Aproveitamos para convidá-los(as) para a cerimônia de encerramento!</p>
  </div>
</body>
</html>"""
    return html

def app():
    st.title("Gerador de E-mail HTML - VII SEMPI")

    with st.form("formulario"):
        campos = [
            "C1_A1", "C2_A1", "C3_A1", "C4_A1", "C5_A1", "C6_A1", "C7_A1", "Media_A1",
            "C1_A2", "C2_A2", "C3_A2", "C4_A2", "C5_A2", "C6_A2", "C7_A2", "Media_A2",
            "Nota_Final_Escrito", "Nota_Final_Oral", "Nota_Geral"
        ]
        dados = {}
        for campo in campos:
            dados[campo] = st.text_input(f"{campo}:")

        submitted = st.form_submit_button("Gerar HTML")

    if submitted:
        html_resultado = gerar_html(dados)
        st.subheader("HTML Gerado")
        st.code(html_resultado, language="html")

if __name__ == "__main__":
    app()

