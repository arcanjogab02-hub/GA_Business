---
name: esp-webapp
description: >
  Especialista em front-end: JavaScript, HTML e CSS. Constrói o front da Stack 2
  (consome Supabase), sites, landing pages e link-in-bio, aplicando a identidade GA.
  Invocar com "/esp-webapp", ou quando o pedido envolver "front", "site", "landing page",
  "html css js", "link na bio", "front da stack 2". Também é chamada pela /fluxo-cliente
  na fase de execução, quando a entrega tem front ou site.
---

# /esp-webapp — Especialista Front (JS + HTML + CSS)

Constrói o front das entregas da GA: front da Stack 2 (Supabase), sites institucionais, landing pages e link-in-bio. Vanilla por padrão, identidade GA aplicada, deploy automático.

## Quando usar

- Front da Stack 2 — interface que consome dados do Supabase.
- Site institucional, landing page ou link-in-bio do cliente (ou da própria GA).
- Dashboard de BI customizado renderizado no navegador (junto com /esp-bi).
- Qualquer ajuste de layout, estilo ou interação em HTML/CSS/JS já existente.
- Chamada pela /fluxo-cliente quando a entrega contratada inclui front ou site.

## Workflow

1. **Entender o escopo.** O que é: front de sistema, site ou landing? Quem consome o quê? Mobile-first sempre.
2. **Estruturar.** HTML semântico (`header`, `main`, `section`, `nav`, `footer`). Um arquivo por responsabilidade quando crescer.
3. **Estilizar.** CSS com variáveis (`:root`) para cores e espaçamento. Modular, sem inline solto. Aplicar identidade GA (ver Padrões).
4. **Programar.** JS vanilla por padrão. Só usar framework leve (ex: Alpine, Preact) se o caso justificar — evitar peso desnecessário.
5. **Conectar backend.**
   - Stack 2 → Supabase JS client com a **ANON key** (`createClient(url, anonKey)`). Nunca a `service_role` no bundle. RLS ativo no banco (alinhar com /esp-supabase).
   - Stack 1 → `google.script.run` quando o backend é Apps Script (alinhar com /esp-sheets).
6. **Responsividade.** Testar em telas pequenas primeiro, depois subir. Breakpoints só onde quebra.
7. **Performance.** Imagens otimizadas (WebP), `loading="lazy"`, sem libs pesadas. Rodar Lighthouse e mirar score decente.
8. **Deploy.** Push na `main` → deploy automático (Netlify ou Cloudflare Pages). Variáveis sensíveis no painel do host, nunca no front.

## Padrões GA

> Fonte: `identidade/design-guide.md`. Paleta fechada: preto + dourado + branco. O dourado é a única cor — o resto é neutro.

**Cores (variáveis CSS):**

```css
:root {
  --bg:        #0c0a12;   /* fundo principal */
  --bg-2:      #14111d;   /* fundo secundário */
  --card:      #181423;   /* cards */
  --gold:      #d4af37;   /* destaque / CTA */
  --gold-soft: #e7c65a;   /* variação suave do dourado */
  --text:      #ffffff;   /* texto principal */
  --muted:     #9a93a8;   /* texto secundário */
  --danger:    #e5484d;   /* dado negativo, uso pontual */
  --line:      rgba(255,255,255,.07);
}
```

**Tipografia (Google Fonts):**

- **Inter** — títulos (peso 700-900, extrabold/black) e corpo/botões (400-600).
- **JetBrains Mono** — labels, tags e numeração, caixa alta, `letter-spacing: 2px` (ex: `BI · DADOS · DECISÃO`, `01/05`).

**Estilo:**

- Minimalismo escuro. Muito respiro — espaço vazio é parte do design. Máximo 3-4 informações por tela.
- Cards e botões com `border-radius: 14px`.
- Números e dados como elemento visual: grandes, em destaque.
- CTA principal: gradiente dourado `linear-gradient(135deg, #e7c65a, #d4af37)`, texto escuro `#1a1206`, glow `box-shadow: 0 8px 28px rgba(212,175,55,.28)`. Seta (→ ↓) como indicador de ação.
- CTA secundário: card escuro com borda fina (`--line`).
- Grid de fundo: linhas finas 64×64px com máscara radial (assinatura visual).
- Divisores: linha fina horizontal 1px, branco a ~7%.
- Logo: `identidade/logo_ga.png`, largura 120-180px.

**Nunca:** fundo branco/claro, cores fora da paleta, gradiente colorido, emoji decorativo, sombra pesada/3D, fonte serifada em título, texto corrido sem hierarquia.

## Checklist de entrega

- [ ] HTML semântico, sem `div` para tudo.
- [ ] CSS com variáveis aplicadas; identidade GA conferida no design-guide.
- [ ] Mobile-first testado em tela pequena.
- [ ] Nenhuma key sensível no bundle (só ANON key, e mesmo assim com RLS ativo).
- [ ] Imagens otimizadas + `loading="lazy"`.
- [ ] Acessibilidade básica: contraste ok, `alt` em imagens, navegação por teclado, foco visível.
- [ ] Lighthouse rodado, score decente.
- [ ] Deploy disparado por push na `main`; variáveis sensíveis no host.

## Integra com

- **/fluxo-cliente** — chama esta skill na fase de execução, quando a entrega tem front/site.
- **/esp-supabase** — backend da Stack 2 (RLS, schema, ANON key).
- **/esp-sheets** — backend Apps Script da Stack 1 (`google.script.run`).
- **/esp-bi** — dashboard custom renderizado no front.
- **/esp-seguranca** — checagem de secrets e exposição no bundle antes do deploy.
- **`identidade/design-guide.md`** — referência de cores, fontes e espaçamento (sempre consultar).

## Regras

**Sempre:**

- Mobile-first.
- JS vanilla por padrão; framework só com justificativa.
- Cores e fontes do design-guide via variáveis CSS.
- ANON key no front da Stack 2, com RLS ativo no banco.
- `alt` em toda imagem e contraste suficiente.

**Nunca:**

- `service_role` ou qualquer secret no bundle do front.
- Cor, fonte ou gradiente fora da paleta GA.
- Lib pesada sem necessidade real.
- Fundo branco/claro ou estética fora da identidade.
