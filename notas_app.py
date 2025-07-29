import streamlit as st

# HTML base para os lembretes (com placeholders para minutos e textos)
LEMBRETE_ENVIO_HTML = """
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
    <p>Prezados(as) autores(as),</p>

    <p>Esperamos que esta mensagem os(as) encontre bem.</p>

    <p>
      A Comissão Organizadora da <strong>VII Semana Acadêmica da Propriedade Intelectual (VII SEMPI)</strong> relembra que todos os trabalhos aprovados deverão ser apresentados em sessão pública e avaliados por membros do Comitê Científico.
    </p>

    <p>
      {texto_envio_arquivo}
    </p>

    <div class="highlight">
      Se o autor principal não for apresentar o trabalho, seja por impossibilidade de comparecimento à sessão ou por outra razão, deverá designar um coautor para realizar a apresentação, respeitando o prazo estipulado. O coautor designado deverá, obrigatoriamente, estar inscrito no evento. Ressalta-se, porém, que os demais coautores que não participarão do evento, seja de forma presencial ou on-line, não precisam estar inscritos, ainda que seus nomes constem no trabalho. A alteração deverá ser comunicada à Comissão Organizadora no e-mail <a href="mailto:submissoes.sempi@gmail.com">submissoes.sempi@gmail.com</a> até <strong>29 de agosto de 2025</strong>.
    </div>

    <p>
      A ordem das apresentações, tanto presenciais quanto on-line, seguirá a programação previamente divulgada em nossos canais oficiais, salvo em casos excepcionais devidamente justificados. Autores que submeteram mais de um resumo expandido, especialmente em sessões temáticas diferentes, terão suas apresentações organizadas de forma a evitar conflitos de horário.
    </p>

    <p>
      O modelo editável está disponível no site do evento: <br />
      <a href="https://www.even3.com.br/vii-semana-academica-da-propriedade-intelectual-594540/" target="_blank" rel="noopener noreferrer">
        https://www.even3.com.br/vii-semana-academica-da-propriedade-intelectual-594540/
      </a>.
      Embora não haja limite de quantidade de slides, é obrigatório manter integralmente a formatação original (estilo, tamanho da fonte e cores).
    </p>

    <p>
      Permanecemos à disposição para quaisquer dúvidas ou esclarecimentos que se fizerem necessários.
    </p>
  </div>
</body>
</html>
"""

LEMBRETE_APRESENTACAO_HTML = """
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
</html>
"""

