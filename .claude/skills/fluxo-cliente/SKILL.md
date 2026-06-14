---
name: fluxo-cliente
description: >
  Playbook de atendimento ponta a ponta — da captação do lead à entrega e ao caso de sucesso.
  Conduz o fluxo: qualificar → diagnóstico gratuito (videochamada + SPIN) → definir entregável + stack →
  entregável grátis de amostra → proposta → fechar (chama /novo-projeto) → executar (chama os
  especialistas técnicos) → entregar → documentar caso.
  Use quando o usuário disser "/fluxo-cliente", "novo lead", "cheguei num cliente", "fechei com X",
  "como conduzir esse atendimento", "que stack uso pra esse cliente" ou pedir pra padronizar o atendimento.
---

# /fluxo-cliente — Atendimento ponta a ponta

Fluxo único pra conduzir um projeto do primeiro contato à entrega. Cobre a parte humana
(comercial, diagnóstico, proposta, handoff) e a técnica (stack, execução, segurança).

BI é o carro-chefe. Marketing e IA entram como diferencial e camada operacional — nunca como a venda principal.
A venda lidera com **dado / decisão / ponto cego**, não com "IA" (commoditizado). IA e sistema são o *como*.

São 9 fases. Não pular fase — mas em projeto pequeno várias resolvem em minutos.
Cada fase tem um **portão**: só avança quando o portão fecha.

---

## Fase 1 — Captação e qualificação

Lead chegou (Instagram, indicação, diagnóstico gratuito da bio). Antes de investir tempo, qualificar.

Avaliar na conversa:
- Que problema te trouxe aqui? (deixa o cliente falar o sintoma, não a solução)
- Já tem planilha/sistema hoje? Como decide as coisas?
- É PME? Tem como investir num projeto sob medida?

**Portão:** é fit? (PME, decide no achismo ou sem visibilidade de dado, tem orçamento mínimo.)
Se for fit → **agendar a videochamada de diagnóstico**. Se não → ofertar o diagnóstico/conteúdo gratuito e encerrar sem queimar tempo.

---

## Fase 2 — Diagnóstico gratuito (videochamada + SPIN)

O diagnóstico é **sempre em videochamada**. Conduzir ao vivo com a skill **/diagnostico**, que roda o
roteiro **SPIN Selling** na tua segunda tela e adapta a próxima pergunta conforme o cliente responde.
Não perguntar "o que você quer" — descobrir o ponto cego. Quem nomeia a dor e o custo é o cliente.

O que sai da call:
- **Onde mora o dado** hoje (planilha, caderno, sistema, cabeça do dono)
- **Como decide** hoje e onde erra por falta de número
- **Quem vai usar** o que for entregue, e quantos
- **O ponto cego** — o número que ele não vê e que muda o jogo (ex: "1.126 de 1.200 clientes inativos")

**Portão:** consigo nomear em uma frase o problema real e o número que o resolve?
Essa frase é o gancho do entregável grátis e da proposta.

---

## Fase 3 — Definir entregável + stack

Com o diagnóstico na mão, decidir **o que** entregar e **em que** stack.

### Regra zero
Se o cliente já tem stack obrigatória (ferramenta que ele exige manter), ela manda. Ignora a tabela.

### Tabela de decisão

| Sinal | Stack 1 — Sheets + Apps Script | Stack 2 — Supabase + front |
|---|---|---|
| Nº de usuários | até ~5 | mais de 5 / tende a crescer |
| Login e permissões | não precisa de login robusto | precisa login real e papéis |
| Volume / concorrência | baixo, o dado cabe em planilha | volume alto, escrita concorrente, tempo real |
| Integração / API | não precisa | precisa de API / integrações externas |
| Orçamento | baixo | comporta mais |
| Criticidade | baixa chance de quebrar, não é crítico | operação crítica, não pode cair |

Regra prática: **bateu 2+ sinais da coluna Stack 2 → Stack 2.** Na dúvida com cliente pequeno,
começa na Stack 1 (mais barata e rápida) e migra se crescer.

### BI (carro-chefe)
BI não é stack separada — é a camada de visualização sobre o dado que vive na Stack 1 ou 2.
**Não existe BI sem dado.** Se o cliente quer dashboard mas não tem dado estruturado, o primeiro
entregável é estruturar a fonte (Stack 1 ou 2); o BI vem em cima.

### IA aplicada
Sempre **avaliar e sugerir** onde a IA encaixa (automação, classificação, geração, análise) — é diferencial.
Mas a decisão de incluir é tua, caso a caso. Quando fizer sentido, marcar na proposta como item opcional.

