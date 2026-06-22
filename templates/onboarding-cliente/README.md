# Template de onboarding do cliente

Padrão da GA pro primeiro contato depois que o projeto fecha: agradece, explica como vamos trabalhar e coleta o briefing — tudo num documento só, fácil de ler e responder.

## Arquivos
- `_fonte/template.md` — fonte editável (markdown simples)
- `Onboarding_GA_TEMPLATE.docx` — gerado a partir da fonte (é o que se envia ao cliente)

## Como usar num cliente novo
1. Copie `_fonte/template.md` pra pasta do projeto do cliente.
2. Troque `[NOME]` e o **Bloco 2** pelas perguntas específicas daquele projeto (BI, ERP, site, Notion…). Mantenha o resto.
3. Gere o docx:
   ```
   powershell -NoProfile -ExecutionPolicy Bypass -File scripts\md-to-docx.ps1 -In "<caminho>\onboarding.md" -Out "<caminho>\Onboarding_<Cliente>.docx"
   ```
4. Envie o docx ao cliente.

## Marcadores do markdown (ver `scripts/md-to-docx.ps1`)
`#` título · `##` seção · `###` rótulo · `-` bullet · `>` nota · `---` divisória · `[__]` linha de resposta · `**negrito**`.

## Princípios
- Minimalista. Pergunta curta, uma por linha, com espaço pra responder logo abaixo.
- Só o que muda a execução. Se a resposta não altera o que você vai construir, corta a pergunta.
