# -*- coding: utf-8 -*-
"""Gera o PDF da proposta de solução — base Treino Tracker, identidade GA."""
from weasyprint import HTML

OUT = "/home/user/GA_Business/saidas/proposta-treino-hipertrofia/proposta-treino-hipertrofia.pdf"
LOGO = "file:///home/user/GA_Business/identidade/logo_ga.png"

HTML_DOC = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;700&display=swap');

  @page {{
    size: A4;
    margin: 0;
  }}
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  html {{ -weasy-hyphens:none; }}

  body {{
    font-family:'Inter', sans-serif;
    background:#0c0a12;
    color:#ffffff;
    font-size:11px;
    line-height:1.55;
  }}

  .page {{
    position:relative;
    width:210mm;
    height:297mm;
    padding:20mm 18mm 16mm 18mm;
    background:#0c0a12;
    page-break-after:always;
    overflow:hidden;
    display:flex;
    flex-direction:column;
  }}
  .page:last-child {{ page-break-after:auto; }}

  /* grid de fundo assinatura */
  .grid-bg {{
    position:absolute; inset:0;
    background-image:
      linear-gradient(rgba(255,255,255,.04) 1px, transparent 1px),
      linear-gradient(90deg, rgba(255,255,255,.04) 1px, transparent 1px);
    background-size:64px 64px;
    -webkit-mask-image:radial-gradient(circle at 50% 0%, #000 30%, transparent 75%);
    mask-image:radial-gradient(circle at 50% 0%, #000 30%, transparent 75%);
    z-index:0;
  }}
  .glow {{
    position:absolute; top:-120px; left:50%; transform:translateX(-50%);
    width:520px; height:300px;
    background:radial-gradient(ellipse at center, rgba(212,175,55,.16), transparent 70%);
    z-index:0;
  }}
  .content {{ position:relative; z-index:1; flex:1 1 auto; }}

  /* tipografia */
  .label {{
    font-family:'JetBrains Mono', monospace;
    font-size:9.5px; letter-spacing:2.5px; text-transform:uppercase;
    color:#d4af37;
  }}
  .muted {{ color:#9a93a8; }}
  h1 {{ font-weight:900; font-size:30px; line-height:1.08; letter-spacing:-.5px; }}
  h2 {{ font-weight:800; font-size:18px; line-height:1.15; margin-bottom:10px; letter-spacing:-.3px; }}
  h3 {{ font-weight:700; font-size:12.5px; margin-bottom:4px; }}
  p {{ margin-bottom:9px; color:#d8d3e0; }}
  strong {{ color:#fff; font-weight:700; }}
  .gold {{ color:#d4af37; }}

  .divider {{ height:1px; background:rgba(255,255,255,.08); margin:16px 0; }}

  /* cabeçalho capa */
  .cover-head {{ display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:48px; }}
  .cover-head img {{ width:150px; }}
  .cover-meta {{ text-align:right; font-family:'JetBrains Mono',monospace; font-size:9px; color:#9a93a8; letter-spacing:1.5px; line-height:1.9; }}

  .cover-title {{ margin-top:60px; }}
  .cover-title .label {{ display:block; margin-bottom:18px; }}
  .cover-sub {{ font-size:14px; color:#9a93a8; margin-top:18px; max-width:440px; line-height:1.6; }}

  .cover-foot {{ position:relative; z-index:1; margin-top:auto; padding-top:18px;
    display:flex; justify-content:space-between; align-items:flex-end;
    font-family:'JetBrains Mono',monospace; font-size:9px; letter-spacing:1.5px; color:#9a93a8; }}

  /* cards / boxes */
  .card {{
    background:#181423; border:1px solid rgba(255,255,255,.07);
    border-radius:14px; padding:16px 18px; margin-bottom:12px;
  }}
  .card.tight {{ padding:13px 16px; }}

  .row {{ display:flex; gap:12px; }}
  .row > * {{ flex:1; }}

  /* contraste problema vs solução */
  .vs {{ display:flex; gap:12px; margin:14px 0; }}
  .vs .box {{ flex:1; border-radius:14px; padding:15px 16px; }}
  .vs .bad {{ background:rgba(229,72,77,.06); border:1px solid rgba(229,72,77,.28); }}
  .vs .good {{ background:rgba(212,175,55,.07); border:1px solid rgba(212,175,55,.35); }}
  .vs .tag {{ font-family:'JetBrains Mono',monospace; font-size:8.5px; letter-spacing:1.5px; text-transform:uppercase; margin-bottom:8px; display:block; }}
  .vs .bad .tag {{ color:#e5484d; }}
  .vs .good .tag {{ color:#d4af37; }}

  /* KPI strip */
  .kpis {{ display:flex; gap:9px; margin:14px 0; }}
  .kpi {{ flex:1; background:#181423; border:1px solid rgba(255,255,255,.07); border-radius:12px; padding:12px 10px; }}
  .kpi .k-label {{ font-family:'JetBrains Mono',monospace; font-size:7.5px; letter-spacing:1px; color:#9a93a8; text-transform:uppercase; }}
  .kpi .k-num {{ font-size:20px; font-weight:900; color:#d4af37; line-height:1.1; margin:5px 0 2px; }}
  .kpi .k-sub {{ font-size:8px; color:#9a93a8; }}

  /* feature list */
  .feat {{ display:flex; gap:11px; margin-bottom:11px; align-items:flex-start; }}
  .feat .n {{ font-family:'JetBrains Mono',monospace; font-size:10px; color:#d4af37; font-weight:700; min-width:26px; padding-top:1px; }}
  .feat .body p {{ margin-bottom:0; font-size:10.5px; }}

  /* fluxo */
  .flow {{ display:flex; align-items:stretch; gap:0; margin:14px 0; }}
  .flow .step {{ flex:1; background:#181423; border:1px solid rgba(255,255,255,.07); border-radius:12px; padding:12px 11px; text-align:center; }}
  .flow .arrow {{ display:flex; align-items:center; color:#d4af37; font-size:16px; padding:0 7px; }}
  .flow .step .s-label {{ font-family:'JetBrains Mono',monospace; font-size:7.5px; letter-spacing:1px; color:#9a93a8; text-transform:uppercase; margin-bottom:5px; }}
  .flow .step .s-title {{ font-size:10.5px; font-weight:700; }}

  ul.clean {{ list-style:none; }}
  ul.clean li {{ position:relative; padding-left:16px; margin-bottom:6px; font-size:10.5px; color:#d8d3e0; }}
  ul.clean li::before {{ content:"→"; position:absolute; left:0; color:#d4af37; font-weight:700; }}

  /* investimento */
  .price-box {{ background:linear-gradient(135deg, rgba(212,175,55,.10), rgba(212,175,55,.03));
    border:1px solid rgba(212,175,55,.35); border-radius:14px; padding:20px 22px; }}
  .price-num {{ font-size:26px; font-weight:900; color:#d4af37; }}

  .footer-cta {{ background:#14111d; border:1px solid rgba(255,255,255,.07); border-radius:14px; padding:18px 20px; margin-top:14px; }}
  .footer-cta .label {{ display:block; margin-bottom:8px; }}
  .contact {{ font-family:'JetBrains Mono',monospace; font-size:10px; color:#d8d3e0; letter-spacing:.5px; line-height:2; }}
  .contact .gold {{ color:#d4af37; }}
</style>
</head>
<body>

<!-- ============ CAPA ============ -->
<div class="page">
  <div class="grid-bg"></div>
  <div class="glow"></div>
  <div class="content">
    <div class="cover-head">
      <img src="{LOGO}" alt="GA Business Insights">
      <div class="cover-meta">
        PROPOSTA DE SOLUÇÃO<br>
        TREINO · HIPERTROFIA<br>
        JUN / 2026
      </div>
    </div>

    <div class="cover-title">
      <span class="label">BI · DADOS · DECISÃO &nbsp;·&nbsp; APLICADO AO TREINO</span>
      <h1>Não é uma planilha<br>de treino.<br><span class="gold">É um sistema que<br>prova o ganho.</span></h1>
      <p class="cover-sub">Treino personalizado para hipertrofia feminina — com registro de sessão e análise de evolução. A carga subiu? O volume cresceu? O dado responde. Não o achismo.</p>
    </div>
  </div>
  <div class="cover-foot">
    <div>GA BUSINESS INSIGHTS<br><span style="color:#d4af37">@ga.businessinsights</span></div>
    <div style="text-align:right">PARA: ANA S.<br>CONSULTORIA SOLO · PALMAS/TO</div>
  </div>
</div>

<!-- ============ PÁGINA 2 — PROBLEMA + SOLUÇÃO ============ -->
<div class="page">
  <div class="grid-bg"></div>
  <div class="content">
    <span class="label">01 — O PROBLEMA</span>
    <h2 style="margin-top:10px">A planilha de treino que todo mundo entrega morre na segunda semana.</h2>
    <p>Você pediu um guia claro, com plano de progressão. O problema não é montar a lista de exercícios — isso qualquer um faz. O problema é o que acontece <strong>depois</strong>: a planilha estática não sabe se você evoluiu. E hipertrofia é exatamente isso — <strong>sobrecarga progressiva medida no tempo</strong>. Sem medir, não há plano. Há palpite.</p>

    <div class="vs">
      <div class="box bad">
        <span class="tag">▸ PLANILHA COMUM</span>
        <p style="margin-bottom:0; font-size:10px; color:#cbc4d6">Lista de exercícios fixa. Você anota a carga no papel ou esquece. Ninguém sabe se a semana 6 foi mais pesada que a semana 1. A progressão fica no "acho que tô mais forte".</p>
      </div>
      <div class="box good">
        <span class="tag">▸ SISTEMA GA</span>
        <p style="margin-bottom:0; font-size:10px; color:#e8e3ef">Você registra cada série em segundos. O sistema calcula volume, força estimada (1RM) e recorde por exercício. A evolução aparece em gráfico — semana a semana, grupo a grupo.</p>
      </div>
    </div>

    <div class="divider"></div>

    <span class="label">02 — A SOLUÇÃO</span>
    <h2 style="margin-top:10px">Um app de treino + análise. Já construído. <span class="gold">Testado em mim.</span></h2>
    <p>Não vou prototipar uma ideia no seu projeto. Eu já rodo esse sistema — chamo de <strong>Treino Tracker</strong>. Registro meus treinos nele, ele me mostra a evolução. O que eu te entrego é esse motor, <strong>personalizado pro seu treino e pra hipertrofia feminina</strong>: split adaptado, volume maior em membros inferiores, autorregulação por RIR — e a progressão sempre visível no número.</p>

    <div class="kpis">
      <div class="kpi"><div class="k-label">Volume / semana</div><div class="k-num">kg</div><div class="k-sub">carga total movida</div></div>
      <div class="kpi"><div class="k-label">Força (1RM est.)</div><div class="k-num">↑</div><div class="k-sub">por exercício</div></div>
      <div class="kpi"><div class="k-label">Frequência</div><div class="k-num">/sem</div><div class="k-sub">sessões na semana</div></div>
      <div class="kpi"><div class="k-label">Grupo foco</div><div class="k-num">●</div><div class="k-sub">maior volume</div></div>
      <div class="kpi"><div class="k-label">Recordes</div><div class="k-num">PR</div><div class="k-sub">por exercício</div></div>
    </div>
    <p class="muted" style="font-size:9px; font-family:'JetBrains Mono',monospace; letter-spacing:.5px">▸ MÉTRICAS REAIS DO PAINEL DO TREINO TRACKER — O MESMO QUE VOCÊ VAI USAR.</p>
  </div>
  <div class="cover-foot"><div>GA BUSINESS INSIGHTS</div><div>02 / 04</div></div>
</div>

<!-- ============ PÁGINA 3 — O QUE ENTREGA + COMO FUNCIONA ============ -->
<div class="page">
  <div class="grid-bg"></div>
  <div class="content">
    <span class="label">03 — O QUE VOCÊ RECEBE</span>
    <h2 style="margin-top:10px">Dois lados: registrar é simples, ler a evolução é o que importa.</h2>

    <div class="row">
      <div class="card">
        <h3 class="gold">Registro de sessão</h3>
        <p class="muted" style="font-size:9px; margin-bottom:9px">O lado que você usa na academia, no celular.</p>
        <ul class="clean">
          <li>Escolhe o treino (ex: inferiores, superiores, push, pull) e a data</li>
          <li>Busca o exercício e adiciona série: reps, carga (kg ou lb) e RIR</li>
          <li>"Repetir última sessão" — não recomeça do zero toda vez</li>
          <li>Técnicas avançadas (drop-set, myo-reps) marcadas no registro</li>
        </ul>
      </div>
      <div class="card">
        <h3 class="gold">Painel de evolução</h3>
        <p class="muted" style="font-size:9px; margin-bottom:9px">O lado que prova que o treino funciona.</p>
        <ul class="clean">
          <li>Volume por semana — está crescendo? (gráfico de barras)</li>
          <li>Progressão de força por exercício (1RM estimado, linha)</li>
          <li>Distribuição por grupo muscular — equilíbrio do treino</li>
          <li>Tabela de recordes pessoais (PR) por exercício</li>
        </ul>
      </div>
    </div>

    <div class="divider"></div>

    <span class="label">04 — COMO FUNCIONA</span>
    <h2 style="margin-top:10px">Você registra. O sistema calcula. A decisão fica óbvia.</h2>
    <div class="flow">
      <div class="step"><div class="s-label">VOCÊ FAZ</div><div class="s-title">Registra a série<br>(reps · carga · RIR)</div></div>
      <div class="arrow">→</div>
      <div class="step"><div class="s-label">O SISTEMA</div><div class="s-title">Calcula volume<br>e força (1RM)</div></div>
      <div class="arrow">→</div>
      <div class="step"><div class="s-label">O PAINEL</div><div class="s-title">Atualiza gráficos<br>e recordes</div></div>
      <div class="arrow">→</div>
      <div class="step"><div class="s-label">VOCÊ DECIDE</div><div class="s-title">Subir carga<br>ou volume</div></div>
    </div>

    <div class="card tight" style="margin-top:6px">
      <h3>Por que isso gera massa (e a planilha comum não)</h3>
      <p style="margin-bottom:0; font-size:10.5px">Hipertrofia tem dois motores comprovados: <strong>sobrecarga progressiva</strong> e <strong>volume adequado</strong>. Os dois são número — e número precisa ser medido pra ser aumentado de propósito. O sistema autorregula pela RIR (quão perto da falha você foi) e mostra, semana a semana, se a carga ou o volume realmente subiram. <span class="gold">É a diferença entre treinar e progredir.</span></p>
    </div>
  </div>
  <div class="cover-foot"><div>GA BUSINESS INSIGHTS</div><div>03 / 04</div></div>
</div>

<!-- ============ PÁGINA 4 — PERSONALIZAÇÃO + INVESTIMENTO + CTA ============ -->
<div class="page">
  <div class="grid-bg"></div>
  <div class="content">
    <span class="label">05 — PERSONALIZAÇÃO PRA VOCÊ</span>
    <h2 style="margin-top:10px">Hipertrofia feminina não é treino masculino com menos peso.</h2>
    <p>O sistema é meu, mas o treino é seu. A montagem considera o que a fisiologia feminina responde melhor: <strong>maior tolerância a volume e frequência</strong>, ênfase em membros inferiores e glúteos, e recuperação mais rápida — tudo dentro de sobrecarga progressiva. A seleção de exercícios entra de acordo com o que você (ou seu treinador) prefere; eu estruturo o plano de progressão por semanas e ligo tudo ao painel.</p>
    <p class="muted" style="font-size:9.5px"><strong style="color:#9a93a8">Honestidade do escopo:</strong> sou consultor de dados e sistemas, não personal trainer. A força da entrega é o sistema, a estrutura de progressão e a análise. A metodologia segue princípios de hipertrofia consolidados — e fica 100% editável pela sua preferência ou do seu profissional.</p>

    <div class="divider"></div>

    <span class="label">06 — ESCOPO &amp; INVESTIMENTO</span>
    <div class="row" style="margin-top:10px">
      <div class="card" style="flex:1.3">
        <h3>O que está incluído</h3>
        <ul class="clean">
          <li>Sistema de registro de treino (celular + computador)</li>
          <li>Painel de evolução: volume, força, grupos, PRs</li>
          <li>Plano de treino estruturado por semanas (progressão)</li>
          <li>Personalização pro seu split e seus exercícios</li>
          <li>Treino de uso (call rápida) + guia de como atualizar</li>
        </ul>
      </div>
      <div class="price-box" style="flex:1">
        <span class="label">INVESTIMENTO DE REFERÊNCIA</span>
        <div class="price-num" style="margin:8px 0 2px">R$ 150 / hora</div>
        <p style="font-size:9.5px; color:#cbc4d6; margin-bottom:8px">Escopo estimado: <strong>10 a 14 horas</strong>. Fecho o valor exato depois de entender teu treino numa call de 20 min — não cobro no escuro.</p>
        <p style="font-size:8.5px; color:#9a93a8; margin-bottom:0; font-family:'JetBrains Mono',monospace; letter-spacing:.5px">DENTRO DA FAIXA R$ 100–230/H DO PROJETO.</p>
      </div>
    </div>

    <div class="footer-cta">
      <span class="label">PRÓXIMO PASSO</span>
      <h3 style="font-size:14px; margin-bottom:6px">Uma call de 20 minutos. Eu te mostro o Treino Tracker rodando ao vivo.</h3>
      <p style="font-size:10px; margin-bottom:12px">Você vê o sistema funcionando antes de fechar qualquer coisa. Aí decide com dado na mão — não com promessa.</p>
      <div class="contact">
        <span class="gold">▸</span> Instagram &nbsp; <span class="gold">@ga.businessinsights</span><br>
        <span class="gold">▸</span> Cases reais &nbsp; <span class="gold">ga-business.pages.dev/cases</span>
      </div>
    </div>
  </div>
  <div class="cover-foot">
    <div>GA BUSINESS INSIGHTS &nbsp;·&nbsp; BI · IA · SISTEMAS</div><div>04 / 04</div>
  </div>
</div>

</body>
</html>
"""

HTML(string=HTML_DOC).write_pdf(OUT)
print("PDF gerado:", OUT)
