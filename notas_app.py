import streamlit as st

# ===== Identidade visual e dados do evento =====
EVENTO_NOME = "VIII Semana Acadêmica da Propriedade Intelectual"
EVENTO_SIGLA = "VIII SEMPI"
EVENTO_COMPLETO = f"{EVENTO_NOME} ({EVENTO_SIGLA})"
EVENTO_URL = "https://www.even3.com.br/viii-semana-academica-da-propriedade-intelectual-753406/"
EMAIL_CONTATO = "submissoes.sempi@gmail.com"

# ===== Cabeçalho único (autoajustado ao container) =====
HTML_HEADER = """
<img src="https://mcusercontent.com/2c391bf17d26a076dacd48918/images/5b0ec1af-a5e2-97f5-c683-61d55fab42bc.png"
     alt="Cabeçalho da VIII SEMPI"
     style="max-width:100%; height:auto; display:block; margin:0 0 22px 0; border-radius:12px;" />
"""

# ===== CSS institucional para os HTMLs gerados =====
EMAIL_CSS = """
body {
  font-family: Arial, Helvetica, sans-serif;
  line-height: 1.65;
  color: #2f2f2f;
  background-color: #f7f2e9;
  margin: 0;
  padding: 0;
}
.container {
  max-width: 760px;
  margin: 0 auto;
  padding: 26px 22px 32px 22px;
}
.email-card {
  background-color: #ffffff;
  border: 1px solid #e6dccb;
  border-radius: 16px;
  padding: 24px;
  box-shadow: 0 8px 24px rgba(4, 92, 110, 0.10);
}
.title-band {
  border-left: 6px solid #D1951D;
  background-color: #f3efe6;
  padding: 16px 18px;
  margin: 8px 0 24px 0;
  border-radius: 10px;
}
.title-band h1 {
  color: #045c6e;
  font-size: 22px;
  line-height: 1.25;
  margin: 0;
  letter-spacing: 0.3px;
  text-transform: uppercase;
}
.title-band p {
  color: #7b5a12;
  font-size: 14px;
  margin: 6px 0 0 0;
  text-align: left;
}
p {
  margin: 0 0 16px 0;
  text-align: justify;
}
a {
  color: #045c6e;
  text-decoration: none;
  font-weight: bold;
}
a:hover {
  text-decoration: underline;
}
.box {
  background-color: #ffffff;
  border: 1px solid #e7decf;
  border-top: 5px solid #D1951D;
  border-radius: 14px;
  padding: 18px;
  margin: 22px 0;
  box-shadow: 0 5px 16px rgba(4, 92, 110, 0.08);
}
.box-title {
  color: #045c6e;
  font-size: 16px;
  font-weight: bold;
  margin: 0 0 12px 0;
  text-align: left;
}
.box-date {
  color: #7b5a12;
  font-size: 13px;
  font-weight: normal;
  float: right;
}
.highlight {
  background-color: #f3efe6;
  border-left: 5px solid #D1951D;
  padding: 14px 16px;
  border-radius: 10px;
  margin: 18px 0;
  text-align: justify;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 12px;
  font-size: 14px;
}
th {
  background-color: #045c6e;
  color: #ffffff;
  padding: 10px 9px;
  border: 1px solid #045c6e;
  text-align: left;
}
td {
  padding: 10px 9px;
  border: 1px solid #e6dccb;
  vertical-align: top;
}
tr:nth-child(even) td {
  background-color: #fbf8f1;
}
.weight-cell {
  color: #7b5a12;
  font-weight: bold;
  text-align: center;
  white-space: nowrap;
}
.grade-cell {
  color: #045c6e;
  font-weight: bold;
  text-align: center;
  white-space: nowrap;
}
.media {
  background-color: #f3efe6;
  border-left: 5px solid #D1951D;
  border-radius: 10px;
  padding: 12px 14px;
  margin: 14px 0 0 0;
  color: #045c6e;
  font-weight: bold;
  text-align: left;
}
.parecer {
  margin-top: 14px;
  padding-top: 12px;
  border-top: 1px solid #e6dccb;
  font-style: italic;
  color: #444444;
  text-align: justify;
}
.nota-final {
  background-color: #045c6e;
  color: #ffffff;
  border-radius: 16px;
  padding: 20px;
  margin: 24px 0;
  text-align: center;
  box-shadow: 0 8px 22px rgba(4, 92, 110, 0.18);
}
.nota-final .label {
  display: block;
  color: #f2d69b;
  font-size: 13px;
  font-weight: bold;
  letter-spacing: 0.6px;
  text-transform: uppercase;
  margin-bottom: 4px;
}
.nota-final .value {
  display: block;
  font-size: 34px;
  font-weight: bold;
  line-height: 1.1;
}
.nota-final.reprovacao {
  background-color: #7b2d26;
}
.notas-container {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  margin: 24px 0;
  overflow: hidden;
  border-radius: 16px;
  box-shadow: 0 8px 22px rgba(4, 92, 110, 0.12);
}
.notas-container td {
  background-color: #045c6e;
  color: #ffffff;
  border: 1px solid #0c6f82;
  text-align: center;
  padding: 18px 10px;
}
.nota-label {
  display: block;
  color: #f2d69b;
  font-size: 12px;
  font-weight: bold;
  letter-spacing: 0.4px;
  text-transform: uppercase;
  margin-bottom: 6px;
}
.nota-value {
  display: block;
  color: #ffffff;
  font-size: 24px;
  font-weight: bold;
}
ol, ul {
  margin-top: 8px;
  padding-left: 24px;
}
li {
  margin-bottom: 8px;
}
.footer {
  border-top: 2px solid #D1951D;
  margin-top: 26px;
  padding-top: 14px;
  color: #045c6e;
  font-size: 13px;
  text-align: center;
}
"""

