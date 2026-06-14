# Fluxo de atendimento — mapa rápido

Referência de uma olhada: cada etapa e a skill que roda nela. O playbook completo está em `/fluxo-cliente`.

```
CAPTAÇÃO → DIAGNÓSTICO (call) → ENTREGÁVEL+STACK → AMOSTRA GRÁTIS → PROPOSTA → FECHAMENTO → EXECUÇÃO → ENTREGA → CASO
```

## As 9 etapas

| # | Etapa | Skill | Portão (só avança quando…) |
|---|---|---|---|
| 1 | Captação e qualificação | `/fluxo-cliente` | é fit? → agenda a videochamada |
| 2 | Diagnóstico gratuito (call + SPIN) | `/diagnostico` | tenho 1 frase: problema + número do ponto cego |
| 3 | Definir entregável + stack | `/fluxo-cliente` (tabela de decisão) | sei o que entregar e em qual stack |
| 4 | Entregável grátis (amostra) | `/diagnostico` (Roteiro 2) + `/esp-*` | cliente viu a amostra e validou a oferta |
| 5 | Proposta (sem valor automático) | `/fluxo-cliente` | proposta enviada |
| 6 | Fechamento e estruturação | `/novo-projeto` | pasta `clientes/<Nome>/` criada |
| 7 | Execução | `/esp-bi` `/esp-sheets` `/esp-supabase` `/esp-webapp` `/esp-ia` | funcionando em teste |
| 8 | Entrega | `/esp-seguranca` | cliente usando, sabendo usar, e seguro |
| 9 | Pós e caso de sucesso | `caso.md` + `/publicar-tema` `/carrossel` | caso documentado |

## Especialistas técnicos (etapa 7)

| Skill | Quando | 
|---|---|
| `/esp-bi` | dashboard, KPI, análise — **carro-chefe** |
| `/esp-sheets` | Stack 1: Sheets-banco + Apps Script |
| `/esp-supabase` | Stack 2: banco Postgres (schema, RLS, auth, API) |
| `/esp-webapp` | front JS/HTML/CSS, site, landing |
| `/esp-ia` | camada de IA aplicada (opcional, você decide) |
| `/esp-seguranca` | revisão antes de entregar (portão obrigatório) |

## Decisão de stack (regra rápida)

1. **Cliente tem stack obrigatória?** → usa a dele. Fim.
2. **≤5 usuários, dado em planilha, barato, não crítico** → Stack 1.
3. **Bateu 2+ de:** login real, volume/concorrência, API/integração, operação crítica → Stack 2.
4. **BI** é camada sobre a fonte — não existe BI sem dado.

## Como isso bate com o painel.html

O kanban do painel segue as mesmas etapas:

```
Prospect → Diagnóstico → [Amostra] → Proposta → Execução → Entregue
```

O painel já tem a coluna *Amostra grátis*. Pra alimentar: rode `/painel` (eu atualizo `dados/prospeccoes.json`) e importe o arquivo no painel — ele **soma**, não apaga.
