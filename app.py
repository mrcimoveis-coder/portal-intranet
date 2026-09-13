import streamlit as st

# 1. Configuração da página e Inserção do Ícone (Favicon) da MRC Imóveis
st.set_page_config(
    page_title="Intranet MRC Imóveis", 
    page_icon="https://raw.githubusercontent.com/mrcimoveis-coder/intranet/main/logo.jpeg", 
    layout="wide"
)

# 2. Ocultar o menu padrão do Streamlit para parecer um site próprio
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
.block-container {
    padding-top: 0rem; padding-bottom: 0rem; padding-left: 0rem; padding-right: 0rem;
    max-width: 100%;
}
</style>
""", unsafe_allow_html=True)

# 3. Definição da Senha de Acesso
SENHA_CORRETA = "431360"

if "autenticado_intranet" not in st.session_state:
    st.session_state.autenticado_intranet = False

# ==========================================
# TELA DE LOGIN (Se não estiver autenticado)
# ==========================================
if not st.session_state.autenticado_intranet:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.image("https://raw.githubusercontent.com/mrcimoveis-coder/intranet/main/logo.jpeg", width=260)
        st.title("🔒 Acesso à Intranet")
        st.write("Portal restrito aos colaboradores da MRC Imóveis.")
        
        senha_input = st.text_input("Digite a senha de acesso:", type="password")
        if st.button("Entrar", type="primary", use_container_width=True):
            if senha_input == SENHA_CORRETA:
                st.session_state.autenticado_intranet = True
                st.rerun()
            else:
                st.error("❌ Senha incorreta.")
    st.stop() # Bloqueia o carregamento do HTML para não autenticados

# ==========================================
# INTRANET CARREGADA (Com Menu Sanfona)
# ==========================================
# HTML sem recuos para evitar formatação de código do Streamlit
html_intranet = """
<style>
:root {
    --primary-red: #C4001A;
    --primary-hover: #900013;
    --dark-gray: #2B2B2B;
    --silver-gray: #6C757D;
    --light-bg: #F4F6F8;
    --card-bg: #FFFFFF;
}
#intranet-wrapper {
    font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    background-color: var(--light-bg);
    color: var(--dark-gray);
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}
.header-custom {
    background-color: #ffffff;
    border-bottom: 3px solid var(--primary-red);
    padding: 1.2rem 2rem;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}
.header-content-custom {
    max-width: 1200px; margin: 0 auto; display: flex; align-items: center; gap: 15px;
}
.header-content-custom img { max-height: 70px; width: auto; }
.portal-title-custom { font-size: 1.35rem; font-weight: 700; color: var(--dark-gray); border-left: 2px solid var(--silver-gray); padding-left: 15px; }
.main-custom { max-width: 1200px; margin: 40px auto; padding: 0 20px; flex: 1; width: 100%; }

/* Layout Base (Mantendo as 3 colunas em telas grandes) */
.dashboard-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 35px; align-items: start; }

/* Estilo do Menu Sanfona */
details.topic-column {
    background-color: transparent;
}
summary.topic-header {
    cursor: pointer;
    list-style: none; /* Remove a seta nativa padrão */
    position: relative;
    padding-bottom: 8px;
    border-bottom: 2px solid #E2E8F0;
    margin-bottom: 15px;
    outline: none;
}
summary.topic-header::-webkit-details-marker {
    display: none;
}
/* Seta customizada que gira */
summary.topic-header::after {
    content: '▼';
    position: absolute;
    right: 5px;
    top: 5px;
    font-size: 12px;
    color: var(--primary-red);
    transition: transform 0.3s ease;
}
details[open] summary.topic-header::after {
    transform: rotate(180deg);
}
.topic-header h2 { font-size: 1.3rem; color: var(--dark-gray); display: inline-block; margin: 0 0 5px 0;}
.topic-header p { color: var(--silver-gray); font-size: 0.85rem; margin: 0; padding-right: 20px;}

