# Estratégia

> O que importa agora. Prioridades, metas, prazos.

## Fase

Lançamento e estruturação — negócio novo, sem histórico de empreendedorismo, operando solo com restrição severa de tempo.

## Gargalo atual

Tempo escasso (trabalho formal de 6h/dia no TJTO) + falta de processo nos departamentos da consultoria. Experiência técnica em BI existe, mas a operação do negócio (comercial, marketing, atendimento, produção) ainda roda no improviso.

## Prioridade principal

Usar IA para substituir esforço manual nos departamentos — começar pelo que trava mais: **estratégia de post + copy para o Instagram** (1-2 posts/semana, qualidade sobre volume).

## O que pode esperar

- Estruturação formal de proposta comercial (estrutura já existe na skill; falta a lógica de preço)
- Expansão de canais além do Instagram

## Próximas prioridades derivadas do gargalo

1. Automatizar criação de conteúdo para Instagram via skills do MazyOS
2. Documentar os dois produtos principais (ERP Low Cost stack 1 e stack 2) para reutilizar em propostas
3. Mapear rotinas semanais e transformar em skills (`/mapear-rotinas`)

## Posicionamento (confirmado)

- **Mensagem da marca:** BI / decisão. Vitrine sempre lidera com dado, ponto cego, "achismo" — não com "IA" (commoditizado). IA/sistema/site são o *como*, não o que se vende.
- **Modelo de oferta:** personalização (bespoke por cliente). Não trabalha com pacotes prontos.
- **Único produto "de prateleira":** Sistema de captação para corretores. O resto é sob medida.
- **Funil da bio:** diagnóstico gratuito é o chamariz universal (porta de entrada pra qualquer empresa); corretor entra segmentado abaixo.

## Processo de atendimento (padronizado)

Atendimento ponta a ponta agora roda na skill `/fluxo-cliente` (captação → diagnóstico → entregável + stack → amostra grátis → proposta → execução → entrega → caso).

**Funil de venda:**
1. **Diagnóstico gratuito** — sempre em videochamada, conduzido com **SPIN Selling**. Roteiro vivo na skill `/diagnostico` (pra ler na segunda tela durante a call, adapta a próxima pergunta conforme o cliente responde).
2. **Entregável grátis de amostra** — pequeno, com dado real do cliente, focado no ponto cego. Instiga curiosidade, mostra o estado desejado atendido e valida a oferta antes da proposta paga.
3. **Proposta paga** → fechamento → execução → entrega → caso.

**Especialistas técnicos (execução):** `/esp-bi` (carro-chefe), `/esp-sheets` (Stack 1), `/esp-supabase` (Stack 2 banco), `/esp-webapp` (front/site), `/esp-ia` (camada opcional), `/esp-seguranca` (portão de entrega).

**Decisão de stack:** cliente com stack obrigatória manda. Senão: ≤5 usuários + dado em planilha → Stack 1; bateu 2+ sinais de login/volume/API/criticidade → Stack 2. BI é camada sobre a fonte — não existe BI sem dado.

## Infraestrutura

- **Site / link-in-bio:** `ga-business.pages.dev` (Cloudflare Pages, plano grátis)
- **Deploy:** automático a cada push na branch `main` do repo `GA_Business` — a pasta servida é `bio-link/` (diretório de saída configurado no Cloudflare). Rodar `/salvar` publica o site.
- **Repo GitHub:** github.com/arcanjogab02-hub/GA_Business (verificar se está privado — contém `_memoria/`)
- **Pendente:** trocar link da bio do Instagram para `ga-business.pages.dev`. Domínio próprio (`.com.br`, ~R$40/ano) adiado por opção de custo zero.

## Contexto com prazo

Sem prazo definido por enquanto — ritmo ditado pela disponibilidade após o trabalho formal.
