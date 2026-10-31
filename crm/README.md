# 🤝 CRM: funil de clientes no Google Sheets

CRM (*Customer Relationship Management*) é onde a empresa acompanha **cada cliente**: em que etapa ele está, o que já foi conversado e qual é o próximo passo.

### Por que montei o CRM no Google Sheets?

- **Fica aberto por link** para quem quiser ver (o HubSpot gratuito não gera link público).
- **Fica na mesma planilha** do inventário de máquinas, então dá para cruzar os dados: quantas máquinas de cada cliente estão aptas.
- A **lógica é a mesma** de qualquer CRM do mercado (HubSpot, Pipedrive, RD Station): contatos, funil, etapas e atividades.

---

## 🧩 Conceitos de CRM

| Conceito | O que é | Onde fica aqui |
|---|---|---|
| Empresa / contato | O cliente e a pessoa com quem falo | Aba **Clientes** |
| Funil (pipeline) | As etapas pelas quais o cliente passa | Coluna **Etapa** |
| Atividades | Ligações, reuniões, e-mails, visitas | Aba **Histórico** |
| Follow-up | O próximo contato combinado | Colunas **Próximo contato** e **Próxima ação** |

---

## 🔄 Etapas do funil

| Etapa | O que significa |
|---|---|
| 1. Primeiro contato | Cliente demonstrou interesse |
| 2. Diagnóstico técnico | Verificando computadores, sistemas e rede |
| 3. Apresentação da solução | Demonstração do sistema ao cliente |
| 4. Proposta enviada | Aguardando resposta |
| 5. Fechado – ganho | Virou cliente ✅ |
| 6. Fechado – perdido | Não fechou (registrar o motivo) ❌ |

---

## 1. Aba **Clientes**

Dica: importe [`clientes.csv`](clientes.csv) em **Arquivo → Importar → Inserir nova(s) página(s)** e renomeie a aba para **Clientes**.

| Col. | Campo | Como preencher |
|---|---|---|
| A | Empresa | Texto |
| B | Contato | Nome da pessoa |
| C | Telefone / e-mail | Texto |
| D | Segmento | Clínica, Varejo, Indústria... |
| E | Etapa | **Menu suspenso** com as 6 etapas acima |
| F | Último contato | Data |
| G | Próximo contato | Data |
| H | Próxima ação | Ex.: "Enviar orçamento de upgrade" |
| I | Dias sem contato | `=SE(F2=""; ""; HOJE()-F2)` |
| J | Máquinas | `=CONT.SE(Inventário!A:A; A2)` |
| K | Máquinas aptas | `=CONT.SES(Inventário!A:A; A2; Inventário!F:F; "✅ Apto")` |

As colunas **J** e **K** puxam os dados da aba [Inventário](../google-sheets/): o CRM mostra a situação técnica de cada cliente sem digitar nada.

### Alertas visuais (Formatar → Formatação condicional)

| Intervalo | Regra (fórmula personalizada) | Cor | Significado |
|---|---|---|---|
| A2:K | `=E($I2>7; ESQUERDA($E2; 1)<>"5"; ESQUERDA($E2; 1)<>"6")` | Vermelho claro | Mais de 7 dias sem contato |
| A2:K | `=E($G2<>""; $G2<=HOJE())` | Amarelo claro | Tem follow-up para hoje ou atrasado |

---

## 2. Aba **Histórico** (atividades)

Toda conversa vira uma linha, para qualquer pessoa do time saber o que foi combinado:

| Data | Empresa | Tipo | Resumo | Próximo passo |
|---|---|---|---|---|
| 03/11/2026 | Clínica Vida Saudável | Visita | Diagnóstico de 2 máquinas. Recepção-01 com RAM insuficiente. | Enviar orçamento de upgrade até 07/11 |

**Tipo** com menu suspenso: Ligação / Reunião / E-mail / Visita / WhatsApp.

---

## 3. Funil no **Painel**

Na aba Painel (veja [google-sheets](../google-sheets/)), adicione:

| Etapa | Quantidade |
|---|---|
| 1. Primeiro contato | `=CONT.SE(Clientes!E2:E; "1. Primeiro contato")` |
| 2. Diagnóstico técnico | `=CONT.SE(Clientes!E2:E; "2. Diagnóstico técnico")` |
| ... | (uma linha por etapa) |
| Taxa de conversão | `=CONT.SE(Clientes!E2:E; "5*") / CONT.VALORES(Clientes!A2:A)` |

**Gráfico:** selecione a tabela → **Inserir → Gráfico → Barras**.

---

## 4. (Bônus) Lembrete diário de follow-up por e-mail

O arquivo [`lembrete.gs`](lembrete.gs) envia **todo dia de manhã** um e-mail com os clientes que precisam de contato.

1. Na planilha: **Extensões → Apps Script** → crie um arquivo novo e cole o `lembrete.gs`.
2. Rode `lembreteFollowUp` uma vez pelo botão **▶ Executar** e autorize.
3. No menu lateral, **⏰ Acionadores → Adicionar acionador**:
   função `lembreteFollowUp` · **Baseado no tempo** · **Diário** · **8h às 9h**.

---

## 📎 E o HubSpot?

Também conheço a lógica de CRMs de mercado. Pratiquei no **HubSpot CRM (gratuito)**, criando o mesmo funil, e fiz o curso da **HubSpot Academy**. Como a estrutura é a mesma (contatos, empresas, negócios, etapas e atividades), consigo me adaptar ao CRM que a empresa usar.

---

## ✅ Checklist para o portfólio

- [ ] Prints: aba Clientes com alertas coloridos, aba Histórico, gráfico do funil
- [ ] Print do e-mail de lembrete recebido
