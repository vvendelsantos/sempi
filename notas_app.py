import streamlit as st

# Função auxiliar para formatar notas no padrão brasileiro
def formatar_nota_br(nota, casas_decimais=1):
    # Converte a nota para string com o número de casas decimais desejado
    # e depois substitui o ponto pela vírgula.
    nota_str = f"{nota:.{casas_decimais}f}".replace('.', ',')
    
    # Remove o zero extra se a nota for, por exemplo, '8,0' -> '8,' -> '8' (se for o caso)
    # ou '8,10' -> '8,1'
    if ',' in nota_str:
        # Divide a string em parte inteira e parte decimal
        partes = nota_str.split(',')
        if len(partes) > 1:
            decimal_parte = partes[1]
            # Se a parte decimal for '0' (ex: 8,0), remove ',0' para exibir '8'
            if decimal_parte == '0':
                return partes[0]
            # Se a parte decimal terminar em '0' (ex: 8,10), remove o zero extra para exibir '8,1'
            elif decimal_parte.endswith('0') and len(decimal_parte) > 1:
                return partes[0] + ',' + decimal_parte[:-1]
    
    return nota_str


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
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      color: #333333;
      background-color: #ffffff;
      margin: 0;
      padding: 0 20px 20px 20px;
    }
    .container {
      max-width: 700px;
      margin: auto;
    }
    p {
      margin-bottom: 16px;
      text-align: justify;
    }
    a {
      color: #0645ad;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
    .highlight {
      background-color: #f0f0f0;
      border-left: 4px solid #999999;
      padding: 12px 16px;
      border-radius: 4px;
      margin: 16px 0;
      font-size: 0.95em;
      text-align: justify;
    }
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
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      color: #333333;
      background-color: #ffffff;
      margin: 0;
      padding: 0 20px 20px 20px;
    }
    .container {
      max-width: 700px;
      margin: auto;
    }
    p {
      margin-bottom: 16px;
      text-align: justify;
    }
    a {
      color: #0645ad;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
    .highlight {
      background-color: #f0f0f0;
      border-left: 4px solid #999999;
      padding: 12px 16px;
      border-radius: 4px;
      margin: 16px 0;
      font-size: 0.95em;
      text-align: justify;
    }
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

        # Critérios de avaliação e seus pesos para Aprovação/Reprovação
        criterios_avaliacao_aprov_reprov = [
            ("Correspondência do trabalho ao tema do evento e à seção temática escolhida", 2),
            ("Originalidade e contribuição do trabalho na área da Propriedade Intelectual", 1),
            ("Definição clara do problema, dos objetivos e da justificativa do trabalho", 2),
            ("Adequação dos métodos à pesquisa e confiabilidade dos procedimentos apresentados", 2),
            ("Clareza, coerência e objetividade na apresentação e discussão dos resultados", 3)
        ]
        
        # Separar nomes dos critérios e pesos
        nomes_criterios_aprov_reprov = [c[0] for c in criterios_avaliacao_aprov_reprov]
        pesos_criterios_aprov_reprov = [c[1] for c in criterios_avaliacao_aprov_reprov]

        # Notas Avaliador I
        st.subheader("Avaliador(a) I")
        # Criando um valor padrão para o text_area com as notas separadas por linha
        default_notas_i_str = "\n".join([str(8.5) for _ in nomes_criterios_aprov_reprov])
        notas_i_input = st.text_area(
            "Digite as notas para cada critério (uma por linha):",
            value=default_notas_i_str,
            key="notas_aprov_i_input"
        )
        notas_i_digitadas = []
        try:
            notas_i_digitadas = [float(n.strip().replace(',', '.')) for n in notas_i_input.split('\n') if n.strip()]
        except ValueError:
            st.warning("Por favor, insira notas válidas (números).")
            notas_i_digitadas = [0.0] * len(nomes_criterios_aprov_reprov) # Garante que a lista tenha o tamanho correto

        notas_i = {}
        media_ponderada_i = 0.0
        if len(notas_i_digitadas) == len(nomes_criterios_aprov_reprov):
            for i, c in enumerate(nomes_criterios_aprov_reprov):
                notas_i[c] = notas_i_digitadas[i]
            media_ponderada_i = calcular_media_ponderada(list(notas_i.values()), pesos_criterios_aprov_reprov)
            st.info(f"Média ponderada Avaliador I: **{formatar_nota_br(media_ponderada_i, 2)}**")
        else:
            st.warning(f"Por favor, insira {len(nomes_criterios_aprov_reprov)} notas para o Avaliador I.")
            notas_i = {c: 0.0 for c in nomes_criterios_aprov_reprov} # Define notas como 0.0 para evitar erro no HTML

        parecer_i = st.text_area("Parecer Avaliador(a) I", value='"O trabalho apresenta boa estrutura e metodologia consistente. A proposta é pertinente e contribui para o debate sobre Propriedade Intelectual e Sustentabilidade."', key="aprov_parecer_i")

        # Notas Avaliador II
        st.subheader("Avaliador(a) II")
        default_notas_ii_str = "\n".join([str(8.5) for _ in nomes_criterios_aprov_reprov])
        notas_ii_input = st.text_area(
            "Digite as notas para cada critério (uma por linha):",
            value=default_notas_ii_str,
            key="notas_aprov_ii_input"
        )
        notas_ii_digitadas = []
        try:
            notas_ii_digitadas = [float(n.strip().replace(',', '.')) for n in notas_ii_input.split('\n') if n.strip()]
        except ValueError:
            st.warning("Por favor, insira notas válidas (números).")
            notas_ii_digitadas = [0.0] * len(nomes_criterios_aprov_reprov)

        notas_ii = {}
        media_ponderada_ii = 0.0
        if len(notas_ii_digitadas) == len(nomes_criterios_aprov_reprov):
            for i, c in enumerate(nomes_criterios_aprov_reprov):
                notas_ii[c] = notas_ii_digitadas[i]
            media_ponderada_ii = calcular_media_ponderada(list(notas_ii.values()), pesos_criterios_aprov_reprov)
            st.info(f"Média ponderada Avaliador II: **{formatar_nota_br(media_ponderada_ii, 2)}**")
        else:
            st.warning(f"Por favor, insira {len(nomes_criterios_aprov_reprov)} notas para o Avaliador II.")
            notas_ii = {c: 0.0 for c in nomes_criterios_aprov_reprov} # Define notas como 0.0 para evitar erro no HTML

        parecer_ii = st.text_area("Parecer Avaliador(a) II", value='''"Texto claro, bem estruturado e alinhado com os objetivos do evento. Recomenda-se apenas uma revisão final para uniformização da escrita."''', key="aprov_parecer_ii")

        # Cálculo da Nota Final do trabalho (média aritmética das médias ponderadas dos avaliadores)
        if media_ponderada_i > 0 and media_ponderada_ii > 0:
            nota_final_aprovacao = (media_ponderada_i + media_ponderada_ii) / 2
        else:
            nota_final_aprovacao = 0.0
        st.metric("Nota final do trabalho (Média Aritmética):", formatar_nota_br(nota_final_aprovacao, 2))

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
        {''.join(f'<tr><td>{i+1}. {c}</td><td>{formatar_nota_br(notas_i[c])}</td></tr>' for i, c in enumerate(nomes_criterios_aprov_reprov))}
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
        {''.join(f'<tr><td>{i+1}. {c}</td><td>{formatar_nota_br(notas_ii[c])}</td></tr>' for i, c in enumerate(nomes_criterios_aprov_reprov))}
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

    elif aba == "Reprovação":
        st.header("Reprovação")

        # Critérios de avaliação e seus pesos para Aprovação/Reprovação (os mesmos da aba Aprovação)
        criterios_avaliacao_aprov_reprov = [
            ("Correspondência do trabalho ao tema do evento e à seção temática escolhida", 2),
            ("Originalidade e contribuição do trabalho na área da Propriedade Intelectual", 1),
            ("Definição clara do problema, dos objetivos e da justificativa do trabalho", 2),
            ("Adequação dos métodos à pesquisa e confiabilidade dos procedimentos apresentados", 2),
            ("Clareza, coerência e objetividade na apresentação e discussão dos resultados", 3)
        ]
        
        # Separar nomes dos critérios e pesos
        nomes_criterios_aprov_reprov = [c[0] for c in criterios_avaliacao_aprov_reprov]
        pesos_criterios_aprov_reprov = [c[1] for c in criterios_avaliacao_aprov_reprov]

        # Notas Avaliador I
        st.subheader("Avaliador(a) I")
        default_notas_i_str_reprov = "\n".join([str(6.5) for _ in nomes_criterios_aprov_reprov])
        notas_i_input_reprov = st.text_area(
            "Digite as notas para cada critério (uma por linha):",
            value=default_notas_i_str_reprov,
            key="notas_reprov_i_input"
        )
        notas_i_digitadas_reprov = []
        try:
            notas_i_digitadas_reprov = [float(n.strip().replace(',', '.')) for n in notas_i_input_reprov.split('\n') if n.strip()]
        except ValueError:
            st.warning("Por favor, insira notas válidas (números).")
            notas_i_digitadas_reprov = [0.0] * len(nomes_criterios_aprov_reprov)

        notas_i = {}
        media_ponderada_i = 0.0
        if len(notas_i_digitadas_reprov) == len(nomes_criterios_aprov_reprov):
            for i, c in enumerate(nomes_criterios_aprov_reprov):
                notas_i[c] = notas_i_digitadas_reprov[i]
            media_ponderada_i = calcular_media_ponderada(list(notas_i.values()), pesos_criterios_aprov_reprov)
            st.info(f"Média ponderada Avaliador I: **{formatar_nota_br(media_ponderada_i, 2)}**")
        else:
            st.warning(f"Por favor, insira {len(nomes_criterios_aprov_reprov)} notas para o Avaliador I.")
            notas_i = {c: 0.0 for c in nomes_criterios_aprov_reprov} # Define notas como 0.0 para evitar erro no HTML

        parecer_i = st.text_area("Parecer Avaliador(a) I", value='"O trabalho apresenta pontos que precisam ser aprimorados para melhor atender aos critérios do evento."', key="reprov_parecer_i")

        # Notas Avaliador II
        st.subheader("Avaliador(a) II")
        default_notas_ii_str_reprov = "\n".join([str(6.5) for _ in nomes_criterios_aprov_reprov])
        notas_ii_input_reprov = st.text_area(
            "Digite as notas para cada critério (uma por linha):",
            value=default_notas_ii_str_reprov,
            key="notas_reprov_ii_input"
        )
        notas_ii_digitadas_reprov = []
        try:
            notas_ii_digitadas_reprov = [float(n.strip().replace(',', '.')) for n in notas_ii_input_reprov.split('\n') if n.strip()]
        except ValueError:
            st.warning("Por favor, insira notas válidas (números).")
            notas_ii_digitadas_reprov = [0.0] * len(nomes_criterios_aprov_reprov)

        notas_ii = {}
        media_ponderada_ii = 0.0
        if len(notas_ii_digitadas_reprov) == len(nomes_criterios_aprov_reprov):
            for i, c in enumerate(nomes_criterios_aprov_reprov):
                notas_ii[c] = notas_ii_digitadas_reprov[i]
            media_ponderada_ii = calcular_media_ponderada(list(notas_ii.values()), pesos_criterios_aprov_reprov)
            st.info(f"Média ponderada Avaliador II: **{formatar_nota_br(media_ponderada_ii, 2)}**")
        else:
            st.warning(f"Por favor, insira {len(nomes_criterios_aprov_reprov)} notas para o Avaliador II.")
            notas_ii = {c: 0.0 for c in nomes_criterios_aprov_reprov} # Define notas como 0.0 para evitar erro no HTML

        parecer_ii = st.text_area("Parecer Avaliador(a) II", value='"Recomenda-se revisão e aprimoramento do conteúdo para futuras submissões."', key="reprov_parecer_ii")

        # Cálculo da Nota Final do trabalho (média aritmética das médias ponderadas dos avaliadores)
        if media_ponderada_i > 0 and media_ponderada_ii > 0:
            nota_final_reprovacao = (media_ponderada_i + media_ponderada_ii) / 2
        else:
            nota_final_reprovacao = 0.0
        st.metric("Nota final do trabalho (Média Aritmética):", formatar_nota_br(nota_final_reprovacao, 2))


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
        {''.join(f'<tr><td>{i+1}. {c}</td><td>{formatar_nota_br(notas_i[c])}</td></tr>' for i, c in enumerate(nomes_criterios_aprov_reprov))}
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
        {''.join(f'<tr><td>{i+1}. {c}</td><td>{formatar_nota_br(notas_ii[c])}</td></tr>' for i, c in enumerate(nomes_criterios_aprov_reprov))}
      </table>
      <p><strong>Média ponderada: {formatar_nota_br(media_ponderada_ii, 2)}</strong></p>
      <p class="parecer">{parecer_ii}</p>
    </div>

    <div class="nota-final">
      Nota final do trabalho: <strong>{formatar_nota_br(nota_final_reprovacao, 2)}</strong>
    </div>

    <p>
      Permanecemos à disposição para quaisquer dúvidas ou esclarecimentos que se fizer
