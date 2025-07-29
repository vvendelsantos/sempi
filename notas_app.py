import streamlit as st

# Função auxiliar para formatar notas no padrão brasileiro
def formatar_nota_br(nota):
    if nota == int(nota):
        return str(int(nota)).replace('.', ',') # Garante que 10.0 vira "10", 3.0 vira "3"
    else:
        return f"{nota:.1f}".replace('.', ',') # Formata para uma casa decimal e troca ponto por vírgula

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
      text-align: justify;
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
      text-align: justify;
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
      🔗 <a href="https://www.even3.com.br/vii-semana-academica-da-propriedade-intelectual-594540/" target="_blank" rel="noopener noreferrer">
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
      text-align: justify;
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
      text-align: justify;
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
      🔗 <a href="https://www.even3.com.br/vii-semana-academica-da-propriedade-intelectual-594540/" target="_blank" rel="noopener noreferrer">
        https://www.even3.com.br/vii-semana-academica-da-propriedade-intelectual-594540/
      </a>
    </p>

    <div class="highlight">
      <p style="text-align: left;"><strong>⚠️ Orientações importantes:</strong></p>
      <ul style="margin-top: 0; padding-left: 20px;">
        <li style="text-align: left;">Autores que apresentarão seus trabalhos presencialmente devem comparecer ao local da sessão com, no mínimo, <strong>20 minutos de antecedência</strong>.</li>
        <li style="text-align: left;">Essa orientação também se aplica aos participantes com apresentação on-line autorizada, mediante justificativa formal.</li>
        <li style="text-align: left;"><strong>Não serão permitidas correções ou substituições</strong> do arquivo de apresentação durante o evento.</li>
      </ul>
    </div>

    <p>
      Cada apresentador(a) disporá de até <strong>{tempo_apresentacao} minutos</strong> para a exposição do trabalho, seguidos de até <strong>{tempo_arguicao} minutos</strong> para arguição e/ou comentários dos(as) avaliadores(as).
    </p>

    <p>
      Cada trabalho será avaliado por, no mínimo, dois pareceristas. Os critérios de avaliação da apresentação oral seguem os mesmos adotados para o trabalho escrito, com o acréscimo dos seguintes itens:
    </p>

    <ul style="padding-left: 20px; text-align: justify;">
      <li>🎤  do conteúdo apresentado;</li>
      <li>⏳ Adequação ao tempo de apresentação.</li>
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
    ol {{
      padding-left: 20px;
      margin: 0;
      text-align: justify;
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
      Solicitamos, gentilmente, que as correções sejam realizadas e o trabalho corrigido seja ressubmitted no sistema até o dia
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

        # Critérios de avaliação
        criterios_avaliacao = [
            "Correspondência ao tema e seção temática",
            "Originalidade e contribuição",
            "Clareza do problema, objetivos e justificativa",
            "Adequação metodológica",
            "Clareza e coerência dos resultados"
        ]

        # Notas Avaliador I
        st.subheader("Avaliador(a) I")
        notas_i = {}
        for i, c in enumerate(criterios_avaliacao):
            notas_i[c] = st.number_input(f"{i+1}. {c}", min_value=0.0, max_value=10.0, step=0.1, value=8.5, key=f"aprov_i_{i}")

        # Campo para inserir a média ponderada do avaliador I
        media_ponderada_i = st.number_input("Média ponderada:", min_value=0.0, max_value=10.0, step=0.1, value=8.7, key="media_aprov_i")
        parecer_i = st.text_area("Parecer Avaliador(a) I", value='"O trabalho apresenta boa estrutura e metodologia consistente. A proposta é pertinente e contribui para o debate sobre Propriedade Intelectual e Sustentabilidade."', key="aprov_parecer_i")

        # Notas Avaliador II
        st.subheader("Avaliador(a) II")
        notas_ii = {}
        for i, c in enumerate(criterios_avaliacao):
            notas_ii[c] = st.number_input(f"{i+1}. {c}", min_value=0.0, max_value=10.0, step=0.1, value=8.5, key=f"aprov_ii_{i}")

        # Campo para inserir a média ponderada do avaliador II
        media_ponderada_ii = st.number_input("Média ponderada:", min_value=0.0, max_value=10.0, step=0.1, value=8.8, key="media_aprov_ii")
        parecer_ii = st.text_area("Parecer Avaliador(a) II", value='''"Texto claro, bem estruturado e alinhado com os objetivos do evento. Recomenda-se apenas uma revisão final para uniformização da escrita."''', key="aprov_parecer_ii")

        # Campo para inserir a Nota Final do trabalho
        nota_final_aprovacao = st.number_input("Nota final do trabalho:", min_value=0.0, max_value=10.0, step=0.01, value=8.75, key="nota_final_aprovacao")


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
    .nota-final {{
      background-color: #dff0d8;
      border-left: 4px solid #5cb85c;
      padding: 16px;
      margin-top: 20px;
      border-radius: 4px;
      font-weight: bold;
      text-align: justify;
    }}
    .parecer {{
      margin-top: 10px;
      font-style: italic;
      color: #444;
      text-align: justify;
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
        {''.join(f'<tr><td>{i+1}. {c}</td><td>{formatar_nota_br(notas_i[c])}</td></tr>' for i, c in enumerate(criterios_avaliacao))}
      </table>
      <p><strong>Média ponderada: {formatar_nota_br(media_ponderada_i)}</strong></p>
      <p class="parecer">{parecer_i}</p>
    </div>

    <div class="box">
      <p><strong>👤 Avaliador(a) II</strong></p>
      <table>
        <tr>
          <th>Critério</th>
          <th>Nota</th>
        </tr>
        {''.join(f'<tr><td>{i+1}. {c}</td><td>{formatar_nota_br(notas_ii[c])}</td></tr>' for i, c in enumerate(criterios_avaliacao))}
      </table>
      <p><strong>Média ponderada: {formatar_nota_br(media_ponderada_ii)}</strong></p>
      <p class="parecer">{parecer_ii}</p>
    </div>

    <div class="nota-final">
      Nota final do trabalho: <strong>{formatar_nota_br(nota_final_aprovacao)}</strong>
    </div>

    <p>
      As orientações para a elaboração e o envio do arquivo da apresentação estão disponíveis no site do evento:<br />
      🔗 <a href="https://www.even3.com.br/vii-semana-academica-da-propriedade-intelectual-594540/" target="_blank">
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

        # Critérios de avaliação
        criterios_avaliacao = [
            "Correspondência ao tema e seção temática",
            "Originalidade e contribuição",
            "Clareza do problema, objetivos e justificativa",
            "Adequação metodológica",
            "Clareza e coerência dos resultados"
        ]

        # Notas Avaliador I
        st.subheader("Avaliador(a) I")
        notas_i = {}
        for i, c in enumerate(criterios_avaliacao):
            notas_i[c] = st.number_input(f"{i+1}. {c}", min_value=0.0, max_value=10.0, step=0.1, value=6.5, key=f"reprov_i_{i}")

        # Campo para inserir a média ponderada do avaliador I
        media_ponderada_i = st.number_input("Média ponderada", min_value=0.0, max_value=10.0, step=0.1, value=6.7, key="media_reprov_i")
        parecer_i = st.text_area("Parecer Avaliador(a) I", value='"O trabalho apresenta pontos que precisam ser aprimorados para melhor atender aos critérios do evento."', key="reprov_parecer_i")

        # Notas Avaliador II
        st.subheader("Avaliador(a) II")
        notas_ii = {}
        for i, c in enumerate(criterios_avaliacao):
            notas_ii[c] = st.number_input(f"{i+1}. {c}", min_value=0.0, max_value=10.0, step=0.1, value=6.5, key=f"reprov_ii_{i}")

        # Campo para inserir a média ponderada do avaliador II
        media_ponderada_ii = st.number_input("Média ponderada:", min_value=0.0, max_value=10.0, step=0.1, value=6.8, key="media_reprov_ii")
        parecer_ii = st.text_area("Parecer Avaliador(a) II", value='"Recomenda-se revisão e aprimoramento do conteúdo para futuras submissões."', key="reprov_parecer_ii")

        # Campo para inserir a Nota Final do trabalho
        nota_final_reprovacao = st.number_input("Nota final do trabalho:", min_value=0.0, max_value=10.0, step=0.01, value=6.75, key="nota_final_reprovacao")


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
      color: #333333;
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
    .nota-final {{
      background-color: #f8d7da;
      border-left: 4px solid #d9534f;
      padding: 16px;
      margin-top: 20px;
      border-radius: 4px;
      font-weight: bold;
      color: #721c24;
      text-align: justify;
    }}
    .parecer {{
      margin-top: 10px;
      font-style: italic;
      color: #444;
      text-align: justify;
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
      Informamos que o seu resumo expandido foi <strong>reprovado</strong> para apresentação na
      <strong>VII Semana Acadêmica da Propriedade Intelectual (VII SEMPI)</strong>.
    </p>

    <p>
      Abaixo, apresentamos as avaliações realizadas pelos membros do Comitê Científico:
    </p>

    <div class="box">
      <p><strong>👤 Avaliador(a) I</strong></p>
      <table>
        <tr>
          <th>Critério</th>
          <th>Nota</th>
        </tr>
        {''.join(f'<tr><td>{i+1}. {c}</td><td>{formatar_nota_br(notas_i[c])}</td></tr>' for i, c in enumerate(criterios_avaliacao))}
      </table>
      <p><strong>Média ponderada: {formatar_nota_br(media_ponderada_i)}</strong></p>
      <p class="parecer">{parecer_i}</p>
    </div>

    <div class="box">
      <p><strong>👤 Avaliador(a) II</strong></p>
      <table>
        <tr>
          <th>Critério</th>
          <th>Nota</th>
        </tr>
        {''.join(f'<tr><td>{i+1}. {c}</td><td>{formatar_nota_br(notas_ii[c])}</td></tr>' for i, c in enumerate(criterios_avaliacao))}
      </table>
      <p><strong>Média ponderada: {formatar_nota_br(media_ponderada_ii)}</strong></p>
      <p class="parecer">{parecer_ii}</p>
    </div>

    <div class="nota-final">
      Nota final do trabalho: <strong>{formatar_nota_br(nota_final_reprovacao)}</strong>
    </div>

    <p>
      Permanecemos à disposição para quaisquer dúvidas ou esclarecimentos que se fizerem necessários.
    </p>
  </div>
</body>
</html>"""

        st.code(html_reprovacao, language="html")

    elif aba == "Lembretes":
        st.header("Lembretes")

        st.markdown("### Texto para envio do arquivo da apresentação")
        texto_envio_arquivo = st.text_area("Digite o texto para o lembrete de envio do arquivo:", value="Para tanto, solicitamos que o arquivo de apresentação seja enviado até o dia <strong>29 de agosto de 2025</strong>, em formato PDF, por meio da Área do Participante. Para realizar o envio, acesse a plataforma com seu login e senha, clique no menu “Submissões”, selecione o trabalho correspondente, clique em “Editar” e anexe o arquivo no campo indicado. Após o envio, certifique-se de salvar as alterações.")

        st.markdown("### Tempos para apresentação")
        tempo_apresentacao = st.number_input("Tempo para apresentação (minutos)", min_value=1, max_value=60, value=10)
        tempo_arguicao = st.number_input("Tempo para arguição (minutos)", min_value=1, max_value=30, value=5)

        html_lembrete_envio = LEMBRETE_ENVIO_HTML.format(texto_envio_arquivo=texto_envio_arquivo)
        html_lembrete_apresentacao = LEMBRETE_APRESENTACAO_HTML.format(tempo_apresentacao=tempo_apresentacao, tempo_arguicao=tempo_arguicao)

        st.subheader("Lembrete para envio do arquivo")
        st.code(html_lembrete_envio, language="html")

        st.subheader("Lembrete para apresentação")
        st.code(html_lembrete_apresentacao, language="html")

    elif aba == "Resultado final":
        st.header("Resultado Final")

        # Critérios de avaliação para o resultado final (inclui apresentação)
        criterios_final = [
            "Correspondência ao tema e seção temática",
            "Originalidade e contribuição",
            "Clareza do problema, objetivos e justificativa",
            "Adequação metodológica",
            "Clareza e coerência dos resultados",
            "Domínio do conteúdo apresentado", # Emoji adicionado aqui
            "Adequação ao tempo de apresentação" # Emoji adicionado aqui
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
        nota_final_apresentacao = st.number_input("APRESENTAÇÃO ORAL", min_value=0.0, max_value=10.0, step=0.1, value=9.0)
        nota_geral_ponderada = st.number_input("NOTA GERAL", min_value=0.0, max_value=10.0, step=0.01, value=8.85, disabled=True) # Desabilitado para ser calculado

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
    /* Estilo para os "botões" de nota */
    .nota-button-container {{
      display: flex;
      justify-content: space-between;
      gap: 8px;
      margin-top: 20px;
    }}
    .nota-button {{
      background-color: #e6f7ff;
      border: 1px solid #91d5ff;
      padding: 8px 10px;
      border-radius: 6px;
      font-weight: bold;
      text-align: center;
      flex-grow: 1;
      box-shadow: 1px 1px 3px rgba(0,0,0,0.1);
      &.general-note {{
        background-color: #dff0d8;
        border: 1px solid #5cb85c;
      }}
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

    <div class="nota-button-container">
      <div class="nota-button">
        <span class="nota-label">Nota final do trabalho escrito:</span>
        <span class="nota-value"><strong>{formatar_nota_br(nota_final_escrito)}</strong></span>
      </div>
      <div class="nota-button">
        <span class="nota-label">Nota final da apresentação oral:</span>
        <span class="nota-value"><strong>{formatar_nota_br(nota_final_apresentacao)}</strong></span>
      </div>
      <div class="nota-button general-note">
        <span class="nota-label">Nota geral (média ponderada):</span>
        <span class="nota-value"><strong>{formatar_nota_br(nota_geral_ponderada)}</strong></span>
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


if __name__ == "__main__":
    main()