# ===== Funções utilitárias =====

def formatar_nota_br(nota, casas_decimais=1):
    if nota == int(nota):
        return str(int(nota)).replace('.', ',')
    return f"{nota:.{casas_decimais}f}".replace('.', ',')


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
        return 0.0
    soma_produtos = sum(nota * peso for nota, peso in zip(notas, pesos))
    soma_pesos = sum(pesos)
    return soma_produtos / soma_pesos if soma_pesos > 0 else 0.0


def processar_notas_melhor(entrada):
    """
    Aceita notas digitadas em mesma linha ou em linhas separadas.
    Separadores aceitos: espaço, nova linha e ponto-e-vírgula.
    Mantém vírgula como separador decimal (por exemplo: "8,5").
    Retorna lista de floats.
    """
    if entrada is None:
        return []
    s = entrada.replace('\n', ' ').replace(';', ' ')
    tokens = [t for t in s.split() if t.strip()]
    notas = []
    for t in tokens:
        try:
            notas.append(float(t.replace(',', '.')))
        except Exception as e:
            raise ValueError(f"Token inválido: {t}") from e
    return notas


def pagina_email(titulo, subtitulo, conteudo_html):
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <style>{EMAIL_CSS}</style>
</head>
<body>
  <div class="container">
    <div class="email-card">
      {HTML_HEADER}
      <div class="title-band">
        <h1>{titulo}</h1>
        <p>{subtitulo}</p>
      </div>
      {conteudo_html}
      <div class="footer">
        Coordenação Científica da {EVENTO_SIGLA}
      </div>
    </div>
  </div>
</body>
</html>"""


def montar_tabela_avaliacao(nomes_criterios, pesos, notas):
    linhas = "".join(
        f'<tr><td>{i + 1}. {criterio}</td><td class="weight-cell">{pesos[i]}</td><td class="grade-cell">{formatar_nota_br(notas[criterio])}</td></tr>'
        for i, criterio in enumerate(nomes_criterios)
    )
    return f"""
<table>
  <tr>
    <th>Critério</th>
    <th>Peso</th>
    <th>Nota</th>
  </tr>
  {linhas}
</table>"""


def montar_box_avaliador(rotulo, data, tabela_html, media, parecer=None):
    parecer_html = f'<p class="parecer">{parecer}</p>' if parecer is not None else ""
    return f"""