def main():
    st.set_page_config(page_title="Gerador de HTML SEMPI", layout="wide")

    st.title("Gerador de HTML SEMPI - 5 abas")

    abas = ["Desclassificação", "Aprovação", "Reprovação", "Lembretes", "Resultado final"]
    aba = st.sidebar.radio("Selecione a aba:", abas)

    if aba == "Desclassificação":
        # Código simples fixo, pode até fazer editar motivos
        st.header("Desclassificação")

        motivos = st.text_area(
            "Liste os motivos da desclassificação, separados por vírgula:",
            value="X, Y, Z"
        )
        motivos_lista = [m.strip() for m in motivos.split(",") if m.strip()]

        html_desclassificacao = f"""<!DOCTYPE html>
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
        {"".join(f"<li>{m}</li>" for m in motivos_lista)}
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

        st.code(html_desclassificacao, language="html")

    elif aba == "Aprovação":
        st.header("Aprovação")

        # Notas Avaliador I
        st.subheader("Notas Avaliador(a) I")
        notas_i = {}
        criterios_i = [
            "Correspondência ao tema e seção temática",
            "Originalidade e contribuição",
            "Clareza do problema, objetivos e justificativa",
            "Adequação metodológica",
            "Clareza e coerência dos resultados"
        ]
        for c in criterios_i:
            notas_i[c] = st.number_input(f"{c} (Avaliador I)", min_value=0.0, max_value=10.0, step=0.1, value=8.5)

        media_i = sum(notas_i.values()) / len(notas_i)

        parecer_i = st.text_area("Parecer Avaliador(a) I", value='"O trabalho apresenta boa estrutura e metodologia consistente. A proposta é pertinente e contribui para o debate sobre Propriedade Intelectual e Sustentabilidade."')

        # Notas Avaliador II
        st.subheader("Notas Avaliador(a) II")
        notas_ii = {}
        criterios_ii = [
            "Correspondência ao tema e seção temática",
            "Originalidade e contribuição",
            "Clareza do problema, objetivos e justificativa",
            "Adequação metodológica",
            "Clareza e coerência dos resultados"
        ]
        for c in criterios_ii:
            notas_ii[c] = st.number_input(f"{c} (Avaliador II)", min_value=0.0, max_value=10.0, step=0.1, value=8.5)

        media_ii = sum(notas_ii.values()) / len(notas_ii)

        parecer_ii = st.text_area("Parecer Avaliador(a) II", value='''"Texto claro, bem estruturado e alinhado com os objetivos do evento. Recomenda-se apenas uma revisão final para uniformização da escrita."''')

        nota_final = (media_i + media_ii) / 2

        html_aprovacao = f"""<!DOCTYPE html>
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
        {''.join(f'<tr><td>{c}</td><td>{notas_i[c]:.1f}</td></tr>' for c in criterios_i)}
      </table>
      <p><strong>Média ponderada do(a) Avaliador(a) I: {media_i:.1f}</strong></p>
      <p class="parecer">{parecer_i}</p>
    </div>

    <div class="box">
      <p><strong>👤 Avaliador(a) II</strong></p>
      <table>
        <tr>
          <th>Critério</th>
          <th>Nota</th>
        </tr>
        {''.join(f'<tr><td>{c}</td><td>{notas_ii[c]:.1f}</td></tr>' for c in criterios_ii)}
      </table>
      <p><strong>Média ponderada do(a) Avaliador(a) II: {media_ii:.1f}</strong></p>
      <p class="parecer">{parecer_ii}</p>
    </div>

    <div class="nota-final">
      Nota final do trabalho: <strong>{nota_final:.2f}</strong>
    </div>

    <p>
      As orientações para a elaboração e o envio do arquivo da apresentação estão disponíveis no site do evento:<br />
      <a href="https://www.even3.com.br/vii-semana-academica-da-propriedade-intelectual-594540/" target="_blank">
        https://www.even3.com.br/vii-semana-academica-da-propriedade-intelectual-594540/
      </a>
    </p>

    <p>
      Permanecemos à disposição para quaisquer dúvidas ou esclarecimentos que se fizerem necessários.
    </p>
  </div>
</body>
</html>"""

        st.code(html_aprovacao, language="html")

    elif aba == "Reprovação":
        st.header("Reprovação")

        # Notas Avaliador I
        st.subheader("Notas Avaliador(a) I")
        notas_i = {}
        criterios_i = [
            "Correspondência ao tema e seção temática",
            "Originalidade e contribuição",
            "Clareza do problema, objetivos e justificativa",
            "Adequação metodológica",
            "Clareza e coerência dos resultados"
        ]
        for c in criterios_i:
            notas_i[c] = st.number_input(f"{c} (Avaliador I)", min_value=0.0, max_value=10.0, step=0.1, value=6.5)

        media_i = sum(notas_i.values()) / len(notas_i)

        parecer_i = st.text_area("Parecer Avaliador(a) I", value='"O trabalho apresenta pontos que precisam ser aprimorados para melhor atender aos critérios do evento."')

        # Notas Avaliador II
        st.subheader("Notas Avaliador(a) II")
        notas_ii = {}
        criterios_ii = [
            "Correspondência ao tema e seção temática",
            "Originalidade e contribuição",
            "Clareza do problema, objetivos e justificativa",
            "Adequação metodológica",
            "Clareza e coerência dos resultados"
        ]
        for c in criterios_ii:
            notas_ii[c] = st.number_input(f"{c} (Avaliador II)", min_value=0.0, max_value=10.0, step=0.1, value=6.5)

        media_ii = sum(notas_ii.values()) / len(notas_ii)

        parecer_ii = st.text_area("Parecer Avaliador(a) II", value='"Recomenda-se revisão e aprimoramento do conteúdo para futuras submissões."')

        nota_final = (media_i + media_ii) / 2

        html_reprovacao = f"""<!DOCTYPE html>
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
      background-color: #f8d7da;
      border-left: 4px solid #dc3545;
      padding: 16px;
      margin-top: 20px;
      border-radius: 4px;
      font-weight: bold;
      color: #721c24;
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
      Informamos que o seu resumo expandido <strong>não foi aprovado</strong> para apresentação oral na
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
        {''.join(f'<tr><td>{c}</td><td>{notas_i[c]:.1f}</td></tr>' for c in criterios_i)}
      </table>
      <p><strong>Média ponderada do(a) Avaliador(a) I: {media_i:.1f}</strong></p>
      <p class="parecer">{parecer_i}</p>
    </div>

    <div class="box">
      <p><strong>👤 Avaliador(a) II</strong></p>
      <table>
        <tr>
          <th>Critério</th>
          <th>Nota</th>
        </tr>
        {''.join(f'<tr><td>{c}</td><td>{notas_ii[c]:.1f}</td></tr>' for c in criterios_ii)}
      </table>
      <p><strong>Média ponderada do(a) Avaliador(a) II: {media_ii:.1f}</strong></p>
      <p class="parecer">{parecer_ii}</p>
    </div>

    <div class="nota-final">
      Nota final do trabalho: <strong>{nota_final:.2f}</strong>
    </div>

    <p>
      Agradecemos seu interesse em participar da VII SEMPI e esperamos contar com sua presença em futuras edições.
    </p>

    <p>
      Permanecemos à disposição para quaisquer dúvidas ou esclarecimentos que se fizerem necessários.
    </p>
  </div>
