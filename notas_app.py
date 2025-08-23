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

# ===== Templates de lembretes =====
LEMBRETE_ENVIO_HTML = """
<div class="container">
{html_header}
<p>Prezado(a) autor(a),</p>
<p>{texto_envio_arquivo}</p>
</div>
"""

LEMBRETE_APRESENTACAO_HTML = """
<div class="container">
{html_header}
<p>Prezado(a) autor(a),</p>
<p>O tempo da sua apresentação será de {tempo_apresentacao} minutos e o tempo de arguição será de {tempo_arguicao} minutos.</p>
</div>
"""

# ===== App =====
def main():
    st.set_page_config(page_title="Gerador de HTML SEMPI", layout="wide")
    st.title("💻 Notificação interna Even3 (VII SEMPI)")

    abas = ["🚫 Desclassificação", "✅ Aprovação", "❌ Reprovação", "🔔 Lembretes", "🏆 Resultado final"]
    aba = st.sidebar.radio("Selecione a aba:", abas)

    # ---------- Aba Desclassificação ----------
    if aba == "🚫 Desclassificação":
        st.header("Desclassificação")
        motivos = st.text_area("Liste os motivos da desclassificação:", value="X/ Y/ Z")
        motivos_lista = [m.strip() for m in motivos.split("/") if m.strip()]

        html_desclassificacao = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Desclassificação</title>
</head>
<body>
<div class="container">
{HTML_HEADER}
<p>Prezado(a) autor(a),</p>
<div class="box">
<ol>
{"".join(f"<li>{m}</li>" for m in motivos_lista)}
</ol>
</div>
</div>
</body>
</html>"""
        st.code(html_desclassificacao, language="html")

    # ---------- Aba Aprovação / Reprovação ----------
    elif aba in ["✅ Aprovação", "❌ Reprovação"]:
        st.header("Aprovação" if aba=="✅ Aprovação" else "Reprovação")

        criterios_avaliacao = [
            ("Correspondência do trabalho ao tema do evento e à seção temática escolhida", 2),
            ("Originalidade e contribuição do trabalho na área da Propriedade Intelectual", 1),
            ("Definição clara do problema, dos objetivos e da justificativa do trabalho", 2),
            ("Adequação dos métodos à pesquisa e confiabilidade dos procedimentos apresentados", 2),
            ("Clareza, coerência e objetividade na apresentação e discussão dos resultados", 3)
        ]

        nomes_criterios = [c[0] for c in criterios_avaliacao]
        pesos_criterios = [c[1] for c in criterios_avaliacao]

        # Função auxiliar para processar avaliador
        def avaliar(avaliador_label, key_prefix):
            st.subheader(f"Avaliador(a) {avaliador_label}")
            data = st.text_input(f"Data Avaliador(a) {avaliador_label}", value="4 de ago de 2025", key=f"{key_prefix}_data")
            default_notas_str = " ".join([str(0.0) for _ in nomes_criterios])
            notas_input = st.text_area("Notas (mesma linha, separadas por espaço ou ';'):", value=default_notas_str, key=f"{key_prefix}_notas_input")
            try:
                notas_digitadas = processar_notas_melhor(notas_input)
            except ValueError:
                st.warning("Notas inválidas.")
                notas_digitadas = [0.0]*len(nomes_criterios)
            notas_dict = {c: notas_digitadas[i] for i, c in enumerate(nomes_criterios)} if len(notas_digitadas)==len(nomes_criterios) else {c:0.0 for c in nomes_criterios}
            media = calcular_media_ponderada(list(notas_dict.values()), pesos_criterios)
            st.info(f"Média ponderada Avaliador {avaliador_label}: **{formatar_nota_br(media,2)}**")
            parecer = st.text_area(f"Parecer Avaliador(a) {avaliador_label}", value='"Parecer."', key=f"{key_prefix}_parecer")
            return data, notas_dict, media, parecer

        data_i, notas_i, media_i, parecer_i = avaliar("I", f"{aba}_i")
        data_ii, notas_ii, media_ii, parecer_ii = avaliar("II", f"{aba}_ii")

        nota_final = (media_i + media_ii)/2 if media_i>0 and media_ii>0 else 0.0
        st.metric("Nota final do trabalho:", formatar_nota_br(nota_final,2))

        # Gerar HTML completo
        html_template = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>{aba}</title>
</head>
<body>
<div class="container">
{HTML_HEADER}

<div class="box">
<p><strong>👤 Avaliador(a) I</strong> <span style="float: right;">{data_i}</span></p>
<table border="1" cellspacing="0" cellpadding="4">
<tr><th>Critério</th><th>Nota</th></tr>
{''.join(f'<tr><td>{i+1}. {c} (Peso: {pesos_criterios[i]})</td><td>{formatar_nota_br(notas_i[c])}</td></tr>' for i,c in enumerate(nomes_criterios))}
</table>
<p><strong>Média ponderada: {formatar_nota_br(media_i,2)}</strong></p>
<p class="parecer">{parecer_i}</p>
</div>

<div class="box">
<p><strong>👤 Avaliador(a) II</strong> <span style="float: right;">{data_ii}</span></p>
<table border="1" cellspacing="0" cellpadding="4">
<tr><th>Critério</th><th>Nota</th></tr>
{''.join(f'<tr><td>{i+1}. {c} (Peso: {pesos_criterios[i]})</td><td>{formatar_nota_br(notas_ii[c])}</td></tr>' for i,c in enumerate(nomes_criterios))}
</table>
<p><strong>Média ponderada: {formatar_nota_br(media_ii,2)}</strong></p>
<p class="parecer">{parecer_ii}</p>
</div>

<div class="nota-final">
Nota final do trabalho: <strong>{formatar_nota_br(nota_final,2)}</strong>
</div>
</div>
</body>
</html>
"""
        st.code(html_template, language="html")

    # ---------- Aba Lembretes ----------
    elif aba == "🔔 Lembretes":
        st.header("Lembretes")
        texto_envio_arquivo = st.text_area("Texto lembrete envio arquivo", value="Para tanto, solicitamos...")
        tempo_apresentacao = st.number_input("Tempo apresentação (minutos)", min_value=1, max_value=60, value=10)
        tempo_arguicao = st.number_input("Tempo arguição (minutos)", min_value=1, max_value=30, value=5)
        html_lembrete_envio = LEMBRETE_ENVIO_HTML.format(html_header=HTML_HEADER, texto_envio_arquivo=texto_envio_arquivo)
        html_lembrete_apresentacao = LEMBRETE_APRESENTACAO_HTML.format(html_header=HTML_HEADER, tempo_apresentacao=tempo_apresentacao, tempo_arguicao=tempo_arguicao)
        st.subheader("Lembrete para envio do arquivo")
        st.code(html_lembrete_envio, language="html")
        st.subheader("Lembrete para apresentação")
        st.code(html_lembrete_apresentacao, language="html")

    # ---------- Aba Resultado Final ----------
    elif aba == "🏆 Resultado final":
        st.header("Resultado Final")

        criterios_final = [
            ("Correspondência do trabalho ao tema do evento e à seção temática escolhida", 1),
            ("Originalidade e contribuição do trabalho na área da Propriedade Intelectual", 1),
            ("Definição clara do problema, dos objetivos e da justificativa do trabalho", 1),
            ("Adequação dos métodos à pesquisa e confiabilidade dos procedimentos apresentados", 2),
            ("Clareza, coerência e objetividade na apresentação e discussão dos resultados", 2),
            ("Domínio do conteúdo apresentado", 2),
            ("Adequação ao tempo de apresentação", 1)
        ]
        nomes_criterios_final = [c[0] for c in criterios_final]
        pesos_criterios_final = [c[1] for c in criterios_final]

        data_i, notas_i, media_i, parecer_i = avaliar("I", f"{aba}_i")
        data_ii, notas_ii, media_ii, parecer_ii = avaliar("II", f"{aba}_ii")

        nota_final = (media_i + media_ii)/2 if media_i>0 and media_ii>0 else 0.0
        st.metric("Nota final do trabalho:", formatar_nota_br(nota_final,2))

        # HTML completo Resultado Final
        html_template = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Resultado Final</title>