<div class="box">
  <p class="box-title">{rotulo}<span class="box-date">{data}</span></p>
  {tabela_html}
  <p class="media">Média ponderada: {formatar_nota_br(media, 2)}</p>
  {parecer_html}
</div>"""


def montar_bloco_nota_final(label, valor, classe_extra=""):
    classe = f"nota-final {classe_extra}".strip()
    return f"""
<div class="{classe}">
  <span class="label">{label}</span>
  <span class="value">{formatar_nota_br(valor, 2)}</span>
</div>"""


def coletar_notas_avaliador(prefixo, nomes_criterios, pesos_criterios, titulo_avaliador):
    st.subheader(titulo_avaliador)
    data = st.text_input(f"Data {titulo_avaliador}", value="4 de set de 2025", key=f"data_{prefixo}")
    default_notas = " ".join([str(0.0) for _ in nomes_criterios])
    notas_input = st.text_area(
        "Digite as notas para cada critério (na mesma linha, separadas por espaço ou ';'):",
        value=default_notas,
        key=f"notas_{prefixo}_input"
    )

    try:
        notas_digitadas = processar_notas_melhor(notas_input)
    except ValueError:
        st.warning("Por favor, insira notas válidas (números).")
        notas_digitadas = [0.0] * len(nomes_criterios)

    notas = {}
    media = 0.0
    if len(notas_digitadas) == len(nomes_criterios):
        for i, criterio in enumerate(nomes_criterios):
            notas[criterio] = notas_digitadas[i]
        media = calcular_media_ponderada(list(notas.values()), pesos_criterios)
        st.info(f"Média ponderada {titulo_avaliador}: **{formatar_nota_br(media, 2)}**")
    else:
        st.warning(f"Por favor, insira {len(nomes_criterios)} notas para {titulo_avaliador}.")
        notas = {criterio: 0.0 for criterio in nomes_criterios}

    return data, notas, media
    def criterios_trabalho_escrito():
    return [
        ("Clareza na definição do problema, dos objetivos e da justificativa do trabalho", 1),
        ("Adequação dos métodos ao objetivo do trabalho e confiabilidade dos procedimentos apresentados", 3),
        ("Qualidade da apresentação dos resultados e consistência das evidências apresentadas", 3),
        ("Qualidade da discussão dos resultados, considerando a interpretação dos achados e o diálogo com a literatura", 2),
        ("Coerência das considerações finais em relação aos objetivos e aos resultados apresentados", 1),
    ]


def criterios_apresentacao():
    return [
        ("Coerência entre problema, objetivos, métodos, resultados e considerações finais", 4),
        ("Domínio do conteúdo e organização da apresentação", 3),
        ("Clareza e fundamentação nas respostas à arguição dos avaliadores", 3),
    ]


def gerar_lembrete_envio_html(texto_envio_arquivo):
    conteudo = f"""
<p>Prezados(as) autores(as),</p>

<p>Esperamos que esta mensagem os(as) encontre bem.</p>

<p>
  A Comissão Organizadora da <strong>{EVENTO_COMPLETO}</strong> relembra que todos os trabalhos aprovados deverão ser apresentados em sessão pública e avaliados por membros do Comitê Científico.
</p>

<p>{texto_envio_arquivo}</p>

<div class="highlight">
  Se o autor principal não for apresentar o trabalho, seja por impossibilidade de comparecimento à sessão ou por outra razão, deverá designar um coautor para realizar a apresentação, respeitando o prazo estipulado. O coautor designado deverá, obrigatoriamente, estar inscrito no evento. Ressalta-se, porém, que os demais coautores que não participarão do evento, seja de forma presencial ou on-line, não precisam estar inscritos, ainda que seus nomes constem no trabalho. A alteração deverá ser comunicada à Comissão Organizadora no e-mail <a href="mailto:{EMAIL_CONTATO}">{EMAIL_CONTATO}</a> até <strong>29 de agosto de 2025</strong>.
</div>

<p>
  A ordem das apresentações, tanto presenciais quanto on-line, seguirá a programação previamente divulgada em nossos canais oficiais, salvo em casos excepcionais devidamente justificados. Autores que submeteram mais de um resumo expandido, especialmente em sessões temáticas diferentes, terão suas apresentações organizadas de forma a evitar conflitos de horário.
