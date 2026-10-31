# 🖥️ Kit de Atendimento Técnico ao Cliente

Projeto que simula o trabalho de **consultoria técnica / pré-vendas**: verificar se os computadores de um cliente atendem aos requisitos de um sistema, explicar o resultado de forma clara e organizar tudo em **Google Sheets**, **Notion** e **CRM**.

> **Problema:** antes de implantar um sistema, a empresa precisa saber se as máquinas do cliente aguentam. Sem isso, a implantação trava, o cliente fica insatisfeito e o time de desenvolvimento recebe chamados que não são bugs.
>
> **Solução:** um script que faz o diagnóstico em segundos + um fluxo organizado para registrar, explicar e acompanhar cada cliente.

---

## 📂 O que tem neste repositório

| Pasta / arquivo | O que é |
|---|---|
| [`info_pc.py`](info_pc.py) | Script Python que mostra as configurações do PC e se ele atende aos requisitos |
| [`notion/`](notion/) | Como organizo clientes, diagnósticos, atas e o guia para o cliente no Notion |
| [`google-sheets/`](google-sheets/) | Planilha de inventário de máquinas, requisitos e painel de resultados |
| [`crm/`](crm/) | Funil de clientes (CRM) montado no Google Sheets, com lembrete automático de follow-up |
| [`versao-completa/`](versao-completa/) | Versão avançada do script: janela gráfica + envio dos resultados para o Google Sheets |

---

## ▶️ Como usar o script

```bash
pip install psutil
python info_pc.py
```

**Exemplo de saída:**
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

Os requisitos mínimos usados como exemplo: **8 GB de RAM**, **20 GB livres em disco** e **4 núcleos**.

---

## 🔄 O fluxo de atendimento (estudo de caso)

Cliente fictício: **Clínica Vida Saudável**, que quer implantar um sistema de gestão.

| # | Etapa | Ferramenta |
|---|---|---|
| 1 | Clínica entra no funil como **Primeiro contato** | CRM (Sheets) |
| 2 | Envio o **guia de diagnóstico** explicando o que vamos verificar e por quê | Notion (página pública) |
| 3 | Rodamos o `info_pc.py` em cada computador da clínica | Python |
| 4 | Resultados vão para o **inventário de máquinas** e o painel mostra quantas estão aptas | Google Sheets |
| 5 | Explico o resultado ao cliente e registro a **ata da reunião** com dores e requisitos | Notion |
| 6 | Atualizo a etapa no funil e agendo o próximo contato | CRM (Sheets) |

**Divisão das ferramentas:**
- **Google Sheets** → os **números**: inventário, funil de clientes, painel.
- **Notion** → os **textos**: guia para o cliente, página de cada cliente, atas, tutoriais.

---

## 🔒 Decisão de projeto: privacidade do cliente

O script **não envia nenhum dado pela internet**. Ele só mostra o resultado na tela. Na primeira versão, os dados iam automaticamente para a planilha, mas percebi que isso quebraria a confiança do cliente: ninguém quer instalar um programa que envia informações do PC sem ver. Agora o cliente vê o resultado e decide o que compartilhar.

---

## 🔗 Links

- 📘 Guia do cliente no Notion: *(em breve)*
- 📊 Planilha no Google Sheets: *(em breve)*
- 🎥 Vídeo de demonstração: *(em breve)*

---

## 🛠️ Tecnologias

Python · psutil · Google Sheets · Google Apps Script · Notion
