import streamlit as st

# Função auxiliar para formatar notas no padrão brasileiro
def formatar_nota_br(nota, casas_decimais=1):
    if nota == int(nota):
        return str(int(nota)).replace('.', ',')
    else:
        return f"{nota:.{casas_decimais}f}".replace('.', ',')

# Função para calcular média ponderada
def calcular_media_ponderada(notas, pesos):
    """
    Calcula a média ponderada de uma lista de notas com seus respectivos pesos.
    Args:
        notas (list): Lista de notas.
        pesos (list): Lista de pesos correspondentes às notas.
    Returns:
        float: Média ponderada. Retorna 0.0 se não houver notas ou pesos.
    """
    if not notas or not pesos or len(notas) != len(pesos):
        return 0.0 # Retorna 0.0 ou levanta um erro, dependendo da necessidade
    soma_produtos = sum(nota * peso for nota, peso in zip(notas, pesos))
    soma_pesos = sum(pesos)
    return soma_produtos / soma_pesos if soma_pesos > 0 else 0.0

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
      <li>🎤 Domínio do conteúdo apresentado;</li>
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

    st.title("💻 Notificação interna Even3 (VII SEMPI)")

    abas = ["🚫 Desclassificação", "✅ Aprovação", "❌ Reprovação", "🔔 Lembretes", "🏆 Resultado final"]
    aba = st.sidebar.radio("Selecione a aba:", abas)

    if aba == "🚫 Desclassificação":
        st.header("Desclassificação")

        motivos = st.text_area(
            "Liste os motivos da desclassificação:",
            value="X/ Y/ Z"
        )
        motivos_lista = [m.strip() for m in motivos.split("/") if m.strip()]

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
      padding: 0 20px 20px 20px;
    }}
    .container {{
      max-width: 700px;
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
      Solicitamos, gentilmente, que as correções sejam realizadas e o trabalho corrigido seja ressubmetido no sistema até o dia
      <strong>19 de agosto de 2025</strong>.
    </p>

    <p>
      Permanecemos à disposição para quaisquer dúvidas ou esclarecimentos que se fizerem necessários.
    </p>
  </div>
</body>
</html>"""

        st.code(html_desclassificacao, language="html")

    elif aba == "✅ Aprovação":
        st.header("Aprovação")

        criterios_avaliacao_aprov_reprov = [
            ("Correspondência do trabalho ao tema do evento e à seção temática escolhida", 2),
            ("Originalidade e contribuição do trabalho na área da Propriedade Intelectual", 1),
            ("Definição clara do problema, dos objetivos e da justificativa do trabalho", 2),
            ("Adequação dos métodos à pesquisa e confiabilidade dos procedimentos apresentados", 2),
            ("Clareza, coerência e objetividade na apresentação e discussão dos resultados", 3)
        ]
        
        nomes_criterios_aprov_reprov = [c[0] for c in criterios_avaliacao_aprov_reprov]
        pesos_criterios_aprov_reprov = [c[1] for c in criterios_avaliacao_aprov_reprov]

        # Função para processar a entrada de notas
        def processar_notas(input_key, subheader_text, num_criterios):
            st.subheader(subheader_text)
            notas_input = st.text_input(
                f"Digite as {num_criterios} notas para cada critério, separadas por espaço:",
                value=" ".join(["0.0"] * num_criterios),
                key=input_key
            )
            
            notas_digitadas = []
            try:
                notas_digitadas = [float(n.strip().replace(',', '.')) for n in notas_input.split() if n.strip()]
            except ValueError:
                st.warning("Por favor, insira notas válidas (números).")
                return {}, 0.0, False

            if len(notas_digitadas) != num_criterios:
                st.warning(f"Por favor, insira exatamente {num_criterios} notas.")
                return {}, 0.0, False
            
            notas = {c: notas_digitadas[i] for i, c in enumerate(nomes_criterios_aprov_reprov)}
            media_ponderada = calcular_media_ponderada(list(notas.values()), pesos_criterios_aprov_reprov)
            st.info(f"Média ponderada: **{formatar_nota_br(media_ponderada, 2)}**")
            
            return notas, media_ponderada, True

        # Avaliador I
        notas_i, media_ponderada_i, valido_i = processar_notas("notas_aprov_i_input", "Avaliador(a) I", len(nomes_criterios_aprov_reprov))
        parecer_i = st.text_area("Parecer Avaliador(a) I", value='"Parecer."', key="aprov_parecer_i")

        # Avaliador II
        notas_ii, media_ponderada_ii, valido_ii = processar_notas("notas_aprov_ii_input", "Avaliador(a) II", len(nomes_criterios_aprov_reprov))
        parecer_ii = st.text_area("Parecer Avaliador(a) II", value='''"Parecer."''', key="aprov_parecer_ii")

        # Cálculo da Nota Final
        if valido_i and valido_ii:
            nota_final_aprovacao = (media_ponderada_i + media_ponderada_ii) / 2
        else:
            nota_final_aprovacao = 0.0
        st.metric("Nota final do trabalho:", formatar_nota_br(nota_final_aprovacao, 2))

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
      padding: 0 20px 20px 20px;
    }}
    .container {{
      max-width: 700px;
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
        {''.join(f'<tr><td>{i+1}. {c}</td><td>{formatar_nota_br(notas_i.get(c, 0.0))}</td></tr>' for i, c in enumerate(nomes_criterios_aprov_reprov))}
      </table>
      <p><strong>Média ponderada: {formatar_nota_br(media_ponderada_i, 2)}</strong></p>
      <p class="parecer">{parecer_i}</p>
    </div>

    <div class="box">
      <p><strong>👤 Avaliador(a) II</strong></p>
      <table>
        <tr>
          <th>Critério</th>
          <th>Nota</th>
        </tr>
        {''.join(f'<tr><td>{i+1}. {c}</td><td>{formatar_nota_br(notas_ii.get(c, 0.0))}</td></tr>' for i, c in enumerate(nomes_criterios_aprov_reprov))}
      </table>
      <p><strong>Média ponderada: {formatar_nota_br(media_ponderada_ii, 2)}</strong></p>
      <p class="parecer">{parecer_ii}</p>
    </div>

    <div class="nota-final">
      Nota final do trabalho: <strong>{formatar_nota_br(nota_final_aprovacao, 2)}</strong>
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

    elif aba == "❌ Reprovação":
        st.header("Reprovação")

        criterios_avaliacao_aprov_reprov = [
            ("Correspondência do trabalho ao tema do evento e à seção temática escolhida", 2),
            ("Originalidade e contribuição do trabalho na área da Propriedade Intelectual", 1),
            ("Definição clara do problema, dos objetivos e da justificativa do trabalho", 2),
            ("Adequação dos métodos à pesquisa e confiabilidade dos procedimentos apresentados", 2),
            ("Clareza, coerência e objetividade na apresentação e discussão dos resultados", 3)
        ]
        
        nomes_criterios_aprov_reprov = [c[0] for c in criterios_avaliacao_aprov_reprov]
        pesos_criterios_aprov_reprov = [c[1] for c in criterios_avaliacao_aprov_reprov]

        def processar_notas(input_key, subheader_text, num_criterios):
            st.subheader(subheader_text)
            notas_input = st.text_input(
                f"Digite as {num_criterios} notas para cada critério, separadas por espaço:",
                value=" ".join(["0.0"] * num_criterios),
                key=input_key
            )
            
            notas_digitadas = []
            try:
                notas_digitadas = [float(n.strip().replace(',', '.')) for n in notas_input.split() if n.strip()]
            except ValueError:
                st.warning("Por favor, insira notas válidas (números).")
                return {}, 0.0, False

            if len(notas_digitadas) != num_criterios:
                st.warning(f"Por favor, insira exatamente {num_criterios} notas.")
                return {}, 0.0, False
            
            notas = {c: notas_digitadas[i] for i, c in enumerate(nomes_criterios_aprov_reprov)}
            media_ponderada = calcular_media_ponderada(list(notas.values()), pesos_criterios_aprov_reprov)
            st.info(f"Média ponderada: **{formatar_nota_br(media_ponderada, 2)}**")
            
            return notas, media_ponderada, True
            
        # Avaliador I
        notas_i, media_ponderada_i, valido_i = processar_notas("notas_reprov_i_input", "Avaliador(a) I", len(nomes_criterios_aprov_reprov))
        parecer_i = st.text_area("Parecer Avaliador(a) I", value='"Parecer."', key="reprov_parecer_i")

        # Avaliador II
        notas_ii, media_ponderada_ii, valido_ii = processar_notas("notas_reprov_ii_input", "Avaliador(a) II", len(nomes_criterios_aprov_reprov))
        parecer_ii = st.text_area("Parecer Avaliador(a) II", value='"Parecer."', key="reprov_parecer_ii")

        # Cálculo da Nota Final
        if valido_i and valido_ii:
            nota_final_reprovacao = (media_ponderada_i + media_ponderada_ii) / 2
        else:
            nota_final_reprovacao = 0.0
        st.metric("Nota final do trabalho:", formatar_nota_br(nota_final_reprovacao, 2))

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
      padding: 0 20px 20px 20px;
    }}
    .container {{
      max-width: 700px;
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
        {''.join(f'<tr><td>{i+1}. {c}</td><td>{formatar_nota_br(notas_i.get(c, 0.0))}</td></tr>' for i, c in enumerate(nomes_criterios_aprov_reprov))}
      </table>
      <p><strong>Média ponderada: {formatar_nota_br(media_ponderada_i, 2)}</strong></p>
      <p class="parecer">{parecer_i}</p>
    </div>

    <div class="box">
      <p><strong>👤 Avaliador(a) II</strong></p>
      <table>
        <tr>
          <th>Critério</th>
          <th>Nota</th>
        </tr>
        {''.join(f'<tr><td>{i+1}. {c}</td><td>{formatar_nota_br(notas_ii.get(c, 0.0))}</td></tr>' for i, c in enumerate(nomes_criterios_aprov_reprov))}
      </table>
      <p><strong>Média ponderada: {formatar_nota_br(media_ponderada_ii, 2)}</strong></p>
      <p class="parecer">{parecer_ii}</p>
    </div>

    <div class="nota-final">
      Nota final do trabalho: <strong>{formatar_nota_br(nota_final_reprovacao, 2)}</strong>
    </div>

    <p>
      Permanecemos à disposição para quaisquer dúvidas ou esclarecimentos que se fizerem necessários.
    </p>
  </div>
</body>
</html>"""

        st.code(html_reprovacao, language="html")

    elif aba == "🔔 Lembretes":
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

    elif aba == "🏆 Resultado final":
        st.header("Resultado Final")

        criterios_avaliacao_final = [
            ("Correspondência do trabalho ao tema do evento e à seção temática escolhida", 1),
            ("Originalidade e contribuição do trabalho na área da Propriedade Intelectual", 1),
            ("Definição clara do problema, dos objetivos e da justificativa do trabalho", 1),
            ("Adequação dos métodos à pesquisa e confiabilidade dos procedimentos apresentados", 2),
            ("Clareza, coerência e objetividade na apresentação e discussão dos resultados", 2),
            ("Domínio do conteúdo apresentado", 2),
            ("Adequação ao tempo de apresentação", 1)
        ]

        nomes_criterios_final = [c[0] for c in criterios_avaliacao_final]
        pesos_criterios_final = [c[1] for c in criterios_avaliacao_final]
        
        def processar_notas(input_key, subheader_text, num_criterios):
            st.subheader(subheader_text)
            notas_input = st.text_input(
                f"Digite as {num_criterios} notas para cada critério, separadas por espaço:",
                value=" ".join(["0.0"] * num_criterios),
                key=input_key
            )
            
            notas_digitadas = []
            try:
                notas_digitadas = [float(n.strip().replace(',', '.')) for n in notas_input.split() if n.strip()]
            except ValueError:
                st.warning("Por favor, insira notas válidas (números).")
                return {}, 0.0, False

            if len(notas_digitadas) != num_criterios:
                st.warning(f"Por favor, insira exatamente {num_criterios} notas.")
                return {}, 0.0, False
            
            notas = {c: notas_digitadas[i] for i, c in enumerate(nomes_criterios_final)}
            media_ponderada = calcular_media_ponderada(list(notas.values()), pesos_criterios_final)
            st.info(f"Média ponderada: **{formatar_nota_br(media_ponderada, 2)}**")
            
            return notas, media_ponderada, True
            
        # Avaliador I
        notas_final_i, media_ponderada_final_i, valido_i = processar_notas("notas_final_i_input", "Avaliador(a) I - Apresentação", len(nomes_criterios_final))
        
        # Avaliador II
        notas_final_ii, media_ponderada_final_ii, valido_ii = processar_notas("notas_final_ii_input", "Avaliador(a) II - Apresentação", len(nomes_criterios_final))

        if valido_i and valido_ii:
            nota_final_apresentacao = (media_ponderada_final_i + media_ponderada_final_ii) / 2
        else:
            nota_final_apresentacao = 0.0
        st.metric("APRESENTAÇÃO ORAL:", formatar_nota_br(nota_final_apresentacao, 2))
        
        nota_final_escrito = st.number_input("TRABALHO ESCRITO:", min_value=0.0, max_value=10.0, step=0.1, value=0.0, key="nota_final_escrito_input")
        
        nota_geral_ponderada = calcular_media_ponderada(
            [nota_final_escrito, nota_final_apresentacao],
            [7, 3]
        )
        st.metric("NOTA GERAL:", formatar_nota_br(nota_geral_ponderada, 2))

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
      padding: 0 20px 20px 20px;
    }}
    .container {{
      max-width: 700px;
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
"""
