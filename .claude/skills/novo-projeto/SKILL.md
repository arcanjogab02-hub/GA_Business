---
name: novo-projeto
description: >
  Estrutura um trabalho novo na hierarquia cliente > projetos. Identifica o cliente (novo ou
  existente), cria a pasta dele quando necessário e abre um projeto em
  `clientes/<Cliente>/projetos/<Projeto>/` com CLAUDE.md, briefing e subpastas das entregas.
  Use quando o usuário disser "novo projeto", "novo cliente", "/novo-projeto", "começar projeto pra X"
  ou pedir pra estruturar um trabalho novo. Chamada pela /fluxo-cliente na fase de fechamento.
---

# /novo-projeto — Cliente > projeto novo com contexto dedicado

Estrutura: `clientes/<Cliente>/projetos/<Projeto>/`. Um cliente pode ter vários projetos.
A pasta `clientes/` é **local** (gitignorada — contém dado de cliente).

## Passo 1 — Identificar o cliente

Perguntar (ou usar o que a /fluxo-cliente já trouxe):

1. "Qual o cliente?"

Verificar se `clientes/<Cliente>/` já existe.

- **Cliente já existe** → pular pro Passo 3 (novo projeto dentro dele).
- **Cliente novo** → seguir o Passo 2.

## Passo 2 — Criar o cliente (só se for novo)

Coletar o básico:

- Contato (WhatsApp / e-mail)
- Segmento / o que a empresa faz
- Stack obrigatória, se houver

Criar `clientes/<Cliente>/` com:

- `CLAUDE.md` do cliente (template abaixo)
- `diagnostico.md` — colar o diagnóstico da /diagnostico se existir; senão, esqueleto

## Passo 3 — Entrevista do projeto

1. "Qual o nome do projeto?" (ex: "Dashboard de vendas", "ERP estoque")
2. "Objetivo principal? (uma frase)"
3. "Que entregas vai ter? (ex: dashboard BI, sistema, site, automação — pode ser mais de uma)"
4. "Qual stack?" — se a /fluxo-cliente já decidiu, usar; senão, aplicar a tabela de decisão (regra zero: stack obrigatória do cliente manda)

## Passo 4 — Criar o projeto

Criar `clientes/<Cliente>/projetos/<Projeto>/` com:

- `CLAUDE.md` do projeto (template abaixo)
- `briefing.md` — objetivo + escopo + proposta fechada (se houver)
- `caso.md` — esqueleto, preenche após a entrega
- `entregas/` com subpastas conforme as entregas pedidas (ex: `entregas/bi/`, `entregas/sistema/`, `entregas/site/`)

Não criar subpasta que não foi pedida.

## Templates

### CLAUDE.md do cliente

```markdown
# Cliente: [Nome]

> Pasta do cliente. Herda o contexto da raiz (_memoria/, identidade/). Aqui, só o específico do cliente.

## Sobre
- Segmento: [o que a empresa faz]
- Contato: [WhatsApp / e-mail]
- Stack padrão: [Stack 1 / Stack 2 / obrigatória do cliente, se houver]

## Projetos
- [lista os projetos em projetos/ conforme forem criados]

## Específico desse cliente
[regras, preferências, particularidades — preencher conforme descobrir]
```

### CLAUDE.md do projeto

```markdown
# Projeto: [Nome] — Cliente: [Cliente]

> Projeto criado em [data]. Herda o contexto do cliente e da raiz.

## Objetivo
[a frase da entrevista]

## Stack
[Stack 1 / Stack 2 — e o porquê. Regra zero: stack obrigatória do cliente manda.]

## Entregas previstas
- [entrega 1]
- [entrega 2]

## Onde salvar
- Briefing e contexto: nessa pasta
- Entregas: cada subpasta em entregas/

## Específico desse projeto
[vazio — preencher conforme for descobrindo]
```

## Passo 5 — Resumo

```
Cliente: [Cliente]  (novo / existente)
Projeto: clientes/<Cliente>/projetos/<Projeto>/
✓ CLAUDE.md do cliente (se novo) e do projeto
✓ briefing.md · caso.md
✓ entregas/: [subpastas]

Pra trabalhar nesse projeto, abre o terminal dentro da pasta dele —
carrego o CLAUDE.md do projeto + do cliente + da raiz juntos.
```

## Regras

- Nome de pasta: como o usuário falou; manter acentos, espaços viram hífen, nome reconhecível.
- Cliente existente? Não recriar — só adicionar projeto em `projetos/`.
- Projeto com nome já existente no cliente? Avisar e perguntar (adiciona dentro ou cria com sufixo).
- Não criar subpasta "pra organizar melhor" — só as entregas pedidas.
- `clientes/` é local (gitignorado). Não tentar versionar dado de cliente sem o usuário pedir.