</p>

<p>
  O modelo editável está disponível no site do evento:<br />
  <a href="{EVENTO_URL}" target="_blank" rel="noopener noreferrer">{EVENTO_URL}</a>.
  Embora não haja limite de quantidade de slides, é obrigatório manter integralmente a formatação original, incluindo estilo, tamanho da fonte e cores.
</p>

<p>Permanecemos à disposição para quaisquer dúvidas ou esclarecimentos que se fizerem necessários.</p>
"""
    return pagina_email("Lembrete aos autores", "Envio do arquivo de apresentação", conteudo)


def gerar_lembrete_apresentacao_html(tempo_apresentacao, tempo_arguicao):
    conteudo = f"""
<p>Prezados(as),</p>

<p>
  A Comissão Organizadora da <strong>{EVENTO_COMPLETO}</strong> relembra que as apresentações dos trabalhos aprovados acontecerão <strong>amanhã</strong>. A programação completa, contendo datas, horários, locais e ordem das apresentações, encontra-se disponível no site oficial do evento:
</p>

<p><a href="{EVENTO_URL}" target="_blank" rel="noopener noreferrer">{EVENTO_URL}</a></p>

<div class="highlight">
  <p style="text-align: left;"><strong>Orientações importantes</strong></p>
  <ul>
    <li style="text-align: left;">Autores que apresentarão seus trabalhos presencialmente devem comparecer ao local da sessão com, no mínimo, <strong>20 minutos de antecedência</strong>.</li>
    <li style="text-align: left;">Essa orientação também se aplica aos participantes com apresentação on-line autorizada, mediante justificativa formal.</li>
    <li style="text-align: left;"><strong>Não serão permitidas correções ou substituições</strong> do arquivo de apresentação durante o evento.</li>
  </ul>
</div>

<p>
  Cada apresentador(a) disporá de até <strong>{tempo_apresentacao} minutos</strong> para a exposição do trabalho, seguidos de até <strong>{tempo_arguicao} minutos</strong> para arguição e/ou comentários dos(as) avaliadores(as).
</p>

<p>
  Cada trabalho será avaliado por, no mínimo, dois pareceristas. Os critérios de avaliação da apresentação oral serão:
</p>

<ul>
  <li>Coerência entre problema, objetivos, métodos, resultados e considerações finais;</li>
  <li>Domínio do conteúdo e organização da apresentação;</li>
  <li>Clareza e fundamentação nas respostas à arguição dos avaliadores.</li>
</ul>

<p>
  Cada critério será avaliado em uma escala de 0 a 10, e a nota final de cada avaliador será calculada com base na média ponderada das notas atribuídas. A nota final da apresentação corresponderá à média aritmética das avaliações dos pareceristas.
</p>

<p>
  Para fins de premiação, será considerada a média ponderada entre a nota do trabalho escrito e a nota da apresentação.
</p>

<p>Desejamos uma excelente apresentação.</p>
"""
    return pagina_email("Lembrete de apresentação", "Orientações para a sessão pública", conteudo)


# ===== App =====

def main():
    st.set_page_config(page_title="Gerador de HTML SEMPI", layout="wide")

    st.title(f"💻 Notificação interna Even3 ({EVENTO_SIGLA})")

    abas = ["🚫 Desclassificação", "✅ Aprovação", "❌ Reprovação", "🔔 Lembretes", "🏆 Resultado final"]
    aba = st.sidebar.radio("Selecione a aba:", abas)

    if aba == "🚫 Desclassificação":
        st.header("Desclassificação")

        motivos = st.text_area(
            "Liste os motivos da desclassificação:",
            value="X/ Y/ Z"
        )
        motivos_lista = [m.strip() for m in motivos.split("/") if m.strip()]
        lista_motivos = "".join(f"<li>{m}</li>" for m in motivos_lista)

        conteudo = f"""
<p>Prezado(a) autor(a),</p>

<p>Esperamos que esta mensagem o(a) encontre bem.</p>