</body>
</html>"""

        st.code(html_reprovacao, language="html")

    elif aba == "Lembretes":
        st.header("Lembretes")

        # Texto para envio de arquivo
        texto_envio_default = (
            "Para tanto, solicitamos que o arquivo de apresentação seja enviado até o dia "
            "<strong>29 de agosto de 2025</strong>, em formato PDF, por meio da Área do Participante. "
            "Para realizar o envio, acesse a plataforma com seu login e senha, clique no menu “Submissões”, "
            "selecione o trabalho correspondente, clique em “Editar” e anexe o arquivo no campo indicado. "
            "Após o envio, certifique-se de salvar as alterações."
        )

        texto_envio_arquivo = st.text_area(
            "Texto do lembrete para envio de arquivos (HTML permitido):",
            value=texto_envio_default,
            height=150
        )

        tempo_apresentacao = st.number_input("Tempo para exposição do trabalho (minutos)", min_value=1, max_value=60, value=15)
        tempo_arguicao = st.number_input("Tempo para arguição/comentários (minutos)", min_value=0, max_value=30, value=5)

        # Renderiza o HTML completo concatenando os dois blocos
        html_envio = LEMBRETE_ENVIO_HTML.format(texto_envio_arquivo=texto_envio_arquivo)
        html_apresentacao = LEMBRETE_APRESENTACAO_HTML.format(
            tempo_apresentacao=tempo_apresentacao,
            tempo_arguicao=tempo_arguicao
        )

        st.markdown("### Lembrete: Envio de arquivos")
        st.markdown(html_envio, unsafe_allow_html=True)

        st.markdown("---")

        st.markdown("### Lembrete: Apresentação oral")
        st.markdown(html_apresentacao, unsafe_allow_html=True)

        st.markdown("---")

        st.subheader("HTML completo combinado dos lembretes")
        html_completo = html_envio.replace("</body>", "")\
            .replace("</html>", "") + html_apresentacao.split("<body>")[1]
        st.code(html_completo, language="html")

    elif aba == "Resultado final":
        st.header("Resultado final")

        st.text_area("Texto do resultado final (sem parecer):", height=200, value="""
Prezados(as),

Esperamos que esta mensagem os(as) encontre bem.

Informamos que o trabalho foi avaliado e a decisão final está disponível.

Permanecemos à disposição para quaisquer dúvidas ou esclarecimentos que se fizerem necessários.
        """.strip())

        # Você pode adicionar aqui mais inputs para editar se quiser

        # Exemplo HTML fixo básico
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
  </style>
</head>
<body>
  <div>
    <p>Prezados(as),</p>

    <p>Esperamos que esta mensagem os(as) encontre bem.</p>

    <p>
      Informamos que o trabalho foi avaliado e a decisão final está disponível.
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
