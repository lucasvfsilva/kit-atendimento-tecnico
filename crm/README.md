# 🤝 CRM: aba Clientes

Funil de clientes na **mesma planilha** da aba [Máquinas](../google-sheets/), com três automações simples, sem programação.

**Por que no Google Sheets?** Fica aberto por link para quem quiser ver e se conecta direto com os dados das máquinas. A lógica é a mesma de qualquer CRM do mercado: empresa, contato, etapa do funil e próximo contato.

---

## Passo a passo

**1.** Na planilha **Atendimento – Clientes**, clique no **+** lá embaixo e crie a aba **Clientes**:

| | A | B | C | D | E | F |
|---|---|---|---|---|---|---|
| 1 | **Empresa** | **Contato** | **Etapa** | **Próximo contato** | **Máquinas aptas** | **Alerta** |
| 2 | Clínica Vida | Dra. Ana | | 03/11/2026 | | |
| 3 | Mercadinho Bom Preço | Sr. José | | 10/11/2026 | | |

**2. Etapa com menu suspenso:** selecione **C2:C** → **Dados → Validação de dados → Menu suspenso**, com as opções:

`Primeiro contato` · `Diagnóstico` · `Proposta enviada` · `Fechado – ganho` · `Fechado – perdido`

---

## ⚙️ Automação 1: buscar os dados das máquinas sozinho

Em **E2**, cole e arraste para baixo:

```
=CONT.SES(Máquinas!A:A; A2; Máquinas!G:G; "✅ Apto") & " de " & CONT.SE(Máquinas!A:A; A2)
```

O CRM mostra **"1 de 3"** sem você digitar nada. Se a aba Máquinas mudar, o CRM atualiza.

## ⚙️ Automação 2: alerta de follow-up

Em **F2**, cole e arraste para baixo:

```
=SE(D2=""; ""; SE(D2<=HOJE(); "⚠️ Contatar hoje"; "Em dia"))
```

## ⚙️ Automação 3: destacar quem precisa de atenção

Selecione **A2:F** → **Formatar → Formatação condicional → A fórmula personalizada é**:

```
=$F2="⚠️ Contatar hoje"
```

Fundo **amarelo**. A linha inteira do cliente fica destacada no dia do follow-up.

---

## ⭐ Bônus: lembrete diário por e-mail

O [`codigo/lembrete.gs`](../codigo/lembrete.gs) envia **todo dia de manhã** um e-mail com os clientes que precisam de contato.

1. Na planilha: **Extensões → Apps Script** → apague o conteúdo e cole o `lembrete.gs` → salve.
2. Selecione a função `lembreteFollowUp` e clique em **▶ Executar** uma vez para autorizar.
   Se aparecer *"O Google não verificou este app"*: **Avançado → Acessar (não seguro)**. É normal, porque o script é seu.
3. No menu lateral, **⏰ Acionadores → Adicionar acionador**:
   função `lembreteFollowUp` · **Baseado no tempo** · tipo **diário** (em inglês, *Day timer*) · **8h às 9h**.

---

**Próximo passo:** o resumo do atendimento no [Notion](../notion/).
