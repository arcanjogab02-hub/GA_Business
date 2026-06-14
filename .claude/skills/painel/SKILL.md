---
name: painel
description: >
  Mantém o pipeline de prospecções em `dados/prospeccoes.json` e prepara o arquivo pra importar no
  painel.html (CRM operacional da GA). Adiciona/atualiza clientes e tarefas conforme as prospecções,
  no formato e nas etapas do funil. Use com "/painel", "adiciona no painel", "novo prospect",
  "joga esse lead no painel", "atualiza o pipeline", ou quando um lead/cliente mudar de etapa.
---

# /painel — Alimentar o painel.html com as prospecções

O `painel.html` guarda os dados no **localStorage do navegador** — não dá pra escrever direto nele
daqui. A ponte é o botão **↑ IMPORTAR**, que faz **merge** (soma aos dados atuais, não apaga).

Fonte de verdade do que eu acompanho: **`dados/prospeccoes.json`** (fica **local** — `dados/` está no `.gitignore`, então o dado pessoal dos prospects **não vai pro GitHub**).
Fluxo: eu atualizo esse arquivo → você abre o painel → **↑ IMPORTAR** → seleciona `dados/prospeccoes.json`.

## Quando usar

- Novo lead/prospect pra registrar.
- Cliente mudou de etapa (avançou no funil) ou fechou.
- Transformar o estado de uma call (/diagnostico) ou do /fluxo-cliente em cartão no painel.
- Tarefa nova ligada a um cliente (ex: "mandar amostra até sexta").

## Etapas (stage) — batem com o kanban e o /fluxo-cliente

```
prospect → diagnostico → amostra → proposta → execucao → entregue
```

## Schema do `dados/prospeccoes.json`

```json
{
  "clients": [
    {
      "id": "c-padaria-bom-pao",
      "name": "Maria",
      "company": "Padaria Bom Pão",
      "contact": "(63) 9 9999-9999",
      "stage": "diagnostico",
      "product": "Dashboard BI + ERP Stack 1",
      "value": 0,
      "notes": "Ponto cego: não sabe quais produtos dão margem. Call em 12/06."
    }
  ],
  "tasks": [
    {
      "id": "t-amostra-padaria",
      "title": "Mandar amostra grátis (1 KPI real)",
      "clientId": "c-padaria-bom-pao",
      "due": "2026-06-20",
      "priority": "alta",
      "notes": ""
    }
  ]
}
```

- **`name`** (cliente) e **`title`** (tarefa) são obrigatórios. O resto é opcional.
- **`id`**: eu gero estável a partir da empresa (`c-<slug>` / `t-<slug>`) pra ligar tarefa↔cliente e pra atualizar sem duplicar. O usuário não precisa mexer nisso.
- **`value`**: número em R$. Só preencher se o usuário passar — nunca inventar.
- **`due`**: formato `AAAA-MM-DD`. **`priority`**: `alta` | `media` | `baixa`.

## Workflow

1. Coletar a info do lead: nome, empresa, contato, etapa, produto/serviço pretendido, valor estimado (se houver), notas (a dor / o ponto cego / próximo passo).
2. Abrir `dados/prospeccoes.json`.
   - Cliente já existe (mesma empresa+nome)? → **atualizar** os campos.
   - É novo? → **adicionar** com `id` estável `c-<slug-da-empresa>`.
3. Tarefas ligadas ao cliente → adicionar em `tasks` com `clientId` = id do cliente.
4. Salvar o arquivo (JSON válido — sem vírgula sobrando).
5. Avisar o usuário:
   > Atualizei `dados/prospeccoes.json`. Pra ver no painel: abre o `painel.html` → **↑ IMPORTAR** → seleciona `dados/prospeccoes.json`. Ele soma, não apaga.
6. Backup é local: o arquivo **não** vai pro GitHub (`dados/` é gitignorado, por privacidade do PII). Pra ter cópia, use o botão **↓ BACKUP** do painel ou copie o `prospeccoes.json` à parte.

## Como o merge funciona (no painel)

- Match de cliente: por `id`, senão por **empresa + nome** (normalizado).
- Achou → atualiza os campos preenchidos. Não achou → adiciona.
- Tarefas religam ao cliente automaticamente, mesmo que o cliente já existisse no painel com outro id.
- **Nada é apagado** no import.

## Integra com

- **/fluxo-cliente** — cada avanço de fase vira mudança de `stage` aqui.
- **/diagnostico** — depois da call, registrar o prospect + a amostra como tarefa.
- **↓ BACKUP** (no painel) — cópia local do pipeline. O `prospeccoes.json` **não** é versionado pelo /salvar (privacidade do PII).
- **painel.html** — onde você visualiza (importa o arquivo).

## Regras

- O import do painel **soma** (merge): nunca apaga. Pra **excluir** um cliente/tarefa, faça direto no painel.
- Moveu um card **na mão** no painel? Me avisa pra eu refletir no arquivo — senão o próximo import reaplica o `stage` do arquivo.
- Manter o nome da empresa **consistente** entre importações evita cliente duplicado.
- Não inventar `value` nem `due` — só o que o usuário informar.
- JSON sempre válido: sem comentário, sem vírgula sobrando, datas em `AAAA-MM-DD`.
