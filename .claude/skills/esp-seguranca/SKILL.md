---
name: esp-seguranca
description: >
  Revisão de segurança DEFENSIVA antes de entregar um projeto pro cliente: caça e corrige
  exposições (secrets, RLS, acesso, input, LGPD, backup). PORTÃO obrigatório da /fluxo-cliente
  na fase de entrega — não entrega sem passar por aqui. Invocar com "/esp-seguranca", ou quando
  o pedido for "revisão de segurança", "checar exposições", "rls", "secrets", "lgpd",
  "antes de entregar".
---

# /esp-seguranca — Revisão de Segurança (portão de entrega)

Revisão defensiva: encontrar e corrigir o que está exposto no projeto antes de mandar pro cliente. Não atacar nada — só revisar o próprio código e a própria infra. É etapa obrigatória; nenhum projeto vai pro cliente sem passar por aqui.

## Quando usar

- Final de qualquer projeto, antes da entrega (fase de entrega da /fluxo-cliente).
- Antes de subir algo público (Netlify, Cloudflare Pages, Web App do Apps Script).
- Quando suspeitar que vazou chave, senha ou dado no repo ou no front.
- Pedido direto: "revisa a segurança", "checa exposições", "tá seguro pra entregar?".

## Workflow

Rodar item por item. Cada achado vira um item corrigido no checklist — não passar adiante o que não foi resolvido.

1. **Secrets e chaves.** Procurar API key, service_role, senha, token ou string de conexão no front e no código commitado. Nada hardcoded. Segredo fica em `.env`, e `.env` fica fora do git (conferir `.gitignore`). Se algum segredo já entrou no histórico do git, não basta apagar o arquivo — **rotacionar a chave imediatamente** e reescrever/limpar o histórico.
2. **Repo privado.** Conferir se o repositório é privado. O repo pode conter `_memoria/` (dado da operação e de clientes). Se estiver público, fechar.
3. **Supabase RLS (Stack 2).** RLS habilitado em TODA tabela — sem exceção. Cada policy testada com usuário negativo: logar como um usuário e confirmar que ele NÃO acessa o que não é dele. No front, só a ANON key. `service_role` nunca sai do servidor.
4. **Apps Script Web App (Stack 1).** Revisar "Quem tem acesso" (evitar "Qualquer pessoa" sem necessidade real) e "Executar como" (geralmente o dono, não o usuário). Validar e sanitizar o input do `doPost`/`doGet`. Tratar a planilha-banco como dado sensível: proteger abas que não devem ser editadas.
5. **Validação de input.** Sanitizar tudo que vem do usuário, em qualquer stack. Nunca confiar no client — validar no servidor (Edge Function, RPC, Apps Script), não só no JS do front.
6. **LGPD.** Minimizar coleta: só pedir o dado pessoal que o sistema realmente usa. Ter consentimento quando for o caso. Saber onde o dado mora, quem acessa e por quanto tempo (retenção). Aplicar menor privilégio: cada acesso só ao que precisa.
7. **Backup e recuperação.** Confirmar que o cliente consegue recuperar se algo quebrar ou for apagado. Stack 2: backup/export do Postgres. Stack 1: cópia/versão da planilha. Testar a recuperação, não só assumir que existe.
8. **Fechar.** Só liberar a entrega quando todo o checklist estiver marcado. O que não deu pra resolver vira pendência explícita pro cliente — por escrito, não no esquecimento.

## Checklist de entrega

Secrets e repo:
- [ ] Nenhuma API key, `service_role`, senha ou token hardcoded no front ou no código
- [ ] `.env` existe e está no `.gitignore` (não foi commitado)
- [ ] Histórico do git limpo de segredos; o que vazou foi rotacionado
- [ ] Repositório está privado
- [ ] `_memoria/` não está exposta em repo público

Stack 2 (Supabase):
- [ ] RLS habilitado em TODAS as tabelas
- [ ] Policies testadas com usuário negativo (não acessa o que não é dele)
- [ ] Front usa só ANON key; `service_role` só no servidor

Stack 1 (Apps Script / Sheets):
- [ ] "Quem tem acesso" e "Executar como" revisados (sem "qualquer pessoa" à toa)
- [ ] Input do `doPost`/`doGet` validado e sanitizado
- [ ] Abas sensíveis da planilha-banco protegidas

Geral:
- [ ] Todo input do usuário é validado/sanitizado no servidor
- [ ] LGPD: coleta minimizada, consentimento, retenção e acessos definidos
- [ ] Menor privilégio aplicado nos acessos
- [ ] Backup configurado e recuperação testada
- [ ] Pendências de segurança que sobraram estão registradas por escrito pro cliente

## Padrões GA

- Segredo nunca no código. Sempre `.env` + `.gitignore`, ou variável de ambiente no Netlify/Cloudflare.
- No front só anda chave pública (ANON). Chave privada só no servidor.
- Não confiar no client em nenhuma stack. Validar do lado de quem manda.
- RLS ligado por padrão. Tabela sem RLS é falha, não exceção.
- Menor privilégio em tudo: acesso, escopo de chave, permissão de planilha.
- Vazou? Rotaciona primeiro, investiga depois.

## Integra com

- **/fluxo-cliente** — é o portão da fase de entrega; a /fluxo-cliente chama aqui antes de liberar.
- **/esp-supabase** — RLS, Auth e policies (Stack 2).
- **/esp-sheets** — acesso ao Web App e proteção de abas (Stack 1).
- **/esp-webapp** — secrets no bundle e exposição no front.
- **/esp-ia** — quando dado do cliente vai pra serviço externo de IA.
- **/salvar** — verificar repo privado antes do push.

## Regras

Sempre:
- Tratar como DEFENSIVO: revisar e corrigir o próprio projeto.
- Rodar o checklist inteiro antes de liberar a entrega.
- Rotacionar imediatamente qualquer segredo que tenha vazado.
- Testar policy com usuário negativo, não só ler a policy.
- Registrar por escrito qualquer pendência que sobrar.

Nunca:
- Atacar, testar ou invadir sistema de terceiros.
- Deixar segredo no front ou no histórico do git.
- Subir front com `service_role` ou qualquer chave privada.
- Deixar tabela Supabase sem RLS.
- Liberar entrega com checklist incompleto.