**Portão:** entregável definido + stack escolhida (com a regra zero respeitada).

---

## Fase 4 — Entregável grátis (amostra / validação da oferta)

Antes da proposta paga, entregar uma **amostra grátis e enxuta**. Objetivo triplo: instigar curiosidade,
mostrar que o estado desejado é alcançável, e validar a oferta antes de cobrar.

- Depende do diagnóstico e da stack/entregável decididos na fase 3.
- Pequena e rápida (tempo é escasso): mostra um pedaço do resultado, não o todo. Ex: mini-dashboard com 1 KPI real, planilha que acusa o ponto cego, amostra de automação.
- Construir com o especialista certo em **versão amostra** (/esp-bi, /esp-sheets, /esp-ia). O roteiro de como escolher e enquadrar está na **/diagnostico** (Roteiro 2).
- Usar o **dado real do cliente** sempre que possível. Deixar claro o antes/depois e abrir o gancho pra oferta paga.

**Portão:** cliente viu a amostra e validou que quer o resultado completo.

---

## Fase 5 — Proposta

Montar a proposta. Estrutura **sem valor** — o número você define na hora:

- **Problema** — a frase do diagnóstico, com o número do ponto cego
- **Entregável** — o que vai existir no fim, concreto
- **Stack** — a escolhida na fase 3, em linguagem do cliente (sem jargão)
- **Escopo** — o que está dentro / o que está fora
- **IA / extras** — opcionais, se sugeridos
- **Prazo** — realista pro tempo disponível (solo, 6h/dia de trabalho formal)
- **Condições** — pagamento, suporte, revisões — **valor: [definir]**

Tom: direto, dado antes de argumento, sem promessa de guru. Aplicar `_memoria/preferencias.md`.
Reusar as palavras que o cliente disse na call (estado desejado) — vêm do registro da /diagnostico.

**Portão:** proposta enviada.

---

## Fase 6 — Fechamento e estruturação

Cliente aceitou. Estruturar o trabalho:

1. Rodar **/novo-projeto** pra criar `clientes/<Nome>/` com CLAUDE.md, briefing e subpastas das entregas.
2. Colar o diagnóstico e a proposta fechada no `briefing.md`.
3. Registrar a stack escolhida e o porquê no CLAUDE.md do projeto.

**Portão:** pasta do cliente criada e briefing preenchido.

---

## Fase 7 — Execução

Chamar o especialista conforme a stack/entregável. Cada um tem sua skill:

- Stack 1 (Sheets / Apps Script) → **/esp-sheets**
- Stack 2 — banco (Supabase) → **/esp-supabase**
- Stack 2 — front / site → **/esp-webapp**
- Dashboard / análise (carro-chefe) → **/esp-bi**
- Camada de IA (se entrou) → **/esp-ia**

Ordem típica: estruturar o dado → construir → camada de BI → camada de IA (se entrou).

**Portão:** entregável funcionando em ambiente de teste.

---

## Fase 8 — Entrega

Antes de mostrar pro cliente:

1. **Revisão de segurança** → rodar **/esp-seguranca** (secrets, RLS, acesso, LGPD). Não entregar sem isso.
2. Testar o caminho real que o cliente vai percorrer.
3. Documentar pro cliente: um guia curto de "como usar", na linguagem dele (não técnica).
4. Handoff: mostrar funcionando, treinar quem vai operar.

**Portão:** cliente usando, sabendo usar, e seguro.

---

## Fase 9 — Pós e caso de sucesso

1. Documentar em `clientes/<Nome>/caso.md` — problema, número antes/depois, o que foi entregue.
2. Pedir depoimento enquanto o resultado está fresco.
3. Reusar o caso em conteúdo (/publicar-tema, /carrossel) e em propostas futuras.

**Portão:** caso documentado.

---

## Regras

- O diagnóstico é sempre em videochamada, conduzido com SPIN via **/diagnostico**.
- Não pular o diagnóstico — é onde a venda acontece. Proposta sem diagnóstico vira orçamento de commodity.
- Antes de cobrar, validar a oferta com um **entregável grátis de amostra** (pequeno, com dado real, focado no ponto cego).
- A regra zero da stack sempre vence: cliente com stack obrigatória usa a dele.
- Nunca prometer prazo que o tempo solo (6h/dia de trabalho formal) não comporta.
- Nunca entregar sem passar pela /esp-seguranca.
- BI sempre precisa de fonte de dado estruturada antes — não existe dashboard sem dado.
- IA é sugestão, não imposição — você decide caso a caso.
- Valor de proposta nunca é preenchido automaticamente — sempre [definir] pra você decidir.