/* Animação do conteúdo da Sanfona */
.topic-content {
    animation: fadein 0.4s ease-out;
}
@keyframes fadein {
    from { opacity: 0; transform: translateY(-5px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* Cartões de Acesso */
.compact-card {
    text-decoration: none; background-color: var(--card-bg); border-top: 4px solid var(--primary-red);
    border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.05); padding: 15px;
    display: flex; align-items: center; justify-content: space-between; transition: all 0.2s; margin-bottom: 15px;
}
.compact-card:hover { transform: translateY(-3px); box-shadow: 0 5px 12px rgba(0,0,0,0.1); }
.compact-card-left { display: flex; align-items: center; gap: 12px; }
.compact-icon { font-size: 22px; background-color: #F8FAFC; padding: 8px; border-radius: 6px; min-width: 42px; text-align: center; }
.compact-info { display: flex; flex-direction: column; }
.compact-title { color: var(--dark-gray); font-weight: 600; font-size: 14px; }
.compact-subtitle { color: var(--silver-gray); font-size: 11.5px; margin-top: 3px; line-height: 1.2; }
.compact-action { color: var(--primary-red); font-size: 12px; font-weight: bold; white-space: nowrap; margin-left: 10px; }
.disabled-link { cursor: not-allowed; opacity: 0.8; }
.disabled-link .compact-action { color: var(--silver-gray); }
.footer-custom { text-align: center; padding: 20px; background-color: #ffffff; border-top: 1px solid #E2E8F0; color: var(--silver-gray); font-size: 0.85rem; margin-top: 30px; }
</style>

<div id="intranet-wrapper">
<div class="header-custom">
<div class="header-content-custom">
<img src="https://raw.githubusercontent.com/mrcimoveis-coder/intranet/main/logo.jpeg" alt="MRC Imóveis">
<span class="portal-title-custom">INTRANET</span>
</div>
</div>

<div class="main-custom">
<div class="dashboard-grid">

<!-- COLUNA 1: SISTEMAS (SANFONA) -->
<details class="topic-column" open>
<summary class="topic-header">
<h2>Sistemas e Aplicativos</h2>
<p>Acesso rápido às ferramentas operacionais.</p>
</summary>
<div class="topic-content">
<a href="https://conferencia-boletos-mrc.streamlit.app/" target="_blank" class="compact-card">
<div class="compact-card-left">
<span class="compact-icon">📄</span>
<div class="compact-info"><span class="compact-title">Conferência de Boletos</span><span class="compact-subtitle">Validação de dados e arquivos</span></div>
</div>
<span class="compact-action">Abrir &rarr;</span>
</a>
<a href="https://calculo-encerramento-mrc.streamlit.app/" target="_blank" class="compact-card">
<div class="compact-card-left">
<span class="compact-icon">🧮</span>
<div class="compact-info"><span class="compact-title">Cálculo de Encerramento</span><span class="compact-subtitle">Conferência de rescisões</span></div>
</div>
<span class="compact-action">Abrir &rarr;</span>
</a>
<a href="https://superlogica.net/clients/?licenca=mrcimob" target="_blank" class="compact-card">
<div class="compact-card-left">
<span class="compact-icon">🏢</span>
<div class="compact-info"><span class="compact-title">Superlógica Imobiliária</span><span class="compact-subtitle">Acesso ao ERP de gestão</span></div>
</div>
<span class="compact-action">Abrir &rarr;</span>
</a>
<a href="https://carteira-imoveis-mrcimoveis.streamlit.app/" target="_blank" class="compact-card">
<div class="compact-card-left">
<span class="compact-icon">📊</span>
<div class="compact-info"><span class="compact-title">Carteira de Imóveis</span><span class="compact-subtitle">Gestão comercial e acervo</span></div>
</div>
<span class="compact-action">Abrir &rarr;</span>
</a>
</div>
</details>

<!-- COLUNA 2: FICHAS CADASTRAIS (SANFONA) -->
<details class="topic-column" open>
<summary class="topic-header">
<h2>Fichas Cadastrais</h2>
<p>Links para envio de cadastros à imobiliária.</p>
</summary>
<div class="topic-content">
<a href="https://cadastro-pf-mrcimoveis.streamlit.app/" target="_blank" class="compact-card">
<div class="compact-card-left">
<span class="compact-icon">📝</span>
<div class="compact-info"><span class="compact-title">Ficha Pessoa Física (PF)</span><span class="compact-subtitle">Cadastro de inquilino e fiador</span></div>
</div>
<span class="compact-action">Abrir &rarr;</span>
</a>
<a href="https://cadastro-pj-mrcimoveis.streamlit.app/" target="_blank" class="compact-card">
<div class="compact-card-left">
<span class="compact-icon">💼</span>
<div class="compact-info"><span class="compact-title">Ficha Pessoa Jurídica (PJ)</span><span class="compact-subtitle">Locação para empresas</span></div>
</div>
<span class="compact-action">Abrir &rarr;</span>
</a>
<a href="https://cadastro-proprietario-mrcimoveis.streamlit.app/" target="_blank" class="compact-card">
<div class="compact-card-left">
<span class="compact-icon">🔑</span>
<div class="compact-info"><span class="compact-title">Captação Proprietário</span><span class="compact-subtitle">Disponibilizar novo imóvel</span></div>
</div>
<span class="compact-action">Abrir &rarr;</span>
</a>
</div>
</details>

<!-- COLUNA 3: MANUAIS (SANFONA) -->
<details class="topic-column" open>
<summary class="topic-header">
<h2>Manuais e Procedimentos</h2>
<p>Guias e normas internas para a equipe.</p>
</summary>
<div class="topic-content">
<a href="#" class="compact-card disabled-link" onclick="event.preventDefault();">
<div class="compact-card-left">
<span class="compact-icon">📘</span>
<div class="compact-info"><span class="compact-title">Manual de Locação</span><span class="compact-subtitle">Regras e políticas internas</span></div>
</div>
<span class="compact-action">Em breve &rarr;</span>
</a>
<a href="#" class="compact-card disabled-link" onclick="event.preventDefault();">
<div class="compact-card-left">
<span class="compact-icon">📋</span>
<div class="compact-info"><span class="compact-title">Procedimento de Vistoria</span><span class="compact-subtitle">Passo a passo padrão</span></div>
</div>
<span class="compact-action">Em breve &rarr;</span>
</a>
</div>
</details>

</div>
</div>

<div class="footer-custom">
&copy; Intranet MRC Imóveis — Todos os direitos reservados.
</div>
</div>
"""

# Renderiza o HTML dentro do Streamlit de forma limpa e tela cheia
st.markdown(html_intranet, unsafe_allow_html=True)
