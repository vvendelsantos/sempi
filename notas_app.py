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
    /* Novo estilo para as notas - fundo simples */
    .notas-container {{
      display: flex;
      justify-content: space-between;
      gap: 8px;
      margin-top: 20px;
      background-color: #f9f9f9;
      padding: 12px;
      border-radius: 4px;
      border: 1px solid #ddd;
    }}
    .nota-item {{
      text-align: center;
      flex-grow: 1;
    }}
    .nota-label {{
      font-size: 0.85em;
      color: #555;
      display: block;
      margin-bottom: 3px;
    }}
    .nota-value {{
      font-size: 1.3em;
      color: #000;
      font-weight: bold;
    }}
    .nota-geral {{
      color: #1a5276;
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

    <div class="notas-container">
      <div class="nota-item">
        <span class="nota-label">TRABALHO ESCRITO</span>
        <span class="nota-value">{formatar_nota_br(nota_final_escrito)}</span>
      </div>
      <div class="nota-item">
        <span class="nota-label">APRESENTAÇÃO ORAL</span>
        <span class="nota-value">{formatar_nota_br(nota_final_apresentacao)}</span>
      </div>
      <div class="nota-item">
        <span class="nota-label">NOTA GERAL</span>
        <span class="nota-value nota-geral">{formatar_nota_br(nota_geral_ponderada)}</span>
      </div>
    </div>

    <p>
      Aproveitamos para convidá-los(as) a participar da <strong>cerimônia de encerramento</strong>, que será realizada amanhã, <strong>5 de setembro de 2025, às {hora_encerramento}</strong>, no auditório do SergipeTec.
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
</html>
"""