<p>
  Agradecemos o envio do seu trabalho à <strong>{EVENTO_COMPLETO}</strong>. Após revisão editorial preliminar (<em>desk review</em>), informamos que seu trabalho <strong>não atendeu</strong> integralmente aos requisitos mínimos para encaminhamento aos avaliadores.
</p>

<div class="box">
  <p class="box-title">Principais aspectos identificados</p>
  <ol>{lista_motivos}</ol>
</div>

<p>
  Caso o prazo de submissão ainda esteja vigente, o(a) responsável pela submissão poderá realizar nova submissão no sistema.
</p>

<p>Permanecemos à disposição para quaisquer dúvidas ou esclarecimentos que se fizerem necessários.</p>
"""
        html_desclassificacao = pagina_email(
            "Resultado da revisão editorial preliminar",
            "Trabalho desclassificado antes do encaminhamento aos avaliadores",
            conteudo
        )
        st.code(html_desclassificacao, language="html")

    elif aba == "✅ Aprovação":
        st.header("Aprovação")

        criterios_avaliacao_aprov_reprov = criterios_trabalho_escrito()
        nomes_criterios_aprov_reprov = [c[0] for c in criterios_avaliacao_aprov_reprov]
        pesos_criterios_aprov_reprov = [c[1] for c in criterios_avaliacao_aprov_reprov]

        data_avaliador_i, notas_i, media_ponderada_i = coletar_notas_avaliador(
            "aprov_i", nomes_criterios_aprov_reprov, pesos_criterios_aprov_reprov, "Avaliador(a) I"
        )
        parecer_i = st.text_area("Parecer Avaliador(a) I", value='"Parecer."', key="aprov_parecer_i")

        data_avaliador_ii, notas_ii, media_ponderada_ii = coletar_notas_avaliador(
            "aprov_ii", nomes_criterios_aprov_reprov, pesos_criterios_aprov_reprov, "Avaliador(a) II"
        )
        parecer_ii = st.text_area("Parecer Avaliador(a) II", value='"Parecer."', key="aprov_parecer_ii")

        if media_ponderada_i > 0 and media_ponderada_ii > 0:
            nota_final_aprovacao = (media_ponderada_i + media_ponderada_ii) / 2
        else:
            nota_final_aprovacao = 0.0
        st.metric("Nota final do trabalho:", formatar_nota_br(nota_final_aprovacao, 2))

        tabela_i = montar_tabela_avaliacao(nomes_criterios_aprov_reprov, pesos_criterios_aprov_reprov, notas_i)
        tabela_ii = montar_tabela_avaliacao(nomes_criterios_aprov_reprov, pesos_criterios_aprov_reprov, notas_ii)

        conteudo = f"""
<p>Prezados(as),</p>

<p>Esperamos que esta mensagem os(as) encontre bem.</p>

<p>
  Conforme comunicado anterior, esta mensagem apresenta os detalhes das avaliações realizadas pelos membros do Comitê Científico da <strong>{EVENTO_COMPLETO}</strong>. A divulgação das notas e dos pareceres visa dar transparência ao processo avaliativo e contribuir para o aprimoramento do trabalho apresentado e de futuras submissões.
</p>

{montar_box_avaliador("Avaliador(a) I", data_avaliador_i, tabela_i, media_ponderada_i, parecer_i)}

{montar_box_avaliador("Avaliador(a) II", data_avaliador_ii, tabela_ii, media_ponderada_ii, parecer_ii)}

{montar_bloco_nota_final("Nota final do trabalho", nota_final_aprovacao)}

<p>
  As orientações para a elaboração e o envio do arquivo da apresentação estão disponíveis no site do evento:<br />
  <a href="{EVENTO_URL}" target="_blank">{EVENTO_URL}</a>
</p>

