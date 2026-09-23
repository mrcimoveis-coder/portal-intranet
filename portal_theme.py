def render_portal() -> str:
    html = r"""
<style>
:root {
  --mrc-red:#c4001a; --mrc-red-dark:#950014; --navy:#172033; --ink:#252a34;
  --muted:#667085; --line:#e2e6eb; --surface:#ffffff; --canvas:#f4f6f8;
}
* { box-sizing:border-box; }
html { scroll-behavior:smooth; }
body { background:var(--canvas); }
.mrc-shell { min-height:100vh; background:var(--canvas); color:var(--ink); font-family:Inter,"Segoe UI",Arial,sans-serif; }
.mrc-topbar { background:var(--navy); color:#fff; padding:14px 5.5vw; display:flex; align-items:center; justify-content:space-between; gap:24px; }
.mrc-brand { display:flex; align-items:center; gap:18px; }
.mrc-brand img { width:168px; height:56px; object-fit:contain; background:#fff; border-radius:8px; padding:5px 9px; }
.mrc-brand-copy b { display:block; font-size:15px; letter-spacing:.02em; }
.mrc-brand-copy span { color:#b7c0ce; font-size:12px; }
.mrc-nav { display:flex; gap:8px; flex-wrap:wrap; }
.mrc-nav a { color:#dbe1e9!important; text-decoration:none; font-size:13px; font-weight:600; padding:9px 12px; border-radius:7px; }
.mrc-nav a:hover { background:rgba(255,255,255,.09); color:#fff!important; }
.mrc-hero { background:linear-gradient(118deg,#fff 0%,#fff 58%,#f5e9eb 100%); border-bottom:1px solid var(--line); padding:46px 5.5vw 40px; }
.mrc-eyebrow { color:var(--mrc-red); text-transform:uppercase; letter-spacing:.14em; font-size:11px; font-weight:800; }
.mrc-hero h1 { color:var(--navy); margin:10px 0 8px; font-size:clamp(29px,4vw,46px); line-height:1.08; letter-spacing:-.035em; }
.mrc-hero p { max-width:720px; margin:0; color:var(--muted); font-size:16px; line-height:1.6; }
.mrc-status { margin-top:20px; display:inline-flex; align-items:center; gap:8px; background:#fff; border:1px solid var(--line); border-radius:99px; padding:8px 12px; font-size:12px; color:#475467; }
.mrc-status i { width:8px; height:8px; background:#2e9d5b; border-radius:50%; box-shadow:0 0 0 3px #dff3e7; }
.mrc-main { padding:34px 5.5vw 55px; max-width:1600px; margin:0 auto; }
.section-head { display:flex; align-items:end; justify-content:space-between; gap:20px; margin-bottom:17px; }
.section-head h2 { margin:0; color:var(--navy); font-size:22px; letter-spacing:-.015em; }
.section-head p { margin:4px 0 0; color:var(--muted); font-size:13px; }
.quick-grid { display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:16px; margin-bottom:40px; }
.quick-card { position:relative; display:flex; flex-direction:column; min-height:174px; padding:21px; border:1px solid var(--line); border-radius:14px; background:var(--surface); color:var(--ink)!important; text-decoration:none!important; box-shadow:0 5px 18px rgba(16,24,40,.05); overflow:hidden; transition:.18s ease; }
.quick-card:before { content:""; position:absolute; inset:0 auto 0 0; width:4px; background:var(--mrc-red); }
.quick-card:hover { transform:translateY(-3px); box-shadow:0 12px 28px rgba(16,24,40,.10); border-color:#cfd4dc; }
.card-icon { width:43px; height:43px; border-radius:10px; display:grid; place-items:center; background:#f7eaec; color:var(--mrc-red); font-size:21px; margin-bottom:18px; }
.quick-card b { font-size:16px; color:var(--navy); }
.quick-card small { color:var(--muted); line-height:1.4; margin-top:6px; }
.quick-card em { margin-top:auto; padding-top:16px; color:var(--mrc-red); font-size:12px; font-style:normal; font-weight:800; }
.resource-layout { display:grid; grid-template-columns:1.3fr .85fr .95fr; gap:18px; align-items:start; }
.resource-group { background:#fff; border:1px solid var(--line); border-radius:14px; overflow:hidden; box-shadow:0 3px 12px rgba(16,24,40,.035); }
.resource-title { padding:19px 20px 15px; border-bottom:1px solid var(--line); }
.resource-title span { display:inline-block; color:var(--mrc-red); font-size:10px; text-transform:uppercase; letter-spacing:.12em; font-weight:800; margin-bottom:5px; }
.resource-title h3 { margin:0; color:var(--navy); font-size:17px; }
.resource-list { padding:8px; }
.resource-link { display:flex; align-items:center; gap:12px; padding:12px; border-radius:9px; text-decoration:none!important; color:var(--ink)!important; transition:.15s ease; }
.resource-link:hover { background:#f6f7f9; }
.resource-link .mini-icon { flex:0 0 36px; height:36px; display:grid; place-items:center; border-radius:8px; background:#f2f4f7; font-size:17px; }
.resource-link .copy { min-width:0; flex:1; }
.resource-link b { display:block; color:var(--navy); font-size:13.5px; }
.resource-link small { color:var(--muted); font-size:11.5px; line-height:1.35; }
.resource-link .arrow { color:#98a2b3; font-size:17px; }
.manual-new { margin-left:7px; color:#fff; background:var(--mrc-red); border-radius:99px; padding:2px 6px; font-size:8px; letter-spacing:.06em; vertical-align:2px; }
.mrc-footer { padding:20px 5.5vw; border-top:1px solid var(--line); color:#7b8492; background:#fff; font-size:12px; display:flex; justify-content:space-between; gap:20px; }
@media (max-width:1100px) { .quick-grid{grid-template-columns:repeat(2,1fr)} .resource-layout{grid-template-columns:1fr 1fr}.resource-group:last-child{grid-column:1/-1} }
@media (max-width:720px) { .mrc-topbar{align-items:flex-start;flex-direction:column}.mrc-nav{width:100%}.mrc-hero{padding-top:34px}.quick-grid,.resource-layout{grid-template-columns:1fr}.resource-group:last-child{grid-column:auto}.mrc-footer{flex-direction:column}.mrc-brand img{width:145px} }
</style>
<div class="mrc-shell">
  <header class="mrc-topbar">
    <div class="mrc-brand">
      <img src="https://raw.githubusercontent.com/mrcimoveis-coder/portal-intranet/main/logo.jpeg" alt="MRC Imóveis">
      <div class="mrc-brand-copy"><b>Portal Corporativo</b><span>Ambiente interno de trabalho</span></div>
    </div>
    <nav class="mrc-nav"><a href="#rapidos">Acessos rápidos</a><a href="#recursos">Aplicativos</a><a href="#manuais">Manuais</a></nav>
  </header>

  <section class="mrc-hero">
    <div class="mrc-eyebrow">MRC Imóveis · Intranet</div>
    <h1>Central de trabalho MRC</h1>
    <p>Sistemas, cadastros e procedimentos reunidos em um ambiente simples, seguro e organizado para a rotina da equipe.</p>
    <div class="mrc-status"><i></i> Portal operacional disponível</div>
  </section>

  <main class="mrc-main">
    <section id="rapidos">
      <div class="section-head"><div><h2>Acessos rápidos</h2><p>Ferramentas mais utilizadas no dia a dia.</p></div></div>
      <div class="quick-grid">
        <a class="quick-card" href="https://financeiro-mrc-mrcimoveis.streamlit.app/" target="_blank"><span class="card-icon">▥</span><b>Financeiro MRC</b><small>Previsão, saldos, pendências e distribuição.</small><em>Acessar sistema →</em></a>
        <a class="quick-card" href="https://superlogica.net/clients/?licenca=mrcimob" target="_blank"><span class="card-icon">◫</span><b>Superlógica</b><small>ERP para as rotinas da administração imobiliária.</small><em>Acessar sistema →</em></a>
        <a class="quick-card" href="https://caucoes-mrc-mrcimoveis.streamlit.app/" target="_blank"><span class="card-icon">◇</span><b>Gestão de Cauções</b><small>Depósitos, devoluções, reajustes e projeções.</small><em>Acessar sistema →</em></a>
        <a class="quick-card" href="https://carteira-imoveis-mrcimoveis.streamlit.app/" target="_blank"><span class="card-icon">⌂</span><b>Carteira de Imóveis</b><small>Gestão comercial e consulta do acervo.</small><em>Acessar sistema →</em></a>
      </div>
    </section>

    <section id="recursos">
      <div class="section-head"><div><h2>Todos os recursos</h2><p>Navegue por área para localizar rapidamente o que precisa.</p></div></div>
      <div class="resource-layout">
        <article class="resource-group">
          <div class="resource-title"><span>Operação</span><h3>Sistemas e aplicativos</h3></div>
          <div class="resource-list">
            <a class="resource-link" href="https://financeiro-mrc-mrcimoveis.streamlit.app/" target="_blank"><span class="mini-icon">▥</span><span class="copy"><b>Financeiro MRC</b><small>Receitas, despesas e projeções.</small></span><span class="arrow">›</span></a>
            <a class="resource-link" href="https://caucoes-mrc-mrcimoveis.streamlit.app/" target="_blank"><span class="mini-icon">◇</span><span class="copy"><b>Gestão de Cauções</b><small>Garantias, reajustes e devoluções.</small></span><span class="arrow">›</span></a>
            <a class="resource-link" href="https://conferencia-boletos-mrc.streamlit.app/" target="_blank"><span class="mini-icon">✓</span><span class="copy"><b>Conferência de Boletos</b><small>Validação operacional de cobranças.</small></span><span class="arrow">›</span></a>
            <a class="resource-link" href="https://calculo-encerramento-mrc.streamlit.app/" target="_blank"><span class="mini-icon">∑</span><span class="copy"><b>Cálculo de Encerramento</b><small>Apuração para término de contratos.</small></span><span class="arrow">›</span></a>
            <a class="resource-link" href="https://superlogica.net/clients/?licenca=mrcimob" target="_blank"><span class="mini-icon">◫</span><span class="copy"><b>Superlógica Imobiliária</b><small>Acesso ao ERP de gestão.</small></span><span class="arrow">›</span></a>
            <a class="resource-link" href="https://carteira-imoveis-mrcimoveis.streamlit.app/" target="_blank"><span class="mini-icon">⌂</span><span class="copy"><b>Carteira de Imóveis</b><small>Gestão comercial e acervo.</small></span><span class="arrow">›</span></a>
            <a class="resource-link" href="https://app-condominios-mrcimoveis.streamlit.app/" target="_blank"><span class="mini-icon">▦</span><span class="copy"><b>Administração de Condomínios</b><small>Contatos e informações vinculadas.</small></span><span class="arrow">›</span></a>
          </div>
        </article>

        <article class="resource-group">
          <div class="resource-title"><span>Cadastros</span><h3>Fichas cadastrais</h3></div>
          <div class="resource-list">
            <a class="resource-link" href="https://pf.163-176-88-73.nip.io/" target="_blank"><span class="mini-icon">PF</span><span class="copy"><b>Pessoa Física</b><small>Cadastro de inquilino e fiador.</small></span><span class="arrow">›</span></a>
            <a class="resource-link" href="https://pj.163-176-88-73.nip.io/" target="_blank"><span class="mini-icon">PJ</span><span class="copy"><b>Pessoa Jurídica</b><small>Cadastro para locação empresarial.</small></span><span class="arrow">›</span></a>
            <a class="resource-link" href="https://proprietario.163-176-88-73.nip.io/" target="_blank"><span class="mini-icon">⌾</span><span class="copy"><b>Captação de Proprietário</b><small>Disponibilização de novo imóvel.</small></span><span class="arrow">›</span></a>
          </div>
        </article>

        <article class="resource-group" id="manuais">
          <div class="resource-title"><span>Conhecimento</span><h3>Manuais e procedimentos</h3></div>
          <div class="resource-list">
            <a class="resource-link" href="https://docs.google.com/gview?embedded=1&amp;url=https%3A%2F%2Fraw.githubusercontent.com%2Fmrcimoveis-coder%2Fportal-intranet%2Fmain%2FAluguel_Mensal_Guia_Operacional.pdf" target="_blank"><span class="mini-icon">PDF</span><span class="copy"><b>Aluguel Mensal - Guia Operacional <span class="manual-new">NOVO</span></b><small>Cobranças, reajustes, boletos e remessa bancária.</small></span><span class="arrow">›</span></a>
            <a class="resource-link" href="https://drive.google.com/file/d/1wFtdNO-tTefVfbUE3w2O_fKp9kk1lv40/view" target="_blank"><span class="mini-icon">PDF</span><span class="copy"><b>Sistema Financeiro MRC <span class="manual-new">NOVO</span></b><small>Saldos, baixas, forecast, cauções e distribuição.</small></span><span class="arrow">›</span></a>
            <a class="resource-link" href="https://docs.google.com/document/d/1wW0NCOBAMaFNL32pt55YqfEBCigRRm4LEwi37zMiOBE/preview" target="_blank"><span class="mini-icon">01</span><span class="copy"><b>Manual do Superlógica</b><small>Procedimentos e rotinas do sistema.</small></span><span class="arrow">›</span></a>
            <a class="resource-link" href="https://docs.google.com/document/d/1OVG0TWnb9Wa_Gv-1pyUWD8UU_UotIgTzBC46oKNY5bc/preview" target="_blank"><span class="mini-icon">02</span><span class="copy"><b>Procedimentos de Rescisão</b><small>Orientações para desocupação.</small></span><span class="arrow">›</span></a>
            <a class="resource-link" href="https://docs.google.com/document/d/1RCQzuVD8KMgQSKR80Kf5ZY1s4xrsmYhbklDuOONqtCU/preview" target="_blank"><span class="mini-icon">03</span><span class="copy"><b>Certidões de Venda</b><small>Emissão de CNDs e Ônus Reais.</small></span><span class="arrow">›</span></a>
          </div>
        </article>
      </div>
    </section>
  </main>
  <footer class="mrc-footer"><span>© 2026 MRC Imóveis · Uso interno</span><span>Portal Corporativo MRC</span></footer>
</div>
"""
    return "\n".join(line.lstrip() for line in html.splitlines())