</head>
<body>
<div class="container">
{HTML_HEADER}

<div class="box">
<p><strong>👤 Avaliador(a) I</strong> <span style="float: right;">{data_i}</span></p>
<table border="1" cellspacing="0" cellpadding="4">
<tr><th>Critério</th><th>Nota</th></tr>
{''.join(f'<tr><td>{i+1}. {c} (Peso: {pesos_criterios_final[i]})</td><td>{formatar_nota_br(notas_i.get(c,0))}</td></tr>' for i,c in enumerate(nomes_criterios_final))}
</table>
<p><strong>Média ponderada: {formatar_nota_br(media_i,2)}</strong></p>
<p class="parecer">{parecer_i}</p>
</div>

<div class="box">
<p><strong>👤 Avaliador(a) II</strong> <span style="float: right;">{data_ii}</span></p>
<table border="1" cellspacing="0" cellpadding="4">
<tr><th>Critério</th><th>Nota</th></tr>
{''.join(f'<tr><td>{i+1}. {c} (Peso: {pesos_criterios_final[i]})</td><td>{formatar_nota_br(notas_ii.get(c,0))}</td></tr>' for i,c in enumerate(nomes_criterios_final))}
</table>
<p><strong>Média ponderada: {formatar_nota_br(media_ii,2)}</strong></p>
<p class="parecer">{parecer_ii}</p>
</div>

<div class="nota-final">
Nota final do trabalho: <strong>{formatar_nota_br(nota_final,2)}</strong>
</div>
</div>
</body>
</html>
"""
        st.code(html_template, language="html")

if __name__ == "__main__":
    main()
