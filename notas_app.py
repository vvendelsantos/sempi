import streamlit as st

# ===== Cabeçalho =====
HTML_HEADER = """
<img src="https://i.postimg.cc/tT1XwMm8/Cabe-alho-X.png"
     alt="Cabeçalho da VII SEMPI"
     style="max-width:100%; height:auto; display:block; margin-bottom:20px;" />
"""

# ===== Funções =====
def formatar_nota_br(nota, casas_decimais=1):
    if nota == int(nota):
        return str(int(nota)).replace('.', ',')
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

# ===== Templates de lembrete =====
LEMBRETE_ENVIO_HTML = "<p>Lembrete de envio</p>"
LEMBRETE_APRESENTACAO_HTML = "<p>Lembrete de apresentação</p>"

# ===== App =====
def main():
    st.set_page_config(page_title="Gerador de HTML SEMPI", layout="wide")
    st.title("💻 Notificação interna Even3 (VII SEMPI)")
    
    abas = ["🚫 Desclassificação", "✅ Aprovação", "❌ Reprovação", "🔔 Lembretes", "🏆 Resultado final"]
    aba = st.sidebar.radio("Selecione a aba:", abas)

    criterios_avaliacao = [
        ("Correspondência do trabalho ao tema do evento e à seção temática escolhida", 2),
        ("Originalidade e contribuição do trabalho na área da Propriedade Intelectual", 1),
        ("Definição clara do problema, dos objetivos e da justificativa do trabalho", 2),
        ("Adequação dos métodos à pesquisa e confiabilidade dos procedimentos apresentados", 2),
        ("Clareza, coerência e objetividade na apresentação e discussão dos resultados", 3)
    ]
    nomes_criterios = [c[0] for c in criterios_avaliacao]
    pesos_criterios = [c[1] for c in criterios_avaliacao]

    # ---------------- DESCLASSIFICAÇÃO ----------------
    if aba == "🚫 Desclassificação":
        st.header("Desclassificação")
        motivos = st.text_area("Liste os motivos da desclassificação:", value="X/ Y/ Z")
        motivos_lista = [m.strip() for m in motivos.split("/") if m.strip()]
        html_desclassificacao = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head><meta charset="UTF-8"><style>
