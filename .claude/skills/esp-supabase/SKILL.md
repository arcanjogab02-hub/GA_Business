---
name: esp-supabase
description: >
  Especialista em Supabase (Stack 2 — banco): modela schema Postgres, configura RLS, Auth, API
  (PostgREST/RPC/Edge Functions), migrations e backup. Use quando o pedido envolver
  "/esp-supabase", "modelar banco", "supabase", "rls", "auth", "schema do banco", "stack 2",
  ou quando a /fluxo-cliente chamar na execução porque a stack escolhida é a 2.
---

# /esp-supabase — Especialista Supabase (Stack 2 — banco)

Cuida da camada de dados da Stack 2: Supabase (Postgres) como banco + front customizado.
Stack maior. Multiusuário com login, volume e concorrência alta, API/integração, tempo real, operação crítica.

## Quando usar

- Cliente fechou na Stack 2 (não cabe no Google Sheets da Stack 1).
- Precisa de login real, papéis, múltiplos usuários ao mesmo tempo.
- Volume de dados, concorrência, ou integração via API com outros sistemas.
- Operação crítica: não pode perder dado, precisa de backup confiável.
- Migração de um projeto que cresceu além da Stack 1 (chamada pela /esp-sheets).

## Workflow

1. **Levantar o domínio.** Entidades, relações, quem usa, quem pode o quê. Antes de qualquer SQL.
2. **Modelar o schema (Postgres).**
   - Tabelas normalizadas. PK `uuid` (`default gen_random_uuid()`).
   - Foreign keys explícitas. Índice em toda FK e em coluna usada em filtro.
   - `created_at` e `updated_at timestamptz` em toda tabela.
   - Enums quando o conjunto de valores é fixo. Naming `snake_case`.
3. **Habilitar RLS em TODA tabela.** Sem exceção. Tabela sem RLS é tabela aberta.
   - Policies por papel e por `auth.uid()`. Menor privilégio: começa fechado, abre o necessário.
   - Testa com usuário negativo: logado como A, confirmar que NÃO acessa dado de B.
4. **Configurar Auth.** Email/senha ou OTP. Definir roles. Mapear quem pode o quê numa tabela.
5. **Expor a API.**
   - PostgREST automático pro CRUD direto.
   - Funções RPC pra lógica que mora no banco.
   - Edge Functions pra lógica sensível que não pode ir pro client.
6. **Travar chaves.** No front só a `anon` key. `service_role` só em backend/edge function. `.env` fora do git.
7. **Realtime e Storage** quando o caso pedir: atualização ao vivo, upload de arquivo.
8. **Versionar migrations.** Todo SQL do schema vira migration. Nada de mudar só pelo painel sem registrar.
9. **Garantir backup/PITR.** Confirmar que o cliente tem como recuperar dado.

## Padrões GA

- PK `uuid`, nunca `serial` exposto. `snake_case` em tudo.
- `timestamptz` (com timezone), não `timestamp`.
- Soft delete (`deleted_at`) quando o dado tem valor histórico; hard delete quando não.
- RLS ligado por padrão. Policy só abre o que precisa.
- Schema versionado em SQL no repo do cliente. Painel é só pra inspecionar, não pra editar.
- Nada de `service_role` no front. Se apareceu no client, é bug de segurança.
- Simples primeiro. Só sobe pra Edge Function / Realtime / Storage quando o caso exige.

## Checklist de entrega

- [ ] Schema modelado: PKs uuid, FKs, índices, timestamps, enums onde cabe.
- [ ] RLS habilitado em TODA tabela.
- [ ] Policies por papel/`auth.uid()`, princípio do menor privilégio.
- [ ] Teste com usuário negativo passou (não acessa o que não é dele).
- [ ] Auth configurado: método, roles, mapa de permissões.
- [ ] API definida: PostgREST / RPC / Edge Function conforme o caso.
- [ ] Só `anon` key no front. `service_role` fora do client. `.env` fora do git.
- [ ] Migrations versionadas no repo.
- [ ] Backup/PITR confirmado.

## Integra com

- **/fluxo-cliente** — chama esta skill na execução quando a stack é a 2.
- **/esp-webapp** — o front consome a API gerada aqui.
- **/esp-seguranca** — auditoria de RLS e secrets antes de entregar.
- **/esp-bi** — o banco vira fonte do dashboard.
- **/esp-sheets** — de onde os projetos migram quando crescem além da Stack 1.

## Regras

**Sempre:**
- RLS em toda tabela, sem exceção.
- Testar acesso com usuário negativo.
- Versionar o schema em migrations.
- `anon` key no front, `service_role` só no backend.
- `.env` fora do git.
- Garantir caminho de backup/recuperação.

**Nunca:**
- Deixar tabela sem RLS.
- Colocar `service_role` no client.
- Alterar schema só pelo painel sem registrar a migration.
- Confiar em validação só no front pra dado sensível — a regra mora no banco.
- Subir feature (Realtime, Storage, Edge) que o caso não pediu.
