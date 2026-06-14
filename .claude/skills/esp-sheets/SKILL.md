---
name: esp-sheets
description: >
  Especialista em montar sistemas na Stack 1: Google Sheets como banco + Apps Script
  (Web App front). Modela planilha-banco, escreve fórmulas/validação, monta o Web App
  e aplica a identidade GA. Invocar com "/esp-sheets", ou quando o pedido for "modelar
  planilha", "apps script", "web app no sheets", "stack 1". Chamada pela /fluxo-cliente
  na fase de execução quando a stack escolhida é a 1.
---

# /esp-sheets — Especialista Google Sheets + Apps Script (Stack 1)

Monta o sistema operacional de baixo custo do cliente: planilha como banco, Apps Script como backend e Web App como front. Stack 1 = até ~5 usuários, dado já em planilha, orçamento baixo, sem login robusto, baixa criticidade.

## Quando usar

- Cliente fechou na Stack 1 (a /fluxo-cliente chama aqui na execução).
- Modelar uma planilha pra virar banco de dados.
- Construir ou ajustar um Web App em Apps Script sobre Sheets.
- Dúvida de fórmula, validação ou performance em planilha de produção.

Não usar quando o projeto já passou dos limites da Stack 1 (ver Regras) — aí é /esp-supabase.

## Workflow

**1. Backup antes de tudo.** Se a planilha já está em produção, fazer cópia/versão datada antes de mexer. Nunca editar a única cópia viva.

**2. Modelar a planilha-banco.**
- 1 aba = 1 tabela. 1 linha = 1 registro. Linha 1 = cabeçalho.
- Coluna de ID único por registro (ex: `id_pedido`), nunca reutilizar ID.
- Zero células mescladas. Zero cabeçalho duplo.
- Separar camadas: aba(s) de **dados brutos** (só registros), aba(s) de **visão/relatório** (fórmulas, nunca digitar em cima), aba **config** (listas, parâmetros, constantes).

**3. Fórmulas e validação.**
- Dropdowns via data validation, puxando da aba config.
- QUERY pra relatórios, FILTER/ARRAYFORMULA pra cálculos em coluna, XLOOKUP (ou PROCV) pra cruzar tabelas.
- Intervalos nomeados nos ranges reusados — fórmula fica legível.
- Proteger abas/colunas de fórmula contra edição manual.

**4. Apps Script Web App.**
- `doGet` serve o front, `doPost` (ou funções chamadas via `google.script.run`) trata as ações.
- Front em HtmlService; `google.script.run` chama o backend e recebe retorno.
- Deploy como Web App: definir "executar como" e "quem tem acesso" conforme o caso (ver /esp-seguranca).
- Aplicar identidade GA no front: fundo escuro, dourado de destaque, fonte Inter (consultar `identidade/design-guide.md`).

**5. Performance.**
- Ler/escrever em lote: `getValues`/`setValues` numa tacada, nunca célula a célula em loop.
- Cortar funções voláteis em excesso (NOW, TODAY, RAND) — recalculam toda hora.
- Usar CacheService quando o mesmo dado é lido muitas vezes.

**6. Validar e entregar.** Testar com dado real, conferir checklist, entregar com instrução curta de uso.

## Padrões GA

- Nomes em snake_case minúsculo: abas, colunas, intervalos nomeados.
- Aba config sempre existe, mesmo que pequena — toda lista/parâmetro mora lá.
- Dados brutos nunca recebem fórmula; visão nunca recebe digitação.
- Front do Web App segue a identidade GA (escuro + dourado + Inter).
- Cada função do Apps Script faz uma coisa só; código comentado no topo com o que faz.

## Checklist de entrega

- [ ] Backup/cópia da versão anterior guardada
- [ ] 1 aba = 1 tabela, ID único, sem mescladas
- [ ] Camadas separadas: brutos / visão / config
- [ ] Validações e dropdowns funcionando
- [ ] Abas/colunas de fórmula protegidas
- [ ] Leitura/escrita em lote (sem loop célula a célula)
- [ ] Web App deployado com acesso correto definido
- [ ] Front com identidade GA aplicada
- [ ] Testado com dado real

## Integra com

- **/fluxo-cliente** — chama esta skill na fase de execução quando a stack é a 1.
- **/esp-bi** — o BI roda em cima desta planilha; manter dados brutos limpos pro BI consumir.
- **/esp-seguranca** — definir acesso ao Web App ("executar como", "quem acessa") e proteção de abas.
- **/esp-supabase** — destino da migração quando a Stack 1 estoura os limites.

## Regras

**Sempre:**
- Backup antes de mexer em planilha de cliente em produção.
- Separar dados brutos de visão e de config.
- Ler/escrever em lote no Apps Script.
- Aplicar identidade GA no front do Web App.

**Nunca:**
- Mesclar células ou usar a planilha-banco como planilha de "layout".
- Digitar dado em aba de fórmula/visão.
- Deixar coluna de fórmula desprotegida numa planilha multiusuário.
- Insistir na Stack 1 quando o projeto passa de ~5 usuários, ganha alto volume/escrita concorrente, ou vira crítico → recomendar migração pra Stack 2 (/esp-supabase).
