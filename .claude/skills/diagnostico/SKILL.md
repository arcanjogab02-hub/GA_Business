---
name: diagnostico
description: >
  Co-piloto AO VIVO da videochamada de diagnóstico gratuito. Conduz o roteiro SPIN Selling em tempo
  real (Situação → Problema → Implicação → Necessidade), adaptando a próxima pergunta ao que o cliente
  responde, e no fim define o entregável grátis de amostra que valida a oferta. Feito pra ler na
  segunda tela durante a call. Use com "/diagnostico", "call de diagnóstico", "vou fazer a videochamada",
  "diagnóstico gratuito", "spin", ou quando a /fluxo-cliente chegar na fase de diagnóstico.
---

# /diagnostico — Co-piloto da call de diagnóstico (SPIN + entregável grátis)

Roteiro vivo pra conduzir a videochamada de diagnóstico gratuito sem travar. Roda na segunda tela:
eu te dou a próxima pergunta, você cola o que o cliente respondeu, eu adapto. No fim, fechamos o
diagnóstico e definimos o entregável grátis de amostra.

Dois roteiros:
1. **A call** — diagnóstico via SPIN Selling.
2. **O entregável grátis** — a amostra que valida a oferta.

---

## Modo ao vivo (como usar na call)

1. Antes de começar, me dá o setup em uma linha: nome/empresa do cliente, segmento, e o que você já sabe dele.
2. Durante a call, funciona em loop:
   - Eu mostro a **próxima pergunta** + **o que escutar**.
   - Você faz a pergunta e me cola/resume a resposta do cliente.
   - Eu adapto: aprofundo, mudo de fase SPIN, ou sigo.
3. Você dita o ritmo: "próxima", "vai pra implicação", "fecha o diagnóstico".
4. Mantém leve — é conversa, não interrogatório. Deixa o cliente falar.

---

## Roteiro 1 — A call (SPIN Selling)

SPIN é a ordem das perguntas: **S**ituação → **P**roblema → **I**mplicação → **N**ecessidade.
A dor cresce ao longo da conversa. Quem nomeia o problema e o custo é o cliente, não você.

### S — Situação (entender o cenário)
Poucas perguntas, sem cansar. Mapear como opera e onde mora o dado.
- Como funciona a operação de vocês hoje, no dia a dia?
- Onde ficam os dados — planilha, sistema, caderno, na cabeça de alguém?
- Como você acompanha os números hoje? Com que frequência olha?
- Quem decide o quê, e com base em quê?

*Escutar:* dado solto, decisão no achismo, retrabalho manual.

### P — Problema (fazer nomear a dor)
- O que mais te consome tempo nessa rotina?
- Tem algum número que você gostaria de ter e hoje não tem?
- Onde você sente que pode estar perdendo dinheiro sem ver?
- Já tomou uma decisão que, olhando pra trás, com o dado certo teria sido outra?

*Escutar:* o ponto cego começando a aparecer. Anotar a frase do cliente, literal.

### I — Implicação (ampliar o custo da dor) — aqui a venda esquenta
- Esse problema, ao longo de um mês/ano, custa quanto mais ou menos?
- Se continuar do jeito que está, o que acontece?
- Quanto tempo da tua equipe vai embora nisso?
- Esse ponto cego já te custou um cliente, uma compra errada, um prejuízo?

*Escutar:* transformar a dor em número. É o que justifica pagar pra resolver.

### N — Necessidade / Solução (cliente verbaliza o valor)
- Se você enxergasse [o número do ponto cego] em tempo real, o que mudaria?
- Quanto valeria parar de [a dor] de vez?
- Como seria o cenário ideal pra você daqui a 3 meses?

*Escutar:* o cliente descrevendo o estado desejado. Usar as palavras dele na proposta depois.

---

## Fechamento da call

1. **Resumir o diagnóstico em uma frase:** problema real + o número do ponto cego. (Ex: "Você tem 1.200 clientes e não sabe que 1.126 pararam de comprar.")
2. **Apontar o estado desejado** com as palavras do cliente.
3. **Anunciar o entregável grátis:** "Vou te mandar [amostra] em [X dias] pra você ver isso funcionando com o teu próprio dado." (Pedir um dado de exemplo se precisar.)
4. **Combinar o próximo passo** e a data.

---

## Roteiro 2 — O entregável grátis (amostra que valida a oferta)

A amostra grátis tem objetivo triplo:
- **Instigar curiosidade** — mostra que tem mais embaixo.
- **Mostrar o estado desejado** sendo atendido — o cliente vê o "depois" com o dado dele.
- **Validar a oferta** — confirma que ele quer o resultado completo antes de você fazer proposta paga.

### Regras da amostra
- **Pequena e rápida.** Tempo é escasso. Mostra um pedaço do resultado, nunca o todo.
- **Com o dado real do cliente** sempre que possível — o impacto vem de ser ELE no gráfico.
- **Foca no ponto cego** levantado na call. A amostra prova que o ponto cego existe e dá pra resolver.
- **Abre gancho, não fecha.** Deixa claro o que viria no completo, sem entregar de graça.

### Como escolher a amostra (conforme o diagnóstico)
- Ponto cego é dado que ninguém vê → **mini-dashboard com 1 KPI real** (chamar /esp-bi).
- Operação no caderno / planilha bagunçada → **amostra de planilha-banco que já acusa o problema** (chamar /esp-sheets).
- Tarefa manual repetitiva → **prova de conceito de 1 automação** (chamar /esp-ia).
- Construir sempre em versão enxuta — é amostra, não entrega.

### Como apresentar
- Mandar com uma mensagem curta: o número do ponto cego + "isso é uma amostra; o completo faz X, Y, Z".
- Marcar a conversa de proposta enquanto a curiosidade está quente.

---

## Saída / registro

- Salvar o diagnóstico (a frase + SPIN resumido) e o plano da amostra em `clientes/<Nome>/` se a pasta já existe. Senão, guardar pra colar no `briefing.md` quando rodar /novo-projeto.

## Integra com

- **/fluxo-cliente** — é a execução viva da qualificação → diagnóstico e a ponte pro entregável grátis (fases 1, 2 e 4).
- **/esp-bi**, **/esp-sheets**, **/esp-ia** — constroem a amostra em versão enxuta.
- **/novo-projeto** — quando o cliente valida a oferta e o trabalho vira projeto.

## Regras

**Sempre:**
- Diagnóstico em videochamada. SPIN na ordem — deixa o cliente nomear a dor e o custo.
- Anotar as frases do cliente literais — viram a copy da proposta.
- Amostra grátis pequena, com dado real, focada no ponto cego.

**Nunca:**
- Apresentar a solução antes da fase de Implicação — mata a venda cedo.
- Entregar o trabalho completo de graça — amostra abre gancho, não substitui a venda.
- Transformar a call num interrogatório — é conversa.
