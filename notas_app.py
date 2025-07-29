elif aba == "Resultado final":
    st.header("Resultado Final")

    # Critérios de avaliação para o resultado final (inclui apresentação)
    criterios_final = [
        "Correspondência ao tema e seção temática",
        "Originalidade e contribuição",
        "Clareza do problema, objetivos e justificativa",
        "Adequação metodológica",
        "Clareza e coerência dos resultados",
        "Domínio do conteúdo apresentado",
        "Adequação ao tempo de apresentação"
    ]

    st.subheader("Avaliador(a) I - Apresentação")
    notas_final_i = {}
    for i, c in enumerate(criterios_final):
        notas_final_i[c] = st.number_input(f"{i+1}. {c} (Avaliador I)", min_value=0.0, max_value=10.0, step=0.1, value=8.9, key=f"final_i_{i}")

    media_ponderada_final_i = st.number_input("Média ponderada:", min_value=0.0, max_value=10.0, step=0.1, value=8.9, key="media_final_i")

    st.subheader("Avaliador(a) II - Apresentação")
    notas_final_ii = {}
    for i, c in enumerate(criterios_final):
        notas_final_ii[c] = st.number_input(f"{i+1}. {c} (Avaliador II)", min_value=0.0, max_value=10.0, step=0.1, value=8.8, key=f"final_ii_{i}")

    media_ponderada_final_ii = st.number_input("Média ponderada:", min_value=0.0, max_value=10.0, step=0.1, value=8.8, key="media_final_ii")

    nota_final_escrito = st.number_input("TRABALHO ESCRITO", min_value=0.0, max_value=10.0, step=0.1, value=8.7)
    nota_final_apresentacao = st.number_input("APRESENTAÇÃO ORAL", min_value=0.0, max_value=10.0, step=0.1, value=4.0)
    nota_geral_ponderada = st.number_input("NOTA GERAL", min_value=0.0, max_value=10.0, step=0.01, value=8.8, disabled=True)

    hora_encerramento = st.text_input("Hora da cerimônia de encerramento:", value="XXh")

    html_resultado_final = f"""
<!DOCTYPE html>
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
      padding: 20px;
    }}
    .container {{
      max-width: 600px;
      margin: auto;
      padding: 20px;
    }}
    p {{
      margin-bottom: 16px;
      text-align: justify;
    }}
    .box {{
      background-color: #f0f0f0;
      border-left: 4px solid #999999;
      padding: 16px;
      margin: 20px 0;
      border-radius: 4px;
      text-align: justify;
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
    /* Estilo para os cards de nota */
    .nota-card-container {{
      display: flex;
      justify-content: space-between;
      gap: 16px;
      margin-top: 20px;
      flex-wrap: wrap;
    }}
    .nota-card {{
      background-color: #ffffff;
      border: 1px solid #e0e0e0;
      padding: 16px;
      border-radius: 8px;
      box-shadow: 0 4px 8px rgba(0,0,0,0.1);
      text-align: center;
      flex: 1;
      min-width: 150px;
      transition: transform 0.2s;
    }}
    .nota-card:hover {{
      transform: translateY(-2px);
    }}
    .nota-card.general-note {{
      background-color: #dff0d8;
      border: 1px solid #5cb85c;
    }}
    .nota-label {{
      font-size: 0.9em;
      color: #555;
      display: block;
      margin-bottom: 8px;
      text-transform: uppercase;
    }}
    .nota-value {{
      font-size: 1.5em;
      color: #000;
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
        {''.join(f'<tr><td>{i+1}. {c}</td><td>{formatar_nota_br(notas_final_i[c])}</td></tr>' for i, c in enumerate(criterios_final))}
      </table>
      <p><strong>Média ponderada: {formatar_nota_br(media_ponderada_final_i)}</strong></p>
    </div>
    <div class="box">
      <p><strong>👤 Avaliador(a) II</strong></p>
      <table>
        <tr><th>Critério</th><th>Nota</th></tr>
        {''.join(f'<tr><td>{i+1}. {c}</td><td>{formatar_nota_br(notas_final_ii[c])}</td></tr>' for i, c in enumerate(criterios_final))}
      </table>
      <p><strong>Média ponderada: {formatar_nota_br(media_ponderada_final_ii)}</strong></p>
    </div>
    <div class="nota-card-container">
      <div class="nota-card">
        <span class="nota-label">TRABALHO ESCRITO</span>
        <span class="nota-value">{formatar_nota_br(nota_final_escrito)}</span>
      </div>
      <div class="nota-card">
        <span class="nota-label">APRESENTAÇÃO ORAL</span>
        <span class="nota-value">{formatar_nota_br(nota_final_apresentacao)}</span>
      </div>
      <div class="nota-card general-note">
        <span class="nota-label">NOTA GERAL</span>
        <span class="nota-value">{formatar_nota_br(nota_geral_ponderada)}</span>
      </div>
    </div>
    <p>
      Aproveitamos para convidá-los(as) a participar da <strong>cerimônia de encerramento</strong>, que será realizada amanhã, <strong>5 de setembro de 2025, às {hora_encerramento}</strong>, no auditório do SergipeTec.
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
</html>
"""
    st.code(html_resultado_final, language="html")