<p>Permanecemos à disposição para quaisquer dúvidas ou esclarecimentos que se fizerem necessários.</p>
"""
        html_aprovacao = pagina_email("Resultado da avaliação", "Espelho de notas e pareceres", conteudo)
        st.code(html_aprovacao, language="html")
            elif aba == "❌ Reprovação":
        st.header("Reprovação")

        criterios_avaliacao_aprov_reprov = criterios_trabalho_escrito()
        nomes_criterios_aprov_reprov = [c[0] for c in criterios_avaliacao_aprov_reprov]
        pesos_criterios_aprov_reprov = [c[1] for c in criterios_avaliacao_aprov_reprov]

        data_avaliador_i, notas_i, media_ponderada_i = coletar_notas_avaliador(
            "reprov_i", nomes_criterios_aprov_reprov, pesos_criterios_aprov_reprov, "Avaliador(a) I"
        )
        parecer_i = st.text_area("Parecer Avaliador(a) I", value='"Parecer."', key="reprov_parecer_i")

        data_avaliador_ii, notas_ii, media_ponderada_ii = coletar_notas_avaliador(
            "reprov_ii", nomes_criterios_aprov_reprov, pesos_criterios_aprov_reprov, "Avaliador(a) II"
        )
        parecer_ii = st.text_area("Parecer Avaliador(a) II", value='"Parecer."', key="reprov_parecer_ii")

        if media_ponderada_i > 0 and media_ponderada_ii > 0:
            nota_final_reprovacao = (media_ponderada_i + media_ponderada_ii) / 2
        else:
            nota_final_reprovacao = 0.0
        st.metric("Nota final do trabalho:", formatar_nota_br(nota_final_reprovacao, 2))

        tabela_i = montar_tabela_avaliacao(nomes_criterios_aprov_reprov, pesos_criterios_aprov_reprov, notas_i)
        tabela_ii = montar_tabela_avaliacao(nomes_criterios_aprov_reprov, pesos_criterios_aprov_reprov, notas_ii)

        conteudo = f"""
<p>Prezados(as),</p>

<p>Esperamos que esta mensagem os(as) encontre bem.</p>

<p>
  Conforme comunicado anterior, esta mensagem apresenta os detalhes das avaliações realizadas pelos membros do Comitê Científico da <strong>{EVENTO_COMPLETO}</strong>. A divulgação das notas e dos pareceres visa dar transparência ao processo avaliativo e contribuir para o aprimoramento do trabalho apresentado e de futuras submissões.
</p>

{montar_box_avaliador("Avaliador(a) I", data_avaliador_i, tabela_i, media_ponderada_i, parecer_i)}

{montar_box_avaliador("Avaliador(a) II", data_avaliador_ii, tabela_ii, media_ponderada_ii, parecer_ii)}

{montar_bloco_nota_final("Nota final do trabalho", nota_final_reprovacao, "reprovacao")}