body{{font-family: Arial,sans-serif;line-height:1.6;}}
.container{{max-width:700px;margin:auto;padding:20px;}}
.box{{background:#f0f0f0;border-left:4px solid #999;padding:16px;margin:20px 0;border-radius:4px;text-align:justify;}}
ol{{padding-left:20px;}}
</style></head>
<body>
<div class="container">
{HTML_HEADER}
<p>Prezado(a) autor(a),</p>
<p>Após análise preliminar, informamos que seu trabalho <strong>não atendeu</strong> integralmente às diretrizes da Comissão Organizadora.</p>
<div class="box">
<p><strong>📌 Principais aspectos a serem corrigidos:</strong></p>
<ol>
{"".join(f"<li>{m}</li>" for m in motivos_lista)}
</ol>
</div>
<p>Solicitamos que o trabalho corrigido seja ressubmetido até <strong>19 de agosto de 2025</strong>.</p>
</div></body></html>"""
        st.code(html_desclassificacao, language="html")

    # ---------------- APROVAÇÃO ----------------
    elif aba == "✅ Aprovação":
        st.header("Aprovação")

        # --- Avaliador I ---
        st.subheader("Avaliador(a) I")
        data_i = st.text_input("Data Avaliador(a) I", value="4 de ago de 2025", key="data_i")
        default_notas_i_str = " ".join(["0" for _ in nomes_criterios])
        notas_i_input = st.text_area("Notas Avaliador(a) I", value=default_notas_i_str, key="notas_i_input")
        try:
            notas_i_digitadas = processar_notas_melhor(notas_i_input)
        except ValueError:
            st.warning("Notas inválidas.")
            notas_i_digitadas = [0]*len(nomes_criterios)
        notas_i = {c: notas_i_digitadas[i] for i,c in enumerate(nomes_criterios)}
        media_i = calcular_media_ponderada(list(notas_i.values()), pesos_criterios)
        st.info(f"Média ponderada: {formatar_nota_br(media_i,2)}")
        parecer_i = st.text_area("Parecer Avaliador(a) I", value='"Parecer."', key="parecer_i")

        # --- Avaliador II ---
        st.subheader("Avaliador(a) II")
        data_ii = st.text_input("Data Avaliador(a) II", value="4 de ago de 2025", key="data_ii")
        default_notas_ii_str = " ".join(["0" for _ in nomes_criterios])
        notas_ii_input = st.text_area("Notas Avaliador(a) II", value=default_notas_ii_str, key="notas_ii_input")
        try:
            notas_ii_digitadas = processar_notas_melhor(notas_ii_input)
        except ValueError:
            st.warning("Notas inválidas.")
            notas_ii_digitadas = [0]*len(nomes_criterios)
        notas_ii = {c: notas_ii_digitadas[i] for i,c in enumerate(nomes_criterios)}
        media_ii = calcular_media_ponderada(list(notas_ii.values()), pesos_criterios)
        st.info(f"Média ponderada: {formatar_nota_br(media_ii,2)}")
        parecer_ii = st.text_area("Parecer Avaliador(a) II", value='"Parecer."', key="parecer_ii")

        nota_final = (media_i + media_ii)/2 if media_i>0 and media_ii>0 else 0.0
        st.metric("Nota final do trabalho", formatar_nota_br(nota_final,2))

        html_aprovacao = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<style>
body{{font-family:Arial,sans-serif;line-height:1.6;color:#333;}}
.container{{max-width:700px;margin:auto;padding:20px;}}
.box{{background:#f0f0f0;border-left:4px solid #999;padding:16px;margin:20px 0;border-radius:4px;}}
table{{width:100%;border-collapse:collapse;margin-top:10px;}}
th,td{{text-align:left;padding:8px;border-bottom:1px solid #ccc;}}
th{{background:#e0e0e0;}}
.nota-final{{background:#dff0d8;border-left:4px solid #5cb85c;padding:16px;margin-top:20px;border-radius:4px;font-weight:bold;}}
.parecer{{font-style:italic;color:#444;}}
</style>
</head>
<body>
<div class="container">
{HTML_HEADER}
<p>Prezado(a) autor(a),</p>
<p>Seu trabalho foi <strong>aprovado</strong> na avaliação da VII SEMPI.</p>

<div class="box">
<h3>Avaliador(a) I - {data_i}</h3>
<table>
<tr><th>Critério</th><th>Nota</th><th>Peso</th></tr>
{"".join(f'<tr><td>{i+1}. {c}</td><td>{formatar_nota_br(notas_i[c])}</td><td>{pesos_criterios[i]}</td></tr>' for i,c in enumerate(nomes_criterios))}
</table>
<p class="parecer">{parecer_i}</p>
</div>

<div class="box">
<h3>Avaliador(a) II - {data_ii}</h3>
<table>
<tr><th>Critério</th><th>Nota</th><th>Peso</th></tr>
{"".join(f'<tr><td>{i+1}. {c}</td><td>{formatar_nota_br(notas_ii[c])}</td><td>{pesos_criterios[i]}</td></tr>' for i,c in enumerate(nomes_criterios))}
</table>
<p class="parecer">{parecer_ii}</p>
</div>

<div class="nota-final">Nota Final: {formatar_nota_br(nota_final,2)}</div>
</div>
</body>
</html>"""
        st.code(html_aprovacao, language="html")

    # ---------------- REPROVAÇÃO ----------------
    elif aba == "❌ Reprovação":
        st.header("Reprovação")

        # Podemos reutilizar as entradas de notas e pareceres
        st.subheader("Avaliador(a) I")
        parecer_i_rep = st.text_area("Parecer Avaliador(a) I", value='"Parecer de reprovação."', key="parecer_i_rep")
        st.subheader("Avaliador(a) II")
        parecer_ii_rep = st.text_area("Parecer Avaliador(a) II", value='"Parecer de reprovação."', key="parecer_ii_rep")

        html_reprovacao = f"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<style>
body{{font-family:Arial,sans-serif;line-height:1.6;color:#333;}}
.container{{max-width:700px;margin:auto;padding:20px;}}
.box{{background:#f0f0f0;border-left:4px solid #999;padding:16px;margin:20px 0;border-radius:4px;}}
.parecer{{font-style:italic;color:#444;}}
</style>
</head>
<body>
<div class="container">
{HTML_HEADER}
<p>Prezado(a) autor(a),</p>
<p>Seu trabalho <strong>não foi aprovado</strong> na avaliação da VII SEMPI.</p>

<div class="box">
<h3>Avaliador(a) I</h3>
<p class="parecer">{parecer_i_rep}</p>
</div>

<div class="box">
<h3>Avaliador(a) II</h3>
<p class="parecer">{parecer_ii_rep}</p>
</div>
</div>
</body>
</html>
"""
        st.code(html_reprovacao, language="html")

    # ---------------- LEMBRETES ----------------
    elif aba == "🔔 Lembretes":
        st.header("Lembretes de submissão e apresentação")
        st.markdown("**HTML de lembrete de envio:**")
        st.code(LEMBRETE_ENVIO_HTML, language="html")
        st.markdown("**HTML de lembrete de apresentação:**")
        st.code(LEMBRETE_APRESENTACAO_HTML, language="html")

    # ---------------- RESULTADO FINAL ----------------
    elif aba == "🏆 Resultado final":
        st.header("Resultado Final Consolidado")
        st.info("HTML consolidado combinando todos os dados de avaliação e notas com pesos.")
        # Aqui podemos apenas exibir o HTML da aprovação, para simplificação
        st.code(html_aprovacao, language="html")

if __name__ == "__main__":
    main()
