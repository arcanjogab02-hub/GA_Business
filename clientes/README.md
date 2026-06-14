# clientes/

Tudo de cliente mora aqui, na hierarquia **cliente > projetos**.

> Esta pasta é **local** — está no `.gitignore` (só este README vai pro GitHub). Briefings, diagnósticos e entregas têm dado de cliente; ficam fora do repositório por privacidade. Backup você faz à parte.

## Estrutura

```
clientes/
└─ <Cliente>/
   ├─ CLAUDE.md         quem é o cliente, contato, stack padrão
   ├─ diagnostico.md    resultado da call (SPIN, dores, ponto cego)
   └─ projetos/
      └─ <Projeto>/
         ├─ CLAUDE.md   objetivo, stack, entregas
         ├─ briefing.md escopo + proposta fechada
         ├─ caso.md     caso de sucesso (após entrega)
         └─ entregas/   bi/ · sistema/ · site/ ...
```

## Como criar

Rode **/novo-projeto**. Ele identifica se o cliente é novo ou existente, cria a pasta do cliente quando preciso e abre o projeto em `projetos/`.

Um cliente pode ter vários projetos — cada novo trabalho é uma subpasta nova em `projetos/`.