<p>Permanecemos à disposição para quaisquer dúvidas ou esclarecimentos que se fizerem necessários.</p>
"""
        html_reprovacao = pagina_email("Resultado da avaliação", "Espelho de notas e pareceres", conteudo)
        st.code(html_reprovacao, language="html")

    elif aba == "🔔 Lembretes":
        st.header("Lembretes")

        st.markdown("### Texto para envio do arquivo da apresentação")
        texto_envio_arquivo = st.text_area(
            "Digite o texto para o lembrete de envio do arquivo:",
            value=(
                "Para tanto, solicitamos que o arquivo de apresentação seja enviado até o dia "
                "<strong>29 de agosto de 2025</strong>, em formato PDF, por meio da Área do Participante. "
                "Para realizar o envio, acesse a plataforma com seu login e senha, clique no menu \"Submissões\", "
                "selecione o trabalho correspondente, clique em \"Editar\" e anexe o arquivo no campo indicado. "
                "Após o envio, certifique-se de salvar as alterações."
            )
        )

        st.markdown("### Tempos para apresentação")
        tempo_apresentacao = st.number_input("Tempo para apresentação (minutos)", min_value=1, max_value=60, value=10)
        tempo_arguicao = st.number_input("Tempo para arguição (minutos)", min_value=1, max_value=30, value=5)

        html_lembrete_envio = gerar_lembrete_envio_html(texto_envio_arquivo)
        html_lembrete_apresentacao = gerar_lembrete_apresentacao_html(tempo_apresentacao, tempo_arguicao)

        st.subheader("Lembrete para envio do arquivo")
        st.code(html_lembrete_envio, language="html")

        st.subheader("Lembrete para apresentação")
        st.code(html_lembrete_apresentacao, language="html")

    elif aba == "🏆 Resultado final":
        st.header("Resultado Final")

        criterios_avaliacao_final = criterios_apresentacao()
        nomes_criterios_final = [c[0] for c in criterios_avaliacao_final]
        pesos_criterios_final = [c[1] for c in criterios_avaliacao_final]

        data_avaliador_final_i, notas_final_i, media_ponderada_final_i = coletar_notas_avaliador(
            "final_i", nomes_criterios_final, pesos_criterios_final, "Avaliador(a) I - Apresentação"
        )

        data_avaliador_final_ii, notas_final_ii, media_ponderada_final_ii = coletar_notas_avaliador(
            "final_ii", nomes_criterios_final, pesos_criterios_final, "Avaliador(a) II - Apresentação"
        )

        if media_ponderada_final_i > 0 and media_ponderada_final_ii > 0:
            nota_final_apresentacao = (media_ponderada_final_i + media_ponderada_final_ii) / 2
        else:
            nota_final_apresentacao = 0.0
        st.metric("APRESENTAÇÃO ORAL:", formatar_nota_br(nota_final_apresentacao, 2))

        nota_final_escrito = st.number_input("TRABALHO ESCRITO:", min_value=0.0, max_value=10.0, step=0.1, value=0.0)

        nota_geral_ponderada = calcular_media_ponderada(
            [nota_final_escrito, nota_final_apresentacao],
            [7, 3]
        )
        st.metric("NOTA GERAL:", formatar_nota_br(nota_geral_ponderada, 2))

        hora_encerramento = st.text_input("Hora da cerimônia de encerramento:", value="XXh")

        tabela_i = montar_tabela_avaliacao(nomes_criterios_final, pesos_criterios_final, notas_final_i)
        tabela_ii = montar_tabela_avaliacao(nomes_criterios_final, pesos_criterios_final, notas_final_ii)

        notas_html = f"""
<table class="notas-container">
  <tr>
    <td>
      <span class="nota-label">Trabalho escrito</span>
      <span class="nota-value">{formatar_nota_br(nota_final_escrito, 2)}</span>
    </td>
    <td>
      <span class="nota-label">Apresentação oral</span>
      <span class="nota-value">{formatar_nota_br(nota_final_apresentacao, 2)}</span>
    </td>
    <td>
      <span class="nota-label">Nota geral</span>
      <span class="nota-value">{formatar_nota_br(nota_geral_ponderada, 2)}</span>
    </td>
  </tr>
</table>
"""

        conteudo = f"""
<p>Prezados(as),</p>

<p>Esperamos que esta mensagem os(as) encontre bem.</p>

<p>
  A Comissão Organizadora da <strong>{EVENTO_COMPLETO}</strong> os(as) parabeniza pela apresentação do trabalho. Abaixo, apresentamos as avaliações realizadas pelos membros do Comitê Científico, com base nos critérios previamente definidos.
</p>

{montar_box_avaliador("Avaliador(a) I", data_avaliador_final_i, tabela_i, media_ponderada_final_i)}

{montar_box_avaliador("Avaliador(a) II", data_avaliador_final_ii, tabela_ii, media_ponderada_final_ii)}

{notas_html}

<p>
  Aproveitamos para convidá-los(as) a participar da <strong>cerimônia de encerramento</strong>, que será realizada amanhã, <strong>5 de setembro de 2025, às {hora_encerramento}</strong>, no auditório do SergipeTec. Durante a solenidade, serão entregues os <strong>Certificados de Menção Honrosa</strong> aos três trabalhos com as maiores notas gerais em cada seção temática. Também será concedido o <strong>Certificado de Reconhecimento de Melhor Trabalho</strong> ao(à) autor(a) do trabalho que obteve a maior nota geral do evento.
</p>

<p>Permanecemos à disposição para quaisquer dúvidas ou esclarecimentos que se fizerem necessários.</p>
"""
        html_resultado_final = pagina_email("Resultado final", "Notas da apresentação e nota geral", conteudo)
        st.code(html_resultado_final, language="html")


if __name__ == "__main__":
    main()
