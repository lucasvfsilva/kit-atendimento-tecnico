# 🖥️ Kit de Atendimento Técnico ao Cliente

Atendimento completo de um cliente fictício, a **Clínica Vida Saudável**, com **3 computadores**: verificar se as máquinas atendem aos requisitos de um sistema e organizar o resultado em **Google Sheets**, **CRM** e **Notion**.

O objetivo é mostrar o básico bem feito, com cada ferramenta usada para o que ela faz melhor.

```
1. Verifico os PCs  →  2. Registro no Sheets  →  3. Acompanho no CRM  →  4. Resumo no Notion
```

---

## 📂 Estrutura

| Pasta | Conteúdo |
|---|---|
| [`codigo/`](codigo/) | Como verificar os requisitos do PC (atalhos, terminal e script), `info_pc.py` e `lembrete.gs` |
| [`google-sheets/`](google-sheets/) | Aba **Máquinas**: inventário dos computadores com status automático |
| [`crm/`](crm/) | Aba **Clientes**: funil, alerta de follow-up e dados puxados das máquinas |
| [`notion/`](notion/) | Página de **resumo do atendimento** para o cliente e o time |

---

## 📋 Requisitos mínimos (exemplo)

| Item | Mínimo |
|---|---|
| Memória RAM | 8 GB |
| Espaço livre em disco | 20 GB |
| Núcleos do processador | 4 |

---

## 🔄 O fluxo

| # | Etapa | Ferramenta | Resultado |
|---|---|---|---|
| 1 | Verificar RAM, disco e processador de cada PC | Atalhos do Windows, terminal ou `info_pc.py` | Dados de cada máquina |
| 2 | Registrar as máquinas e calcular o status | Google Sheets | "1 de 3 máquinas aptas" |
| 3 | Acompanhar a etapa do cliente e o próximo contato | CRM no Google Sheets | Alerta "⚠️ Contatar hoje" |
| 4 | Resumir o atendimento e os próximos passos | Notion | Página publicada para o cliente |

**Divisão das ferramentas:**
- **Google Sheets** → os **números** (máquinas, funil, contagens automáticas)
- **Notion** → o **texto** (resumo executivo, problemas encontrados, próximos passos)

---

## ▶️ Script de verificação

```bash
pip install psutil
python codigo/info_pc.py
```

```
=== Configurações do PC ===
Computador:  DESKTOP-FU4L3HL
Sistema:     Windows 11
RAM:         15.4 GB
Disco livre: 12.1 GB
Núcleos:     12

=== Requisitos mínimos ===
RAM 8 GB:          OK
Disco livre 20 GB: NÃO ATENDE
4 núcleos:         OK
```

Funciona em **Windows, Mac e Linux** e **não envia nenhum dado pela internet**: só mostra o resultado na tela.

---

## 🔗 Links

- 📊 Planilha (Máquinas + Clientes): *(em breve)*
- 📘 Resumo no Notion: *(em breve)*

---

## 🛠️ Tecnologias

Python · psutil · PowerShell · Google Sheets · Google Apps Script · Notion
