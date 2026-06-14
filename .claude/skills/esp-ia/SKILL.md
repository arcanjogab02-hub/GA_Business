---
name: esp-ia
description: >
  Avalia onde a IA encaixa no processo do cliente e desenha a integração (API Claude/LLM rodando em
  Apps Script, Edge Function do Supabase ou no front). IA aqui é camada operacional e diferencial, nunca
  a venda. Invocar com "/esp-ia", "ia aplicada", "automação", "onde a ia encaixa", "integrar llm",
  "chatbot". Chamada pela /fluxo-cliente na execução como camada OPCIONAL que o fundador decide caso a caso.
---

# /esp-ia — Especialista IA Aplicada

A IA é camada operacional e diferencial — não a venda. A venda lidera com dado e decisão. Esta skill
avalia se a IA cabe num projeto, e quando cabe, desenha como entra. Sempre propõe; nunca impõe.

## Quando usar

- Na execução de um projeto, pra checar se alguma parte do processo do cliente ganha com IA.
- Quando o pedido fala em "automação", "integrar LLM", "chatbot", "classificar", "gerar conteúdo".
- Chamada pela /fluxo-cliente como item opcional da proposta — o fundador decide se entra.
- Não usar pra justificar IA onde uma fórmula ou um `if` resolve.

## Workflow

1. **Mapear onde dói/repete.** No processo do cliente, achar: tarefa manual demorada, classificação
   repetitiva, geração de conteúdo, análise/insight, atendimento/triagem. Sem dor clara, não há projeto.
2. **Avaliar fit antes de propor.** Três perguntas:
   - A IA resolve melhor que uma regra simples? (Se um if/fórmula resolve, não usar IA.)
   - Tem dado suficiente e na qualidade certa?
   - Vale o custo por uso e o risco do erro?
   Se qualquer resposta for não, parar aqui e registrar o motivo.
3. **Escolher o tipo.** automação de tarefa | extração/classificação | geração de conteúdo |
   análise/insight | chatbot/atendimento. Um tipo por problema.
4. **Desenhar a integração.** Definir: API do Claude/LLM (modelo Claude mais capaz e atual pro caso),
   onde roda (Apps Script na Stack 1, Edge Function do Supabase na Stack 2, ou no front), o prompt,
   e o custo estimado por uso (tokens x volume mensal).
5. **Go/no-go.** Apresentar como item OPCIONAL na proposta. O fundador decide se entra. Marcar claro
   o que é base do projeto e o que é a camada de IA sugerida.
6. **Guardrails.** Definir antes de codar: validação do output, humano no loop, proteção do dado,
   teto de custo. (Detalhe na seção Regras.)

## Padrões GA

- Comparar sempre com a alternativa sem IA. Se a regra simples entrega, ela ganha.
- Custo explícito: estimar reais por mês, não só "barato". Volume vezes preço por chamada.
- Prompt versionado junto do código, não solto. Output esperado documentado.
- Onde roda segue a stack do projeto — não introduzir infra nova só pra IA.
- Modelo Claude mais capaz e atual quando precisar de qualidade; ver /claude-api pra ids e preços.
- Entregar a camada de IA isolada: o sistema funciona sem ela, ela é plugada por cima.

## Checklist de entrega

- [ ] Dor mapeada e descrita em uma frase
- [ ] Fit avaliado (melhor que regra simples? dado suficiente? vale custo/risco?)
- [ ] Tipo de uso definido
- [ ] Integração desenhada: API, onde roda, prompt, custo/uso estimado
- [ ] Custo mensal estimado (volume x preço)
- [ ] Guardrails definidos (validação, humano no loop, dado, teto de custo)
- [ ] Marcado como OPCIONAL na proposta, com a decisão do fundador registrada

## Integra com

- **/fluxo-cliente** — camada opcional da execução; o fundador decide se entra.
- **/esp-supabase** e **/esp-sheets** — onde a automação roda (Edge Function ou Apps Script).
- **/esp-bi** — análise e insight automatizados sobre os dados.
- **/esp-seguranca** — dado do cliente e secrets das chaves de API.
- **/claude-api** — referência técnica de modelos, ids, preços e API.

## Regras

**Sempre**
- Avaliar fit antes de propor; comparar com a solução sem IA.
- Apresentar IA como sugestão e item opcional. O fundador decide caso a caso.
- Validar o output — não confiar cego no que o modelo devolve.
- Humano no loop em qualquer decisão crítica.
- Estimar custo por uso e definir teto antes de subir.
- Guardar a chave de API como secret (ver /esp-seguranca).

**Nunca**
- Vender "IA" como produto principal — a venda é dado e decisão.
- Usar IA onde uma fórmula ou um `if` resolve.
- Mandar dado pessoal do cliente pra serviço externo sem consentimento.
- Impor a camada de IA num projeto. Propor, sim; decidir pelo fundador, não.
- Subir integração sem validação de output e sem teto de custo.
