import streamlit as st

# ===== Cabeçalho único (autoajustado ao container) =====
HTML_HEADER = """
<img src="https://i.postimg.cc/tT1XwMm8/Cabe-alho-X.png"
     alt="Cabeçalho da VII SEMPI"
     style="max-width:100%; height:auto; display:block; margin-bottom:20px;" />
"""

# ===== Funções utilitárias =====

def formatar_nota_br(nota, casas_decimais=1):
    if nota == int(nota):
        return str(int(nota)).replace('.', ',')
    else:
        return f"{nota:.{casas_decimais}f}".replace('.', ',')

def calcular_media_ponderada(notas, pesos):
    if not notas or not pesos or len(notas) != len(pesos):
        return 0.0
    soma_produtos = sum(nota * peso for nota, peso in zip(notas, pesos))
    soma_pesos = sum(pesos)
    return soma_produtos / soma_pesos if soma_pesos > 0 else 0.0

def processar_notas_melhor(entrada):
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

# ===== Templates de lembretes (simplificados) =====
LEMBRETE_ENVIO_HTML = """
{html_header}
<p>{texto_envio_arquivo}</p>
"""

LEMBRETE_APRESENTACAO_HTML = """
{html_header}
<p>Tempo de apresentação: {tempo_apresentacao} minutos</p>
<p>Tempo para arguição: {tempo_arguicao} minutos</p>
"""

# ===== App =====
def main():
    st.set_page_config(page_title="Gerador de HTML SEMPI", layout="wide")
    st.title("💻 Notificação interna Even3 (VII SEMPI)")

    abas = ["🚫 Desclassificação", "✅ Aprovação", "❌ Reprovação", "🔔 Lembretes", "🏆 Resultado final"]
    aba = st.sidebar.radio("Selecione a aba:", abas)

    if aba == "🚫 Desclassificação":
        st.header("Desclassificação")
        motivos = st.text_area("Liste os motivos da desclassificação:", value="X/ Y/ Z")
        motivos_lista = [m.strip() for m in motivos.split("/") if m.strip()]
        html_desclassificacao = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head><meta charset="UTF-8"><style>body{{font-family:Arial,sans-serif;}}</style></head>
