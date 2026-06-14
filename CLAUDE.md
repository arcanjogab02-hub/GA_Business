# GA Business Insights — MazyOS

Operação da consultoria. Aqui ficam todos os clientes, conteúdos, entregas e sistemas.

**Estrutura de pastas:**
- `_memoria/` — quem é a empresa, como falamos, foco atual
- `identidade/` — marca da GA (logo, cores, fontes — aplicada em tudo que o sistema gera)
- `clientes/` — uma pasta por cliente; dentro, `projetos/` com um projeto por subpasta (cliente > projetos). Local (gitignorado — contém dado de cliente)
- `marketing/` — conteúdo institucional (posts, carrosséis, artigos)
- `saidas/` — documentos pontuais, análises, relatórios entregues
- `dados/` — arquivos a analisar (exports, CSVs de cliente)
- `scripts/` — automações e utilitários

---

## Contexto do negócio

No início de toda conversa, ler os seguintes arquivos (quando existirem e estiverem preenchidos):

1. `_memoria/empresa.md` — quem é a GA, o que faz, como funciona
2. `_memoria/preferencias.md` — tom de voz, estilo de escrita, o que evitar
3. `_memoria/estrategia.md` — foco atual, prioridades, gargalos

Usar essas informações como base pra qualquer resposta ou decisão. Ao sugerir prioridades, formatos ou abordagens, considerar o foco atual descrito em `estrategia.md`.

Pra qualquer tarefa visual (carrossel, post, landing page), consultar `identidade/design-guide.md` como referência de estilo.

Não é necessário listar o que foi lido nem confirmar a leitura. Apenas usar o contexto naturalmente.

---

## Sobre a consultoria

GA Business Insights é uma consultoria solo de BI, IA, Marketing e Sistemas Operacionais (ERP Low Cost) baseada em Palmas/TO. Atende pequenas e médias empresas que precisam de gestão por dados sem custo de ERP corporativo.

**Produtos principais:**
- ERP Low Cost Stack 1 — Google Sheets como BD + Google Apps Script (Web App front)
- ERP Low Cost Stack 2 — Supabase como BD + front customizado
- Dashboards de BI e análise de dados
- Consultoria de IA aplicada ao processo do cliente
- Estratégia e produção de conteúdo

**Canal de aquisição principal:** Instagram @ga.businessinsights

**Operação:** solo — o fundador acumula trabalho formal (servidor público TJTO, 6h/dia). Tempo é o recurso mais escasso. Tudo que puder ser automatizado, deve ser.

---

## Fluxo de trabalho

Antes de executar qualquer tarefa, verificar se existe skill relevante em `.claude/skills/`. Se encontrar, seguir as instruções da skill. Se não encontrar, executar a tarefa normalmente.

Ao concluir uma tarefa que não tinha skill mas parece repetível, perguntar:

> "Isso pode virar uma skill pra próxima vez. Quer que eu crie?"

Só perguntar quando o padrão de repetição for claro — não pra tarefas pontuais.

---

## Regras do sistema

- **Cliente novo** → rodar `/novo-projeto`: cria `clientes/<Cliente>/` (identidade + diagnóstico) e o primeiro projeto em `clientes/<Cliente>/projetos/<Projeto>/`
- **Projeto novo de cliente existente** → `/novo-projeto` adiciona outra subpasta em `clientes/<Cliente>/projetos/`
- **Case de sucesso** → documentar em `clientes/<Cliente>/projetos/<Projeto>/caso.md` (reutilizar em conteúdo e pitches)
- **Post novo** → produzir via `/publicar-tema` ou `/carrossel`, salvar em `marketing/`
- **Relatório de ads** → rodar `/relatorio-ads` com os exports em `dados/`
- **Mudança de foco ou prioridade** → atualizar `_memoria/estrategia.md`

---

## Aprender com correções

Quando o usuário corrigir algo ou dar instrução permanente ("prefiro assim", "sempre que...", "evita..."), perguntar:

> "Quer que eu salve isso pra não precisar repetir?"

Se sim, identificar onde salvar:
- Sobre o negócio → `_memoria/empresa.md`
- Sobre preferências e estilo → `_memoria/preferencias.md`
- Sobre prioridades e foco → `_memoria/estrategia.md`
- Regra de comportamento nessa pasta → `CLAUDE.md`

---

## Manter contexto atualizado

Ao terminar uma tarefa que mudou algo relevante (cliente novo, skill nova, mudança de foco), perguntar:

> "Isso mudou algo no teu contexto. Quer que eu atualize a memória?"

Mostrar o que vai mudar antes de salvar. Não reformatar o arquivo inteiro.

**Quando NÃO perguntar:**
- Tarefas pontuais sem impacto no contexto
- Perguntas simples ou conversas sem ação

---

## Criação de skills

Quando o usuário pedir skill nova:

1. Verificar se existe template relevante em `templates/skills/`
2. Perguntar se é específica desse projeto ou útil em qualquer:
   - Específica → `.claude/skills/nome-da-skill/SKILL.md`
   - Universal → `~/.claude/skills/nome-da-skill/SKILL.md`
3. Ler `_memoria/empresa.md` e `_memoria/preferencias.md` pra calibrar o conteúdo da skill
4. Seguir o fluxo da skill-creator nativa do Claude Code

---

## Ferramentas conectadas

- [ ] Gmail
- [ ] Google Calendar
- [ ] Google Drive
- [ ] Canva
- [ ] Meta Ads
- [ ] Google Ads
- [ ] Notion
