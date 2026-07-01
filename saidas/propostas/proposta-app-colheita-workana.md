# Proposta — App Mobile + Web para Digitalização de Colheita

**Origem:** Workana (Mayra S.) · Faixa do anúncio: R$ 5.000–16.000 · 10 propostas até o momento
**Data:** 01/07/2026
**Stack decidida:** Stack 2 — Supabase (PostgreSQL) + front web/PWA

---

## Texto pra colar na plataforma

Olá, Mayra!

Colheita tem um problema que quase todo app ignora: **no campo, o sinal falha**. Se o app depende de internet pra registrar o romaneio, o dado se perde exatamente na hora que mais importa. Minha proposta resolve isso de saída.

**O que eu entrego:**

**1. App de campo (Android e iOS)** — login por usuário, registro detalhado do romaneio (talhão, produto, quantidade, veículo, responsável — os campos a gente ajusta ao seu processo real). Funciona **offline** e sincroniza sozinho quando o sinal volta. Nenhum registro se perde.

**2. Painel web** — tudo que o campo registra, centralizado em tempo real. Filtros por período, usuário, talhão e o que mais o fechamento exigir. **Exportação em CSV** pronta pro Excel e pro fechamento externo. E um extra incluso: sou analista de BI — o painel já vem com os números da colheita visíveis (volume por dia, por frente de trabalho, por área), não só uma lista de registros.

**Tecnologia:** banco PostgreSQL gerenciado (Supabase), com autenticação real e permissão por usuário aplicada no nível do banco — quem colhe vê o que registrou, quem gerencia vê tudo. App e painel em tecnologia web moderna: instala no celular como aplicativo, roda em Android e iOS com um código só. Resultado prático pra você: entrega mais rápida, manutenção mais barata e **custo de infraestrutura próximo de zero** no volume inicial.

**Como eu conduzo:**
1. Call de 30 min pra mapear o romaneio de vocês (campos, fluxo, quem usa)
2. Modelo de dados + telas pra sua aprovação
3. App de campo funcionando pra teste real
4. Painel web com filtros e exportação
5. Ajustes com os usuários e entrega com treinamento

Entrego por etapas — você vê funcionando antes de cada avanço, sem caixa-preta.

**Investimento: R$ 5.900** (escopo fechado acima) · **Prazo: 6 semanas**, com entregas parciais desde a semana 2. Funcionalidades além desse escopo são orçadas à parte, sem surpresa no valor.

Fico à disposição pra uma conversa rápida sobre o processo de colheita de vocês.

Gabriel — GA Business Insights
Portfólio: ga-business.pages.dev

---

## Notas internas (não enviar)

### Por que Stack 2

Tabela de decisão da /fluxo-cliente — bateu 4 sinais da coluna Stack 2:
- **Usuários:** vários usuários de campo + gestão → mais de 5, tende a crescer
- **Login:** o anúncio exige login por usuário → Auth real + RLS
- **Volume/concorrência:** escrita simultânea de vários apps no campo → Sheets não segura
- **API:** app mobile + web consumindo o mesmo dado → precisa de API (PostgREST nativo)

### Arquitetura

- **Banco:** Supabase (Postgres + Auth + RLS + PostgREST) → /esp-supabase
- **App de campo:** PWA offline-first (IndexedDB local + fila de sync) → /esp-webapp. Um código pra Android e iOS. Se o cliente exigir loja (Play/App Store), empacotar com Capacitor — decidir na call, não prometer antes.
- **Painel web:** front consumindo Supabase, filtros + export CSV + camada de BI → /esp-webapp + /esp-bi
- **Tags do anúncio (PHP/MySQL):** genéricas da plataforma — regra zero só vale se o cliente exigir explicitamente. Confirmar na call.

### Precificação (decidida: R$ 5.900 — MVP pra ganhar a disputa)

- Faixa do anúncio: R$ 5.000–16.000, com 10 concorrentes → entrada agressiva perto do piso, sem ser o piso.
- Escopo MVP **fechado por escrito** (lição Studio Donnamar): tela nova, integração ou relatório extra = orçamento novo.
- Margem real vem do pós: manutenção mensal separada (modelo Uno Prints: implantação + mensalidade).

### Prazo (decidido: 6 semanas)

Solo, 6h/dia de trabalho formal. MVP (banco + PWA offline + painel) cabe em 6 semanas com entregas parciais desde a semana 2. Não prometer menos.

### IA (opcional, avaliar na call)

Possível camada: leitura de romaneio por foto (Claude Vision) ou resumo diário automático da colheita pro gestor. Marcar como item opcional na proposta fechada, não no bid.
