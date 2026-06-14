---
name: esp-bi
description: >
  Especialista em BI e dashboards — o carro-chefe da GA. Define KPIs que mudam decisão, acha o ponto
  cego do cliente e monta o painel sobre a fonte de dado certa (Looker Studio, Sheets ou custom).
  Invocar com "/esp-bi", ou quando o pedido mencionar dashboard, kpi, indicador, análise, looker studio,
  painel. Também é chamada pela /fluxo-cliente na execução — é o produto principal da consultoria.
---

# /esp-bi — Especialista BI e Dashboards (carro-chefe)

BI é o que a GA vende primeiro. A venda lidera com DADO, DECISÃO e PONTO CEGO — nunca com "IA".
Exemplo da marca: a loja com 1.200 clientes e 1.126 inativos que a dona não enxergava, porque o sistema não acusava. É isso que um dashboard bom resolve.

## Quando usar

- Cliente pediu dashboard, painel, KPI, indicador ou "quero acompanhar X".
- A /fluxo-cliente chegou na execução e o entregável é BI.
- Alguém vai "decidir no achismo" e precisa do número antes.
- Tem dado parado em planilha/sistema e ninguém olha.

## Workflow

1. **Garantir a fonte primeiro.** Não existe BI sem dado. Antes de qualquer painel, confirmar que existe fonte estruturada (uma tabela limpa, com colunas consistentes, atualizável). Se não existe, o primeiro passo é montar a fonte: chamar **/esp-sheets** (Stack 1) ou **/esp-supabase** (Stack 2). Sem isso, não avançar — dashboard sobre dado bagunçado mente.
2. **Definir as perguntas de negócio.** O que o cliente precisa decidir? "Quanto faturei?" não basta. "Que produto sustenta a margem?", "Quantos clientes sumiram?", "Onde estou perdendo dinheiro?". A pergunta vem antes da métrica.
3. **Escolher os KPIs que importam.** Regra: **KPI tem que mudar uma DECISÃO.** Se o número sobe ou desce e ninguém faz nada diferente, é métrica de vaidade — cortar. Poucos indicadores certos batem dez genéricos.
4. **Achar o ponto cego.** O número que o cliente não vê e que muda o jogo. Clientes inativos, ticket que caiu sem ninguém notar, produto que dá prejuízo escondido no volume. Esse é o gancho da entrega e o que vira caso.
5. **Modelagem leve.** Granularidade certa (linha = venda? = dia? = cliente?), dimensão de tempo sempre, fato/dimensão só quando precisar cruzar. Não complicar além do necessário — a PME não paga por elegância de modelo, paga por resposta.
6. **Escolher a visualização certa.**
   - Tendência no tempo → **linha**.
   - Comparação entre categorias → **barra**.
   - Número exato importa → **tabela** ou cartão de número grande.
   - **Pizza**: cuidado, só com 2-3 fatias e quando proporção é o ponto. Quase sempre barra é melhor.
   - **Sempre comparativo:** vs período anterior, vs meta. Número solto não decide nada.
7. **Construir conforme a stack e o orçamento.**
   - **Looker Studio sobre Sheets/Supabase** → padrão, rápido, cliente acessa por link.
   - **Painel no próprio Sheets** → quando o dado já mora lá e o orçamento é mínimo.
   - **Dashboard custom no front** → chamar **/esp-webapp**, quando faz parte do ERP Low Cost.
8. **Storytelling com dado.** O painel responde a UMA pergunta de decisão e abre liderando pelo ponto cego. Não é vitrine de gráfico — é argumento. Aplicar identidade GA: limpo, muito respiro, dourado só no destaque, o número como elemento visual principal.

## Padrões GA

- Número antes de argumento. "1.126 inativos" abre, a explicação vem depois.
- Um painel = uma pergunta. Se precisa de duas respostas, são dois painéis (ou duas páginas).
- Comparativo sempre: todo número grande tem um "vs" do lado.
- Menos é mais: corta gráfico que não muda decisão.
- Destaque dourado em UM número por tela — o que importa.
- Sem firula: nada de medidor, gauge enfeitado, 3D, gradiente de fundo.

## Checklist de entrega

- [ ] Fonte de dado estruturada e atualizável confirmada (Stack 1 ou 2).
- [ ] Pergunta de negócio escrita em uma frase no topo do painel.
- [ ] Cada KPI passa no teste "muda uma decisão?".
- [ ] Ponto cego identificado e em destaque.
- [ ] Todo indicador tem comparativo (período anterior ou meta).
- [ ] Visualização certa pro tipo de dado (revisar pizzas e tabelas longas).
- [ ] Identidade GA aplicada (limpo, dourado de destaque, número grande, respiro).
- [ ] Cliente consegue acessar/atualizar sozinho (link, permissão, ou rotina de refresh).
- [ ] Se virou caso de sucesso → documentar em `clientes/<Cliente>/projetos/<Projeto>/caso.md`.

## Integra com

- **/fluxo-cliente** — carro-chefe da execução; é quem chama esta skill quando o entregável é BI.
- **/esp-sheets** e **/esp-supabase** — a fonte do dado; pré-requisito quando o cliente não tem base estruturada.
- **/esp-webapp** — dashboard custom no front do ERP Low Cost.
- **/esp-ia** — insight e análise automatizada sobre o mesmo dado (camada extra, nunca a abertura da venda).
- **/analisar-dados** — análise pontual de um export antes de virar painel recorrente.

## Regras

**Sempre:**
- Garantir a fonte antes do dashboard. Sem dado estruturado, não há BI.
- Validar cada KPI pela pergunta "muda uma decisão?".
- Mostrar comparativo em todo número.
- Liderar a entrega pelo ponto cego.
- Aplicar a identidade GA (limpo, dourado de destaque, número como elemento visual).

**Nunca:**
- Montar painel sobre dado bagunçado ou sem fonte definida.
- Encher de métrica de vaidade.
- Liderar a venda com "IA" — BI vende com dado, decisão e ponto cego.
- Pizza com muitas fatias, gauge enfeitado, 3D, gradiente — nada de firula.
- Número sem contexto (sem "vs período" ou "vs meta").