<body>
{HTML_HEADER}
<p>Prezado(a) autor(a),</p>
<div class="box"><ol>{"".join(f"<li>{m}</li>" for m in motivos_lista)}</ol></div>
</body></html>"""
        st.code(html_desclassificacao, language="html")

    elif aba in ["✅ Aprovação", "❌ Reprovação"]:
        st.header("Avaliação")

        criterios_avaliacao = [
            ("Correspondência do trabalho ao tema do evento e à seção temática escolhida", 2),
            ("Originalidade e contribuição do trabalho na área da Propriedade Intelectual", 1),
            ("Definição clara do problema, dos objetivos e da justificativa do trabalho", 2),
            ("Adequação dos métodos à pesquisa e confiabilidade dos procedimentos apresentados", 2),
            ("Clareza, coerência e objetividade na apresentação e discussão dos resultados", 3)
        ]
        nomes_criterios = [c[0] for c in criterios_avaliacao]
        pesos_criterios = [c[1] for c in criterios_avaliacao]

        def input_avaliador(prefix):
            st.subheader(f"Avaliador(a) {prefix}")
            data = st.text_input(f"Data Avaliador(a) {prefix}", value="4 de ago de 2025", key=f"data_{prefix}")
            default_notas_str = " ".join([str(0.0) for _ in nomes_criterios])
            notas_input = st.text_area(f"Digite as notas para cada critério (mesma linha, separadas por espaço ou ';') Avaliador {prefix}:",
                                       value=default_notas_str, key=f"notas_{prefix}_input")
            try:
                notas_digitadas = processar_notas_melhor(notas_input)
            except ValueError:
                st.warning("Por favor, insira notas válidas (números).")
                notas_digitadas = [0.0] * len(nomes_criterios)
            notas = {}
            media = 0.0
            if len(notas_digitadas) == len(nomes_criterios):
                for i, c in enumerate(nomes_criterios):
                    notas[c] = notas_digitadas[i]
                media = calcular_media_ponderada(list(notas.values()), pesos_criterios)
                st.info(f"Média ponderada Avaliador {prefix}: **{formatar_nota_br(media, 2)}**")
            else:
                st.warning(f"Por favor, insira {len(nomes_criterios)} notas.")
                notas = {c: 0.0 for c in nomes_criterios}
            parecer = st.text_area(f"Parecer Avaliador(a) {prefix}", value='"Parecer."', key=f"parecer_{prefix}")
            return data, notas, media, parecer

        data_i, notas_i, media_i, parecer_i = input_avaliador("I")
        data_ii, notas_ii, media_ii, parecer_ii = input_avaliador("II")

        nota_final = (media_i + media_ii)/2 if media_i > 0 and media_ii > 0 else 0.0
        st.metric("Nota final do trabalho:", formatar_nota_br(nota_final, 2))

        html_avaliacao = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<style>
body {{font-family: Arial,sans-serif;}}
table {{width:100%;border-collapse:collapse;margin-top:10px;}}
th, td {{text-align:left;padding:8px;border-bottom:1px solid #ccc;}}
th {{background-color:#e0e0e0;}}
.nota-final {{background-color: #dff0d8; border-left:4px solid #5cb85c;padding:16px;margin-top:20px;border-radius:4px;font-weight:bold;}}
.parecer {{font-style: italic;color:#444;}}
</style>
</head>
<body>
{HTML_HEADER}

<div class="box">
<p><strong>👤 Avaliador(a) I</strong> <span style="float:right;">{data_i}</span></p>
<table>
<tr><th>Critério</th><th>Nota</th><th>Peso</th></tr>
{''.join(f'<tr><td>{i+1}. {c}</td><td>{formatar_nota_br(notas_i[c])}</td><td>{pesos_criterios[i]}</td></tr>' for i,c in enumerate(nomes_criterios))}
</table>
<p><strong>Média ponderada: {formatar_nota_br(media_i,2)}</strong></p>
<p class="parecer">{parecer_i}</p>
</div>

<div class="box">
<p><strong>👤 Avaliador(a) II</strong> <span style="float:right;">{data_ii}</span></p>
<table>
<tr><th>Critério</th><th>Nota</th><th>Peso</th></tr>
{''.join(f'<tr><td>{i+1}. {c}</td><td>{formatar_nota_br(notas_ii[c])}</td><td>{pesos_criterios[i]}</td></tr>' for i,c in enumerate(nomes_criterios))}
</table>
<p><strong>Média ponderada: {formatar_nota_br(media_ii,2)}</strong></p>
<p class="parecer">{parecer_ii}</p>
</div>

<div class="nota-final">
Nota final do trabalho: <strong>{formatar_nota_br(nota_final,2)}</strong>
</div>
</body>
</html>"""
        st.code(html_avaliacao, language="html")

    elif aba == "🔔 Lembretes":
        st.header("Lembretes")
        texto_envio_arquivo = st.text_area("Texto para envio do arquivo:", value="Envio até 29 de agosto...")
        tempo_apresentacao = st.number_input("Tempo para apresentação (min)", min_value=1, max_value=60, value=10)
        tempo_arguicao = st.number_input("Tempo para arguição (min)", min_value=1, max_value=30, value=5)
        html_envio = LEMBRETE_ENVIO_HTML.format(html_header=HTML_HEADER, texto_envio_arquivo=texto_envio_arquivo)
        html_apresentacao = LEMBRETE_APRESENTACAO_HTML.format(html_header=HTML_HEADER,
                                                              tempo_apresentacao=tempo_apresentacao,
                                                              tempo_arguicao=tempo_arguicao)
        st.subheader("Lembrete envio arquivo")
        st.code(html_envio, language="html")
        st.subheader("Lembrete apresentação")
        st.code(html_apresentacao, language="html")

    elif aba == "🏆 Resultado final":
        st.header("Resultado Final")

        criterios_final = [
            ("Correspondência do trabalho ao tema do evento e à seção temática escolhida",1),
            ("Originalidade e contribuição do trabalho na área da Propriedade Intelectual",1),
            ("Definição clara do problema, dos objetivos e da justificativa do trabalho",1),
            ("Adequação dos métodos à pesquisa e confiabilidade dos procedimentos apresentados",2),
            ("Clareza, coerência e objetividade na apresentação e discussão dos resultados",2),
            ("Domínio do conteúdo apresentado",2),
            ("Adequação ao tempo de apresentação",1)
        ]
        nomes_final = [c[0] for c in criterios_final]
        pesos_final = [c[1] for c in criterios_final]

        def input_final(prefix):
            st.subheader(f"Avaliador(a) {prefix} - Apresentação")
            data = st.text_input(f"Data Avaliador(a) {prefix}", value="4 de ago de 2025", key=f"data_final_{prefix}")
            default_str = " ".join([str(0.0) for _ in nomes_final])
            notas_input = st.text_area(f"Notas Avaliador {prefix}:", value=default_str, key=f"notas_final_{prefix}_input")
            try:
                notas_digitadas = processar_notas_melhor(notas_input)
            except ValueError:
                st.warning("Notas inválidas.")
                notas_digitadas = [0.0]*len(nomes_final)
            notas = {}
            media = 0.0
            if len(notas_digitadas) == len(nomes_final):
                for i,c in enumerate(nomes_final):
                    notas[c] = notas_digitadas[i]
                media = calcular_media_ponderada(list(notas.values()), pesos_final)
                st.info(f"Média ponderada Avaliador {prefix}: **{formatar_nota_br(media,2)}**")
            else:
                notas = {c:0.0 for c in nomes_final}
            return data, notas, media

        data_i, notas_i, media_i = input_final("I")
        data_ii, notas_ii, media_ii = input_final("II")
        nota_final_apresentacao = (media_i+media_ii)/2 if media_i>0 and media_ii>0 else 0.0
        nota_final_escrito = st.number_input("TRABALHO ESCRITO:", min_value=0.0, max_value=10.0, step=0.1, value=0.0)
        nota_geral = calcular_media_ponderada([nota_final_escrito, nota_final_apresentacao],[7,3])
        st.metric("NOTA GERAL:", formatar_nota_br(nota_geral,2))

        html_resultado = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head><meta charset="UTF-8">
