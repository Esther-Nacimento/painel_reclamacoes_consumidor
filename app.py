import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================
st.set_page_config(
    page_title="Painel de Reclamações de Consumidores",
    page_icon="📊",
    layout="wide"
)

# =========================================================
# ESTILO VISUAL DO DASHBOARD
# =========================================================
st.markdown(
    """
    <style>
        :root {
            --grafite: #17202A;
            --grafite-2: #25313F;
            --azul: #2B6CB0;
            --teal: #0F766E;
            --coral: #D95F43;
            --ambar: #D99A27;
            --lilas: #7C3AED;
            --menta: #DBF5EF;
            --fundo: #F6F8FB;
            --linha: #E2E8F0;
            --branco: #FFFFFF;
            --texto: #1E293B;
            --texto-suave: #64748B;
        }

        .stApp {
            background:
                linear-gradient(180deg, #F6F8FB 0%, #FFFFFF 42%, #F6F8FB 100%);
            color: var(--texto);
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2.5rem;
            max-width: 1320px;
        }

        [data-testid="stSidebar"] {
            background: #17202A;
            border-right: 1px solid rgba(255, 255, 255, 0.10);
        }

        [data-testid="stSidebar"] [data-testid="stSidebarUserContent"] {
            padding-top: 2rem;
        }

        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] span {
            color: #FFFFFF !important;
        }

        [data-testid="stSidebar"] h1 {
            font-size: 28px;
            margin-bottom: 1.4rem;
        }

        [data-testid="stSidebar"] label {
            font-weight: 700;
            margin-bottom: 0.2rem;
        }

        [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
            gap: 0.85rem;
        }

        [data-testid="stSidebar"] .stCaptionContainer {
            color: rgba(255, 255, 255, 0.72) !important;
        }

        [data-testid="stSidebar"] input,
        [data-testid="stSidebar"] textarea,
        [data-testid="stSidebar"] select {
            color: #111827 !important;
        }

        [data-testid="stSidebar"] [data-baseweb="select"] > div,
        [data-testid="stSidebar"] [data-baseweb="input"] > div {
            border-radius: 8px;
            border-color: rgba(255, 255, 255, 0.18);
            box-shadow: none;
        }

        [data-testid="stSidebar"] [data-baseweb="tag"] {
            background-color: #0F766E !important;
            border-radius: 6px !important;
        }

        [data-testid="stSidebar"] [data-baseweb="tag"] span {
            color: #FFFFFF !important;
        }

        [data-testid="stWidgetLabel"] p {
            color: var(--texto) !important;
            font-weight: 700;
            font-size: 14px;
        }

        [data-baseweb="select"] > div,
        [data-baseweb="input"] > div {
            background: #FFFFFF !important;
            border: 1px solid var(--linha) !important;
            border-radius: 8px !important;
            box-shadow: 0 6px 18px rgba(15, 23, 42, 0.05);
        }

        [data-baseweb="select"] span,
        [data-baseweb="input"] input {
            color: var(--texto) !important;
        }

        [data-baseweb="select"] * {
            color: var(--texto) !important;
            opacity: 1 !important;
        }

        .hero-card {
            background:
                linear-gradient(135deg, rgba(23, 32, 42, 0.98) 0%, rgba(37, 49, 63, 0.96) 56%, rgba(15, 118, 110, 0.92) 100%);
            padding: 34px 38px 30px;
            border-radius: 8px;
            color: white;
            box-shadow: 0 20px 48px rgba(15, 23, 42, 0.20);
            margin-bottom: 18px;
            border: 1px solid rgba(255, 255, 255, 0.12);
        }

        .hero-title {
            font-size: 36px;
            font-weight: 850;
            letter-spacing: 0;
            margin-bottom: 10px;
            max-width: 850px;
        }

        .hero-subtitle {
            font-size: 16px;
            line-height: 1.65;
            opacity: 0.92;
            max-width: 980px;
        }

        .hero-badges {
            margin-top: 24px;
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }

        .hero-badge {
            background: rgba(255, 255, 255, 0.11);
            border: 1px solid rgba(255, 255, 255, 0.18);
            padding: 7px 11px;
            border-radius: 8px;
            font-size: 13px;
            font-weight: 650;
            color: #FFFFFF;
        }

        .intro-card {
            background: #FFFFFF;
            border: 1px solid var(--linha);
            border-left: 5px solid var(--teal);
            padding: 17px 20px;
            border-radius: 8px;
            box-shadow: 0 10px 26px rgba(15, 23, 42, 0.06);
            margin-bottom: 24px;
            color: var(--texto);
        }

        .section-title {
            color: var(--grafite);
            font-size: 25px;
            font-weight: 800;
            margin-bottom: 5px;
        }

        .section-subtitle {
            color: var(--texto-suave);
            font-size: 15px;
            line-height: 1.55;
            margin-bottom: 18px;
            max-width: 960px;
        }

        .texto-apoio {
            color: var(--texto-suave);
            font-size: 14px;
            line-height: 1.55;
            margin: 0 0 12px 0;
            max-width: 760px;
        }

        .metric-card {
            background: #FFFFFF;
            border: 1px solid var(--linha);
            padding: 18px 18px 16px;
            border-radius: 8px;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.06);
            min-height: 124px;
            position: relative;
            overflow: hidden;
        }

        .metric-card::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            height: 4px;
            width: 100%;
            background: linear-gradient(90deg, var(--teal), var(--azul), var(--coral), var(--ambar));
        }

        .metric-label {
            font-size: 13px;
            color: var(--texto-suave);
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.04em;
            margin-bottom: 9px;
        }

        .metric-value {
            font-size: 30px;
            color: var(--grafite);
            font-weight: 850;
            line-height: 1.05;
        }

        .metric-help {
            font-size: 13px;
            color: var(--texto-suave);
            margin-top: 9px;
            line-height: 1.35;
        }

        .empresa-destaque {
            background: linear-gradient(135deg, var(--grafite) 0%, #25415A 58%, var(--teal) 100%);
            color: #FFFFFF;
            padding: 22px;
            border-radius: 8px;
            box-shadow: 0 16px 34px rgba(15, 23, 42, 0.16);
            margin-bottom: 18px;
        }

        .empresa-destaque h3 {
            color: #FFFFFF !important;
            font-size: 24px;
            margin-bottom: 6px;
        }

        .empresa-destaque p {
            color: rgba(255, 255, 255, 0.90);
            font-size: 15px;
            line-height: 1.55;
            margin-bottom: 0;
        }

        h1, h2, h3 {
            color: var(--grafite);
            letter-spacing: 0;
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            border-bottom: 1px solid var(--linha);
        }

        .stTabs [data-baseweb="tab"] {
            background: #FFFFFF;
            border: 1px solid var(--linha);
            border-bottom: 0;
            border-radius: 8px 8px 0 0;
            padding: 10px 16px;
            color: var(--texto-suave);
            font-weight: 700;
        }

        .stTabs [aria-selected="true"] {
            color: var(--grafite) !important;
            box-shadow: inset 0 3px 0 var(--teal);
        }

        [data-testid="stMetricValue"] {
            color: var(--grafite);
        }

        div[data-testid="stDataFrame"] {
            border-radius: 8px;
            overflow: hidden;
            border: 1px solid var(--linha);
        }

        div[data-testid="stPlotlyChart"] {
            background: #FFFFFF;
            border: 1px solid var(--linha);
            border-radius: 8px;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.06);
            padding: 8px;
            margin-top: 8px;
        }

        .stDownloadButton button {
            border-radius: 8px;
            border: 1px solid var(--grafite);
            background: var(--grafite);
            color: white;
            font-weight: 700;
            padding: 0.55rem 1rem;
        }

        .stDownloadButton button:hover {
            border-color: var(--teal);
            background: var(--teal);
            color: white;
        }

        .rodape {
            margin-top: 24px;
            padding: 16px 20px;
            border-radius: 8px;
            background: #FFFFFF;
            border: 1px solid var(--linha);
            color: var(--texto-suave);
            font-size: 13px;
            line-height: 1.5;
        }

        @media (max-width: 900px) {
            .block-container {
                padding-top: 1rem;
            }

            .hero-card {
                padding: 24px;
            }

            .hero-title {
                font-size: 28px;
            }
        }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# FUNÇÕES AUXILIARES
# =========================================================
def formatar_numero(valor):
    try:
        return f"{int(valor):,}".replace(",", ".")
    except Exception:
        return "0"


def formatar_nota(valor):
    if pd.isna(valor):
        return "Sem nota"
    return f"{valor:.2f}".replace(".", ",")


def contar_classificacao(df_dados, classificacao):
    if df_dados.empty or "classificacao" not in df_dados.columns:
        return 0
    return int((df_dados["classificacao"] == classificacao).sum())


def abreviar_texto(valor, limite=46):
    valor = str(valor)
    if len(valor) <= limite:
        return valor
    return valor[: limite - 3].rstrip() + "..."


CORES_GRAFICOS = ["#0F766E", "#2B6CB0", "#D95F43", "#D99A27", "#7C3AED", "#475569", "#14B8A6", "#64748B"]
ESCALA_CONTINUA = ["#DBF5EF", "#79C7B8", "#2B6CB0", "#17202A"]


def aplicar_layout_grafico(fig, altura, margem=None):
    fig.update_layout(
        height=altura,
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(family="Inter, Arial, sans-serif", color="#334155", size=13),
        margin=margem or dict(l=8, r=8, t=18, b=8),
        xaxis=dict(
            title=None,
            showgrid=True,
            gridcolor="rgba(148, 163, 184, 0.22)",
            zeroline=False
        ),
        yaxis=dict(
            title=None,
            showgrid=False,
            zeroline=False
        ),
        hoverlabel=dict(
            bgcolor="#17202A",
            bordercolor="#17202A",
            font_color="#FFFFFF"
        )
    )
    fig.update_traces(
        textfont=dict(color="#17202A", size=12)
    )
    fig.update_xaxes(tickfont=dict(color="#64748B", size=12), automargin=True)
    fig.update_yaxes(tickfont=dict(color="#475569", size=11), automargin=True)
    return fig


def aplicar_rotulos_externos(fig, valores, orientacao="h"):
    maior_valor = pd.Series(valores).max()
    limite = maior_valor * 1.32 if maior_valor and maior_valor > 0 else 1

    fig.update_traces(
        textposition="outside",
        textangle=0,
        cliponaxis=False,
        textfont=dict(color="#17202A", size=12)
    )

    if orientacao == "h":
        fig.update_xaxes(range=[0, limite])
    else:
        fig.update_yaxes(range=[0, limite])

    return fig


def card_indicador(titulo, valor, descricao):
    st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-label">{titulo}</div>
            <div class="metric-value">{valor}</div>
            <div class="metric-help">{descricao}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def texto_apoio(texto):
    st.markdown(f'<div class="texto-apoio">{texto}</div>', unsafe_allow_html=True)


@st.cache_data
def carregar_dados():
    caminho_arquivo = Path(__file__).parent / "dados" / "reclamacoes_painel.csv"
    df = pd.read_csv(caminho_arquivo)

    df["data_abertura"] = pd.to_datetime(df["data_abertura"], errors="coerce")
    df["nota_satisfacao"] = pd.to_numeric(df["nota_satisfacao"], errors="coerce")

    if "ano" not in df.columns:
        df["ano"] = df["data_abertura"].dt.year
    if "mes" not in df.columns:
        df["mes"] = df["data_abertura"].dt.month

    colunas_texto = [
        "empresa", "estado", "cidade", "segmento", "area",
        "assunto", "problema", "classificacao"
    ]

    for coluna in colunas_texto:
        if coluna in df.columns:
            df[coluna] = df[coluna].fillna("Não informado").astype(str).str.strip()

    df = df.dropna(subset=["data_abertura"])
    return df


# =========================================================
# CARREGAMENTO DOS DADOS
# =========================================================
df = carregar_dados()

# =========================================================
# CABEÇALHO
# =========================================================
st.markdown(
    """
    <div class="hero-card">
        <div class="hero-title">Painel de Análise de Reclamações de Consumidores</div>
        <div class="hero-subtitle">
            Painel interativo para consulta de reclamações registradas no Consumidor.gov.br
            entre janeiro e abril de 2026. Os indicadores ajudam a identificar empresas,
            temas recorrentes, distribuição territorial e avaliação de satisfação dos consumidores.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="intro-card">
        <b>Sobre o painel:</b> este trabalho organiza reclamações registradas no Consumidor.gov.br
        em indicadores de volume, recorrência, localização e satisfação. O objetivo é apoiar a
        leitura dos dados: identificar quais problemas aparecem com mais frequência, quais empresas
        concentram mais registros e como as avaliações dos consumidores se distribuem no período.
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# OPÇÕES DE CONSULTA
# =========================================================
empresas = sorted(df["empresa"].dropna().unique())
opcoes_empresas = ["Todas as empresas"] + empresas

estados = sorted(df["estado"].dropna().unique())
opcoes_estados = ["Todos os estados"] + estados

areas = sorted(df["area"].dropna().unique())
opcoes_areas = ["Todas as áreas"] + areas

classificacoes = sorted(df["classificacao"].dropna().unique())
opcoes_classificacoes = ["Todas as classificações"] + classificacoes

min_data = df["data_abertura"].min().date()
max_data = df["data_abertura"].max().date()

# A aba Panorama usa todos os registros carregados.
df_filtrado = df.copy()

total_reclamacoes = len(df_filtrado)
total_empresas = df_filtrado["empresa"].nunique() if not df_filtrado.empty else 0
total_estados = df_filtrado["estado"].nunique() if not df_filtrado.empty else 0
nota_media = df_filtrado["nota_satisfacao"].mean() if not df_filtrado.empty else None
total_resolvidas = contar_classificacao(df_filtrado, "Resolvida")
total_nao_resolvidas = contar_classificacao(df_filtrado, "Não Resolvida")

if df_filtrado.empty:
    st.warning("Nenhum dado foi encontrado com os filtros selecionados. Ajuste os filtros para visualizar os resultados.")
else:
    # =========================================================
    # ABAS DO DASHBOARD
    # =========================================================
    aba_geral, aba_empresa = st.tabs([
        "Panorama",
        "Análise por empresa"
    ])

    # =========================================================
    # ABA 1 - PANORAMA
    # =========================================================
    with aba_geral:
        st.markdown('<div class="section-title">Indicadores principais</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="section-subtitle">Leitura inicial do conjunto analisado, antes dos filtros da consulta por empresa.</div>',
            unsafe_allow_html=True
        )

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            card_indicador(
                "Total de reclamações",
                formatar_numero(total_reclamacoes),
                "Volume de manifestações consideradas na análise."
            )
        with col2:
            card_indicador(
                "Reclamações resolvidas",
                formatar_numero(total_resolvidas),
                "Registros classificados como resolvidos."
            )
        with col3:
            card_indicador(
                "Não resolvidas",
                formatar_numero(total_nao_resolvidas),
                "Registros classificados como não resolvidos."
            )
        with col4:
            card_indicador(
                "Nota média de satisfação",
                formatar_nota(nota_media),
                "Resultado médio das avaliações informadas."
            )

        st.write("")

        st.markdown('<div class="section-title">Panorama das reclamações</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="section-subtitle">Esta visão reúne os principais sinais do período: concentração de reclamações por problema e fornecedor, variação mensal e perfil das classificações registradas.</div>',
            unsafe_allow_html=True
        )

        col_graf1, col_graf2 = st.columns(2)

        with col_graf1:
            st.subheader("Problemas mais frequentes")
            texto_apoio("Este ranking evidencia os motivos de reclamação mais recorrentes. Quanto maior a concentração em poucos problemas, mais claro fica onde estão os principais pontos de atrito na experiência do consumidor.")

            problemas = (
                df_filtrado["problema"]
                .value_counts()
                .head(10)
                .reset_index()
            )
            problemas.columns = ["problema", "total"]
            problemas["problema_resumo"] = problemas["problema"].apply(lambda valor: abreviar_texto(valor, 44))

            fig_problemas = px.bar(
                problemas,
                x="total",
                y="problema_resumo",
                orientation="h",
                text="total",
                color="total",
                color_continuous_scale=ESCALA_CONTINUA,
                labels={"total": "Reclamações", "problema_resumo": "Problema"},
                hover_data={"problema": True, "problema_resumo": False}
            )
            aplicar_layout_grafico(fig_problemas, 500)
            fig_problemas.update_layout(coloraxis_showscale=False, yaxis={"categoryorder": "total ascending"})
            aplicar_rotulos_externos(fig_problemas, problemas["total"], orientacao="h")
            st.plotly_chart(fig_problemas, use_container_width=True)

        with col_graf2:
            st.subheader("Empresas com mais reclamações")
            texto_apoio("O volume por empresa ajuda a identificar quais fornecedores aparecem com mais frequência nos registros. A leitura deve considerar que empresas maiores ou com mais clientes tendem a gerar mais interações.")

            empresas_rank = (
                df_filtrado["empresa"]
                .value_counts()
                .head(10)
                .reset_index()
            )
            empresas_rank.columns = ["empresa", "total"]
            empresas_rank["empresa_resumo"] = empresas_rank["empresa"].apply(lambda valor: abreviar_texto(valor, 34))

            fig_empresas = px.bar(
                empresas_rank,
                x="total",
                y="empresa_resumo",
                orientation="h",
                text="total",
                color="total",
                color_continuous_scale=ESCALA_CONTINUA,
                labels={"total": "Reclamações", "empresa_resumo": "Empresa"},
                hover_data={"empresa": True, "empresa_resumo": False}
            )
            aplicar_layout_grafico(fig_empresas, 500)
            fig_empresas.update_layout(coloraxis_showscale=False, yaxis={"categoryorder": "total ascending"})
            aplicar_rotulos_externos(fig_empresas, empresas_rank["total"], orientacao="h")
            st.plotly_chart(fig_empresas, use_container_width=True)

        col_graf3, col_graf4 = st.columns(2)

        with col_graf3:
            st.subheader("Evolução mensal")
            texto_apoio("A série mensal permite observar se as reclamações aumentaram, diminuíram ou permaneceram estáveis ao longo do período. Picos podem indicar eventos específicos, sazonalidade ou mudanças no atendimento.")

            reclamacoes_mes = (
                df_filtrado
                .groupby(["ano", "mes"])
                .size()
                .reset_index(name="total")
                .sort_values(["ano", "mes"])
            )
            reclamacoes_mes["periodo"] = (
                reclamacoes_mes["mes"].astype(int).astype(str).str.zfill(2) + "/" +
                reclamacoes_mes["ano"].astype(int).astype(str)
            )

            fig_mes = px.line(
                reclamacoes_mes,
                x="periodo",
                y="total",
                labels={"periodo": "Período", "total": "Reclamações"},
                markers=True
            )
            fig_mes.update_traces(
                line=dict(width=4, color="#0F766E"),
                marker=dict(size=10, color="#D95F43", line=dict(width=2, color="#FFFFFF"))
            )
            aplicar_layout_grafico(fig_mes, 390)
            st.plotly_chart(fig_mes, use_container_width=True)

        with col_graf4:
            st.subheader("Classificação das reclamações")
            texto_apoio("A classificação mostra como os registros foram categorizados após o atendimento. Essa distribuição ajuda a avaliar o desfecho das reclamações, não apenas a quantidade registrada.")

            classificacao_df = (
                df_filtrado["classificacao"]
                .value_counts()
                .reset_index()
            )
            classificacao_df.columns = ["classificacao", "total"]

            fig_class = px.pie(
                classificacao_df,
                names="classificacao",
                values="total",
                hole=0.55,
                color_discrete_sequence=CORES_GRAFICOS
            )
            fig_class.update_layout(
                height=390,
                paper_bgcolor="rgba(0,0,0,0)",
                font=dict(family="Inter, Arial, sans-serif", color="#334155", size=13),
                margin=dict(l=8, r=8, t=20, b=8),
                legend=dict(orientation="h", y=-0.10),
                hoverlabel=dict(bgcolor="#17202A", bordercolor="#17202A", font_color="#FFFFFF")
            )
            fig_class.update_traces(textinfo="percent+label", textfont_size=12, marker=dict(line=dict(color="#FFFFFF", width=2)))
            st.plotly_chart(fig_class, use_container_width=True)

        st.subheader("Leitura interpretativa")
        texto_apoio("A síntese abaixo combina volume, recorrência e satisfação para transformar os indicadores em uma leitura direta do cenário analisado.")

        problema_top = df_filtrado["problema"].value_counts().idxmax()
        empresa_top = df_filtrado["empresa"].value_counts().idxmax()
        estado_top = df_filtrado["estado"].value_counts().idxmax()

        texto_resumo = (
            f"Foram analisadas **{formatar_numero(total_reclamacoes)} reclamações** registradas entre "
            f"{min_data.strftime('%d/%m/%Y')} e {max_data.strftime('%d/%m/%Y')}. "
            f"Desse total, **{formatar_numero(total_resolvidas)}** foram classificadas como resolvidas e "
            f"**{formatar_numero(total_nao_resolvidas)}** como não resolvidas. "
            f"O tema mais recorrente foi **{problema_top}**, indicando uma demanda expressiva relacionada a esse tipo de ocorrência. "
            f"Entre os fornecedores, **{empresa_top}** concentrou o maior volume de registros. "
            f"A maior presença territorial aparece em **{estado_top}** e a nota média de satisfação ficou em **{formatar_nota(nota_media)}**."
        )
        st.info(texto_resumo)

    # =========================================================
    # ABA 2 - ANÁLISE POR EMPRESA
    # =========================================================
    with aba_empresa:
        st.markdown('<div class="section-title">Análise por empresa</div>', unsafe_allow_html=True)
        st.markdown(
            '<div class="section-subtitle">Use os filtros para comparar fornecedores ou aprofundar a análise de uma empresa específica. O recorte permite observar volume, localização, tipo de problema e satisfação dentro das condições selecionadas.</div>',
            unsafe_allow_html=True
        )

        filtro_col1, filtro_col2 = st.columns([2, 1])
        with filtro_col1:
            empresa_consulta = st.selectbox("Empresa", opcoes_empresas, key="empresa_consulta")
        with filtro_col2:
            estado_consulta = st.selectbox("Estado", opcoes_estados, key="estado_consulta")

        filtro_col3, filtro_col4, filtro_col5 = st.columns([1.3, 1.3, 1])
        with filtro_col3:
            area_consulta = st.selectbox("Área/segmento", opcoes_areas, key="area_consulta")
        with filtro_col4:
            classificacao_consulta = st.selectbox("Classificação", opcoes_classificacoes, key="classificacao_consulta")
        with filtro_col5:
            periodo_consulta = st.date_input(
                "Período",
                value=(min_data, max_data),
                min_value=min_data,
                max_value=max_data,
                key="periodo_consulta"
            )

        df_empresa_filtrado = df.copy()

        if empresa_consulta != "Todas as empresas":
            df_empresa_filtrado = df_empresa_filtrado[df_empresa_filtrado["empresa"] == empresa_consulta]

        if estado_consulta != "Todos os estados":
            df_empresa_filtrado = df_empresa_filtrado[df_empresa_filtrado["estado"] == estado_consulta]

        if area_consulta != "Todas as áreas":
            df_empresa_filtrado = df_empresa_filtrado[df_empresa_filtrado["area"] == area_consulta]

        if classificacao_consulta != "Todas as classificações":
            df_empresa_filtrado = df_empresa_filtrado[df_empresa_filtrado["classificacao"] == classificacao_consulta]

        if isinstance(periodo_consulta, tuple) and len(periodo_consulta) == 2:
            data_inicio = pd.to_datetime(periodo_consulta[0])
            data_fim = pd.to_datetime(periodo_consulta[1])
            df_empresa_filtrado = df_empresa_filtrado[
                (df_empresa_filtrado["data_abertura"] >= data_inicio) &
                (df_empresa_filtrado["data_abertura"] <= data_fim)
            ]

        st.write("")

        if df_empresa_filtrado.empty:
            st.warning("Nenhum registro foi encontrado para os filtros selecionados.")
        elif empresa_consulta == "Todas as empresas":
            st.markdown(
                f"""
                <div class="empresa-destaque">
                    <h3>Comparativo entre empresas</h3>
                    <p>Com a opção "Todas as empresas", a análise funciona como comparação entre fornecedores. Use os demais filtros para observar áreas, estados ou classificações específicas.</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            total_consulta = len(df_empresa_filtrado)
            empresas_consulta = df_empresa_filtrado["empresa"].nunique()
            estados_consulta = df_empresa_filtrado["estado"].nunique()
            nota_consulta = df_empresa_filtrado["nota_satisfacao"].mean()
            resolvidas_consulta = contar_classificacao(df_empresa_filtrado, "Resolvida")
            nao_resolvidas_consulta = contar_classificacao(df_empresa_filtrado, "Não Resolvida")

            c1, c2, c3, c4, c5 = st.columns(5)
            with c1:
                card_indicador("Reclamações filtradas", formatar_numero(total_consulta), "Volume considerado nesta consulta.")
            with c2:
                card_indicador("Resolvidas", formatar_numero(resolvidas_consulta), "Registros solucionados no recorte.")
            with c3:
                card_indicador("Não resolvidas", formatar_numero(nao_resolvidas_consulta), "Registros sem solução no recorte.")
            with c4:
                card_indicador("Nota média", formatar_nota(nota_consulta), "Avaliação média dos consumidores.")
            with c5:
                card_indicador("Empresas", formatar_numero(empresas_consulta), "Fornecedores presentes no resultado.")

            st.write("")
            col_comp1, col_comp2 = st.columns(2)

            with col_comp1:
                st.subheader("Empresas com mais reclamações")
                texto_apoio("O ranking permite comparar concentração de reclamações entre fornecedores. Ele não mede sozinho a qualidade do atendimento, mas aponta onde o volume de registros é mais alto dentro dos filtros escolhidos.")

                empresas_consulta_df = (
                    df_empresa_filtrado["empresa"]
                    .value_counts()
                    .head(10)
                    .reset_index()
                )
                empresas_consulta_df.columns = ["empresa", "total"]
                empresas_consulta_df["empresa_resumo"] = empresas_consulta_df["empresa"].apply(lambda valor: abreviar_texto(valor, 34))

                fig_empresas_consulta = px.bar(
                    empresas_consulta_df,
                    x="total",
                    y="empresa_resumo",
                    orientation="h",
                    text="total",
                    color="total",
                    color_continuous_scale=ESCALA_CONTINUA,
                    labels={"total": "Reclamações", "empresa_resumo": "Empresa"},
                    hover_data={"empresa": True, "empresa_resumo": False}
                )
                aplicar_layout_grafico(fig_empresas_consulta, 430)
                fig_empresas_consulta.update_layout(coloraxis_showscale=False, yaxis={"categoryorder": "total ascending"})
                aplicar_rotulos_externos(fig_empresas_consulta, empresas_consulta_df["total"], orientacao="h")
                st.plotly_chart(fig_empresas_consulta, use_container_width=True)

            with col_comp2:
                st.subheader("Áreas com mais registros")
                texto_apoio("A leitura por área mostra em quais setores as reclamações se concentram. Esse recorte ajuda a separar problemas de uma empresa específica de tendências de mercado.")

                areas_consulta_df = (
                    df_empresa_filtrado["area"]
                    .value_counts()
                    .head(10)
                    .reset_index()
                )
                areas_consulta_df.columns = ["area", "total"]
                areas_consulta_df["area_resumo"] = areas_consulta_df["area"].apply(lambda valor: abreviar_texto(valor, 34))

                fig_areas_consulta = px.bar(
                    areas_consulta_df,
                    x="total",
                    y="area_resumo",
                    orientation="h",
                    text="total",
                    color="total",
                    color_continuous_scale=ESCALA_CONTINUA,
                    labels={"total": "Reclamações", "area_resumo": "Área"},
                    hover_data={"area": True, "area_resumo": False}
                )
                aplicar_layout_grafico(fig_areas_consulta, 430)
                fig_areas_consulta.update_layout(coloraxis_showscale=False, yaxis={"categoryorder": "total ascending"})
                aplicar_rotulos_externos(fig_areas_consulta, areas_consulta_df["total"], orientacao="h")
                st.plotly_chart(fig_areas_consulta, use_container_width=True)

            empresa_top_recorte = df_empresa_filtrado["empresa"].value_counts().idxmax()
            area_top_recorte = df_empresa_filtrado["area"].value_counts().idxmax()

            st.subheader("Leitura do comparativo")
            st.info(
                f"A consulta reúne **{formatar_numero(total_consulta)} reclamações** de "
                f"**{formatar_numero(empresas_consulta)} empresas**. "
                f"Há **{formatar_numero(resolvidas_consulta)}** reclamações resolvidas e "
                f"**{formatar_numero(nao_resolvidas_consulta)}** não resolvidas. "
                f"O maior volume está associado a **{empresa_top_recorte}**, enquanto a área mais frequente é **{area_top_recorte}**. "
                f"Essa comparação ajuda a identificar concentração de registros antes de aprofundar a análise em um fornecedor específico."
            )
        else:
            titulo_empresa = empresa_consulta

            st.markdown(
                f"""
                <div class="empresa-destaque">
                    <h3>{titulo_empresa}</h3>
                    <p>Esta seção isola os registros da empresa selecionada para analisar volume, abrangência territorial, satisfação e problemas mais recorrentes.</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            total_empresa = len(df_empresa_filtrado)
            nota_empresa = df_empresa_filtrado["nota_satisfacao"].mean()
            estados_empresa = df_empresa_filtrado["estado"].nunique()
            resolvidas_empresa = contar_classificacao(df_empresa_filtrado, "Resolvida")
            nao_resolvidas_empresa = contar_classificacao(df_empresa_filtrado, "Não Resolvida")

            c1, c2, c3, c4, c5 = st.columns(5)
            with c1:
                card_indicador("Reclamações da empresa", formatar_numero(total_empresa), "Volume da empresa nos filtros atuais.")
            with c2:
                card_indicador("Resolvidas", formatar_numero(resolvidas_empresa), "Registros solucionados para a empresa.")
            with c3:
                card_indicador("Não resolvidas", formatar_numero(nao_resolvidas_empresa), "Registros sem solução para a empresa.")
            with c4:
                card_indicador("Nota média", formatar_nota(nota_empresa), "Avaliação média informada pelos consumidores.")
            with c5:
                card_indicador("Estados", formatar_numero(estados_empresa), "UFs com registros da empresa.")

            st.write("")
            col_emp1, col_emp2 = st.columns(2)

            with col_emp1:
                st.subheader("Principais problemas da empresa")
                texto_apoio("Este gráfico mostra quais temas aparecem com mais frequência para a empresa. A concentração em poucos problemas pode indicar gargalos específicos de atendimento, cobrança, contrato, entrega ou uso de dados.")

                problemas_empresa = (
                    df_empresa_filtrado["problema"]
                    .value_counts()
                    .head(8)
                    .reset_index()
                )
                problemas_empresa.columns = ["problema", "total"]
                problemas_empresa["problema_resumo"] = problemas_empresa["problema"].apply(lambda valor: abreviar_texto(valor, 44))

                fig_prob_emp = px.bar(
                    problemas_empresa,
                    x="total",
                    y="problema_resumo",
                    orientation="h",
                    text="total",
                    color="total",
                    color_continuous_scale=ESCALA_CONTINUA,
                    labels={"total": "Reclamações", "problema_resumo": "Problema"},
                    hover_data={"problema": True, "problema_resumo": False}
                )
                aplicar_layout_grafico(fig_prob_emp, 430)
                fig_prob_emp.update_layout(coloraxis_showscale=False, yaxis={"categoryorder": "total ascending"})
                aplicar_rotulos_externos(fig_prob_emp, problemas_empresa["total"], orientacao="h")
                st.plotly_chart(fig_prob_emp, use_container_width=True)

            with col_emp2:
                st.subheader("Estados com mais registros")
                texto_apoio("A distribuição por estado ajuda a observar onde a empresa teve maior presença de reclamações. Diferenças territoriais podem refletir tamanho da operação, concentração de clientes ou problemas regionais.")

                estados_empresa_df = (
                    df_empresa_filtrado["estado"]
                    .value_counts()
                    .head(8)
                    .reset_index()
                )
                estados_empresa_df.columns = ["estado", "total"]

                fig_est_emp = px.bar(
                    estados_empresa_df,
                    x="estado",
                    y="total",
                    text="total",
                    color="total",
                    color_continuous_scale=ESCALA_CONTINUA,
                    labels={"estado": "Estado", "total": "Reclamações"}
                )
                aplicar_layout_grafico(fig_est_emp, 430)
                fig_est_emp.update_layout(coloraxis_showscale=False)
                aplicar_rotulos_externos(fig_est_emp, estados_empresa_df["total"], orientacao="v")
                st.plotly_chart(fig_est_emp, use_container_width=True)

            st.subheader("Leitura da empresa")

            problema_empresa_top = df_empresa_filtrado["problema"].value_counts().idxmax()
            estado_empresa_top = df_empresa_filtrado["estado"].value_counts().idxmax()
            classificacao_top = df_empresa_filtrado["classificacao"].value_counts().idxmax()

            resumo_empresa = (
                f"Para **{titulo_empresa}**, a consulta retornou **{formatar_numero(total_empresa)} reclamações**. "
                f"Entre elas, **{formatar_numero(resolvidas_empresa)}** foram classificadas como resolvidas e "
                f"**{formatar_numero(nao_resolvidas_empresa)}** como não resolvidas. "
                f"O principal tema registrado foi **{problema_empresa_top}**, o que indica o ponto mais recorrente de insatisfação dentro dos filtros aplicados. "
                f"O maior volume territorial aparece em **{estado_empresa_top}**. "
                f"A classificação mais comum foi **{classificacao_top}** e a nota média de satisfação ficou em **{formatar_nota(nota_empresa)}**."
            )
            st.info(resumo_empresa)

# =========================================================
# RODAPÉ
# =========================================================
st.markdown(
    """
    <div class="rodape">
        <b>Fonte:</b> dados públicos do Consumidor.gov.br, referentes às reclamações analisadas no período selecionado. <br>
        <b>Tratamento:</b> registros organizados e padronizados previamente com SQL e DuckDB. <br>
        <b>Ferramentas de visualização:</b> painel desenvolvido em Python com Streamlit, Pandas e Plotly. <br>
        <b>Observação:</b> os indicadores têm finalidade informativa e devem ser interpretados considerando o período, os filtros aplicados e a quantidade de registros disponíveis.
    </div>
    """,
    unsafe_allow_html=True
)
