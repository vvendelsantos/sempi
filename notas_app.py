import streamlit as st

# [Seus templates HTML anteriores permanecem iguais...]

def main():
    st.set_page_config(page_title="Gerador de HTML SEMPI", layout="wide")

    st.title("Gerador de HTML SEMPI - 5 abas")

    abas = ["Desclassificação", "Aprovação", "Reprovação", "Lembretes", "Resultado final"]
    aba = st.sidebar.radio("Selecione a aba:", abas)

    if aba == "Desclassificação":
        # [Código da aba Desclassificação permanece igual...]
        pass

    elif aba == "Aprovação":
        # [Código da aba Aprovação permanece igual...]
        pass

    elif aba == "Reprovação":
        # [Código da aba Reprovação permanece igual...]
        pass

    elif aba == "Lembretes":
        # [Código da aba Lembretes permanece igual...]
        pass

    elif aba == "Resultado final":
        st.header("Resultado Final")
        
        # Adicione aqui os controles para a aba Resultado final
        html_resultado_final = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      color: #333333;
      background-color: #ffffff;
      margin: 0;
      padding: 20px;
    }
    .container {
      max-width: 700px;
      margin: auto;
    }
    .box {
      background-color: #f0f0f0;
      border-left: 4px solid #999999;
      padding: 16px;
      margin: 20px 0;
      border-radius: 4px;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 10px;
    }
    th, td {
      text-align: left;
      padding: 8px;
      border-bottom: 1px solid #ccc;
    }
    th {
      background-color: #e0e0e0;
    }
    .nota-final {
      background-color: #dff0d8;
      border-left: 4px solid #5cb85c;
      padding: 16px;
      margin-top: 20px;
      border-radius: 4px;
      font-weight: bold;
    }
    a {
      color: #0645ad;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
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
        <tr><td>1. Correspondência ao tema e seção temática</td><td>8,5</td></tr>
        <tr><td>2. Originalidade e contribuição</td><td>9,0</td></tr>
        <tr><td>3. Clareza do problema, objetivos e justificativa</td><td>8,0</td></tr>
        <tr><td>4. Adequação metodológica</td><td>9,5</td></tr>
        <tr><td>5. Clareza e coerência dos resultados</td><td>8,5</td></tr>
        <tr><td>6. Domínio do conteúdo apresentado</td><td>9,5</td></tr>
        <tr><td>7. Adequação ao tempo de apresentação</td><td>9,0</td></tr>
      </table>
      <p><strong>Média ponderada do(a) Avaliador(a) I: 8,9</strong></p>
    </div>

    <div class="box">
      <p><strong>👤 Avaliador(a) II</strong></p>
      <table>
        <tr><th>Critério</th><th>Nota</th></tr>
        <tr><td>1. Correspondência ao tema e seção temática</td><td>9,0</td></tr>
        <tr><td>2. Originalidade e contribuição</td><td>8,5</td></tr>
        <tr><td>3. Clareza do problema, objetivos e justificativa</td><td>8,5</td></tr>
        <tr><td>4. Adequação metodológica</td><td>9,0</td></tr>
        <tr><td>5. Clareza e coerência dos resultados</td><td>9,0</td></tr>
        <tr><td>6. Domínio do conteúdo apresentado</td><td>8,5</td></tr>
        <tr><td>7. Adequação ao tempo de apresentação</td><td>9,5</td></tr>
      </table>
      <p><strong>Média ponderada do(a) Avaliador(a) II: 8,8</strong></p>
    </div>

    <div class="nota-final">
      Nota final do trabalho escrito: <strong>8,7</strong><br />
      Nota final da apresentação oral: <strong>9,0</strong><br />
      Nota geral (média ponderada): <strong>8,85</strong>
    </div>

    <p>
      Aproveitamos para convidá-los(as) a participar da <strong>cerimônia de encerramento</strong>, que será realizada amanhã, <strong>5 de setembro de 2025, às XXh</strong>, no auditório do SergipeTec.
      Durante a solenidade, serão entregues os <strong>Certificados de Menção Honrosa</strong> aos três trabalhos com as maiores notas gerais em cada seção temática. Também será concedido o <strong>Certificado de Reconhecimento de "Melhor Trabalho"</strong> ao(à) autor(a) do trabalho que obteve a maior nota geral do evento.
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
        
        st.code(html_resultado_final, language="html")

if __name__ == "__main__":
    main()