<style>
body {{font-family: Arial,sans-serif;}}
table {{width:100%;border-collapse:collapse;margin-top:10px;}}
th,td {{text-align:left;padding:8px;border-bottom:1px solid #ccc;}}
th {{background-color:#e0e0e0;}}
.nota-final {{background-color:#dff0d8;border-left:4px solid #5cb85c;padding:16px;margin-top:20px;border-radius:4px;font-weight:bold;}}
</style>
</head>
<body>
{HTML_HEADER}

<div class="box">
<p><strong>👤 Avaliador(a) I</strong> <span style="float:right;">{data_i}</span></p>
<table>
<tr><th>Critério</th><th>Nota</th><th>Peso</th></tr>
{''.join(f'<tr><td>{i+1}. {c}</td><td>{formatar_nota_br(notas_i[c])}</td><td>{pesos_final[i]}</td></tr>' for i,c in enumerate(nomes_final))}
</table>
<p><strong>Média ponderada: {formatar_nota_br(media_i,2)}</strong></p>
</div>

<div class="box">
<p><strong>👤 Avaliador(a) II</strong> <span style="float:right;">{data_ii}</span></p>
<table>
<tr><th>Critério</th><th>Nota</th><th>Peso</th></tr>
{''.join(f'<tr><td>{i+1}. {c}</td><td>{formatar_nota_br(notas_ii[c])}</td><td>{pesos_final[i]}</td></tr>' for i,c in enumerate(nomes_final))}
</table>
<p><strong>Média ponderada: {formatar_nota_br(media_ii,2)}</strong></p>
</div>

<div class="nota-final">
Nota final da apresentação: <strong>{formatar_nota_br(nota_final_apresentacao,2)}</strong><br>
Nota trabalho escrito: <strong>{formatar_nota_br(nota_final_escrito,2)}</strong><br>
Nota geral: <strong>{formatar_nota_br(nota_geral,2)}</strong>
</div>
</body>
</html>"""
        st.code(html_resultado, language="html")


if __name__ == "__main__":
    main()
